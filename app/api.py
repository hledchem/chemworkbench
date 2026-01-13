# app/api.py
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Any, Dict, Optional
from pathlib import Path
import tempfile
import json

from core.registry import get_all, get_by_id
from core.file_sniffer import sniff_file
from core.validator import validate_molecule  # if you added validator/schema
# processors should implement your BaseProcessor (read/plot/write)
# from processors.simple_props import SimplePropsProcessor  # example

app = FastAPI(title="ChemWorkBench API")

# Serve demo UI from app/static (optional)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


class MoleculeModel(BaseModel):
    __root__: Dict[str, Any]


@app.post("/api/process/json")
async def process_json(mol: MoleculeModel, processor_id: Optional[str] = None):
    """
    Process an in-memory molecule JSON.
    - If processor_id is provided, use that processor.
    - Otherwise use a default processor (first registered) or return an error.
    """
    mol_json = mol.__root__
    # optional: validate against schema if you added one
    try:
        validate_molecule(mol_json)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Validation error: {e}")

    # choose processor
    proc_cls = None
    if processor_id:
        proc_cls = get_by_id(processor_id)
        if not proc_cls:
            raise HTTPException(status_code=404, detail=f"Processor not found: {processor_id}")
    else:
        procs = get_all()
        if not procs:
            raise HTTPException(status_code=500, detail="No processors registered")
        proc_cls = procs[0]

    proc = proc_cls()
    try:
        result = proc.plot(mol_json)  # use plot for in-memory data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processor error: {e}")

    return {"processor": proc.id, "result": result}


@app.post("/api/process/file")
async def process_file(file: UploadFile = File(...), processor_id: Optional[str] = Form(None)):
    """
    Upload a file and process it.
    - If processor_id is provided, use that processor.
    - Otherwise sniff the file to find candidates.
    """
    # write uploaded file to a temp file so existing processors can read it
    suffix = Path(file.filename).suffix or ""
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp_path = Path(tmp.name)
        content = await file.read()
        tmp.write(content)

    # choose processor
    proc_cls = None
    if processor_id:
        proc_cls = get_by_id(processor_id)
        if not proc_cls:
            tmp_path.unlink(missing_ok=True)
            raise HTTPException(status_code=404, detail=f"Processor not found: {processor_id}")
    else:
        candidates = sniff_file(tmp_path)
        if not candidates:
            tmp_path.unlink(missing_ok=True)
            raise HTTPException(status_code=400, detail="No matching processors found for uploaded file")
        proc_cls = candidates[0]

    proc = proc_cls()
    try:
        data = proc.read(tmp_path)
        result = proc.plot(data)
    except Exception as e:
        tmp_path.unlink(missing_ok=True)
        raise HTTPException(status_code=500, detail=f"Processor error: {e}")

    tmp_path.unlink(missing_ok=True)
    return {"processor": proc.id, "result": result}


@app.get("/api/processors")
def list_processors_api():
    procs = get_all()
    return [{"id": p.id, "name": p.name, "file_types": p.file_types} for p in procs]
