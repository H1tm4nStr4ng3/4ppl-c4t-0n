from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database


app = FastAPI(title='SGApp API Completa')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try: yield db
    finally: db.close()


# API para PA_DI_FA
@app.get("/pa-di-fa/", response_model=List[schemas.PA_DI_FA])
def list_pa_di_fa(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_DI_FA).offset(skip).limit(limit).all()

@app.post("/pa-di-fa/", response_model=schemas.PA_DI_FA)
def create_pa_di_fa(item: schemas.PA_DI_FACreate, db: Session = Depends(get_db)):
    db_item = models.PA_DI_FA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-di-fa/{id}", response_model=schemas.PA_DI_FA)
def update_pa_di_fa(id: int, item: schemas.PA_DI_FAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_DI_FA).filter(models.PA_DI_FA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-di-fa/{id}")
def delete_pa_di_fa(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_DI_FA).filter(models.PA_DI_FA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_DI_PR
@app.get("/pa-di-pr/", response_model=List[schemas.PA_DI_PR])
def list_pa_di_pr(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_DI_PR).offset(skip).limit(limit).all()

@app.post("/pa-di-pr/", response_model=schemas.PA_DI_PR)
def create_pa_di_pr(item: schemas.PA_DI_PRCreate, db: Session = Depends(get_db)):
    db_item = models.PA_DI_PR(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-di-pr/{id}", response_model=schemas.PA_DI_PR)
def update_pa_di_pr(id: int, item: schemas.PA_DI_PRUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_DI_PR).filter(models.PA_DI_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-di-pr/{id}")
def delete_pa_di_pr(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_DI_PR).filter(models.PA_DI_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_DI_RA
@app.get("/pa-di-ra/", response_model=List[schemas.PA_DI_RA])
def list_pa_di_ra(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_DI_RA).offset(skip).limit(limit).all()

@app.post("/pa-di-ra/", response_model=schemas.PA_DI_RA)
def create_pa_di_ra(item: schemas.PA_DI_RACreate, db: Session = Depends(get_db)):
    db_item = models.PA_DI_RA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-di-ra/{id}", response_model=schemas.PA_DI_RA)
def update_pa_di_ra(id: int, item: schemas.PA_DI_RAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_DI_RA).filter(models.PA_DI_RA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-di-ra/{id}")
def delete_pa_di_ra(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_DI_RA).filter(models.PA_DI_RA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_AC
@app.get("/pa-eq-ac/", response_model=List[schemas.PA_EQ_AC])
def list_pa_eq_ac(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_AC).offset(skip).limit(limit).all()

@app.post("/pa-eq-ac/", response_model=schemas.PA_EQ_AC)
def create_pa_eq_ac(item: schemas.PA_EQ_ACCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_AC(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-ac/{id}", response_model=schemas.PA_EQ_AC)
def update_pa_eq_ac(id: int, item: schemas.PA_EQ_ACUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_AC).filter(models.PA_EQ_AC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-ac/{id}")
def delete_pa_eq_ac(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_AC).filter(models.PA_EQ_AC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_CA
@app.get("/pa-eq-ca/", response_model=List[schemas.PA_EQ_CA])
def list_pa_eq_ca(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_CA).offset(skip).limit(limit).all()

@app.post("/pa-eq-ca/", response_model=schemas.PA_EQ_CA)
def create_pa_eq_ca(item: schemas.PA_EQ_CACreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_CA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-ca/{id}", response_model=schemas.PA_EQ_CA)
def update_pa_eq_ca(id: int, item: schemas.PA_EQ_CAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CA).filter(models.PA_EQ_CA.id_equi == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-ca/{id}")
def delete_pa_eq_ca(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CA).filter(models.PA_EQ_CA.id_equi == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_CB
@app.get("/pa-eq-cb/", response_model=List[schemas.PA_EQ_CB])
def list_pa_eq_cb(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_CB).offset(skip).limit(limit).all()

@app.post("/pa-eq-cb/", response_model=schemas.PA_EQ_CB)
def create_pa_eq_cb(item: schemas.PA_EQ_CBCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_CB(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-cb/{id}", response_model=schemas.PA_EQ_CB)
def update_pa_eq_cb(id: int, item: schemas.PA_EQ_CBUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CB).filter(models.PA_EQ_CB.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-cb/{id}")
def delete_pa_eq_cb(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CB).filter(models.PA_EQ_CB.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_CH
@app.get("/pa-eq-ch/", response_model=List[schemas.PA_EQ_CH])
def list_pa_eq_ch(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_CH).offset(skip).limit(limit).all()

@app.post("/pa-eq-ch/", response_model=schemas.PA_EQ_CH)
def create_pa_eq_ch(item: schemas.PA_EQ_CHCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_CH(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-ch/{id}", response_model=schemas.PA_EQ_CH)
def update_pa_eq_ch(id: int, item: schemas.PA_EQ_CHUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CH).filter(models.PA_EQ_CH.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-ch/{id}")
def delete_pa_eq_ch(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CH).filter(models.PA_EQ_CH.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_CI
@app.get("/pa-eq-ci/", response_model=List[schemas.PA_EQ_CI])
def list_pa_eq_ci(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_CI).offset(skip).limit(limit).all()

@app.post("/pa-eq-ci/", response_model=schemas.PA_EQ_CI)
def create_pa_eq_ci(item: schemas.PA_EQ_CICreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_CI(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-ci/{id}", response_model=schemas.PA_EQ_CI)
def update_pa_eq_ci(id: int, item: schemas.PA_EQ_CIUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CI).filter(models.PA_EQ_CI.id_equi == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-ci/{id}")
def delete_pa_eq_ci(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CI).filter(models.PA_EQ_CI.id_equi == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_CV
@app.get("/pa-eq-cv/", response_model=List[schemas.PA_EQ_CV])
def list_pa_eq_cv(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_CV).offset(skip).limit(limit).all()

@app.post("/pa-eq-cv/", response_model=schemas.PA_EQ_CV)
def create_pa_eq_cv(item: schemas.PA_EQ_CVCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_CV(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-cv/{id}", response_model=schemas.PA_EQ_CV)
def update_pa_eq_cv(id: int, item: schemas.PA_EQ_CVUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CV).filter(models.PA_EQ_CV.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-cv/{id}")
def delete_pa_eq_cv(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_CV).filter(models.PA_EQ_CV.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_DC
@app.get("/pa-eq-dc/", response_model=List[schemas.PA_EQ_DC])
def list_pa_eq_dc(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_DC).offset(skip).limit(limit).all()

@app.post("/pa-eq-dc/", response_model=schemas.PA_EQ_DC)
def create_pa_eq_dc(item: schemas.PA_EQ_DCCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_DC(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-dc/{id}", response_model=schemas.PA_EQ_DC)
def update_pa_eq_dc(id: int, item: schemas.PA_EQ_DCUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_DC).filter(models.PA_EQ_DC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-dc/{id}")
def delete_pa_eq_dc(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_DC).filter(models.PA_EQ_DC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_EQ
@app.get("/pa-eq-eq/", response_model=List[schemas.PA_EQ_EQ])
def list_pa_eq_eq(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_EQ).offset(skip).limit(limit).all()

@app.post("/pa-eq-eq/", response_model=schemas.PA_EQ_EQ)
def create_pa_eq_eq(item: schemas.PA_EQ_EQCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_EQ(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-eq/{id}", response_model=schemas.PA_EQ_EQ)
def update_pa_eq_eq(id: int, item: schemas.PA_EQ_EQUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_EQ).filter(models.PA_EQ_EQ.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-eq/{id}")
def delete_pa_eq_eq(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_EQ).filter(models.PA_EQ_EQ.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_EX
@app.get("/pa-eq-ex/", response_model=List[schemas.PA_EQ_EX])
def list_pa_eq_ex(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_EX).offset(skip).limit(limit).all()

@app.post("/pa-eq-ex/", response_model=schemas.PA_EQ_EX)
def create_pa_eq_ex(item: schemas.PA_EQ_EXCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_EX(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-ex/{id}", response_model=schemas.PA_EQ_EX)
def update_pa_eq_ex(id: int, item: schemas.PA_EQ_EXUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_EX).filter(models.PA_EQ_EX.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-ex/{id}")
def delete_pa_eq_ex(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_EX).filter(models.PA_EQ_EX.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_HM
@app.get("/pa-eq-hm/", response_model=List[schemas.PA_EQ_HM])
def list_pa_eq_hm(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_HM).offset(skip).limit(limit).all()

@app.post("/pa-eq-hm/", response_model=schemas.PA_EQ_HM)
def create_pa_eq_hm(item: schemas.PA_EQ_HMCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_HM(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-hm/{id}", response_model=schemas.PA_EQ_HM)
def update_pa_eq_hm(id: int, item: schemas.PA_EQ_HMUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_HM).filter(models.PA_EQ_HM.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-hm/{id}")
def delete_pa_eq_hm(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_HM).filter(models.PA_EQ_HM.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_LE
@app.get("/pa-eq-le/", response_model=List[schemas.PA_EQ_LE])
def list_pa_eq_le(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_LE).offset(skip).limit(limit).all()

@app.post("/pa-eq-le/", response_model=schemas.PA_EQ_LE)
def create_pa_eq_le(item: schemas.PA_EQ_LECreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_LE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-le/{id}", response_model=schemas.PA_EQ_LE)
def update_pa_eq_le(id: int, item: schemas.PA_EQ_LEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_LE).filter(models.PA_EQ_LE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-le/{id}")
def delete_pa_eq_le(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_LE).filter(models.PA_EQ_LE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_MA
@app.get("/pa-eq-ma/", response_model=List[schemas.PA_EQ_MA])
def list_pa_eq_ma(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_MA).offset(skip).limit(limit).all()

@app.post("/pa-eq-ma/", response_model=schemas.PA_EQ_MA)
def create_pa_eq_ma(item: schemas.PA_EQ_MACreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_MA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-ma/{id}", response_model=schemas.PA_EQ_MA)
def update_pa_eq_ma(id: int, item: schemas.PA_EQ_MAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_MA).filter(models.PA_EQ_MA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-ma/{id}")
def delete_pa_eq_ma(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_MA).filter(models.PA_EQ_MA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_MO
@app.get("/pa-eq-mo/", response_model=List[schemas.PA_EQ_MO])
def list_pa_eq_mo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_MO).offset(skip).limit(limit).all()

@app.post("/pa-eq-mo/", response_model=schemas.PA_EQ_MO)
def create_pa_eq_mo(item: schemas.PA_EQ_MOCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_MO(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-mo/{id}", response_model=schemas.PA_EQ_MO)
def update_pa_eq_mo(id: int, item: schemas.PA_EQ_MOUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_MO).filter(models.PA_EQ_MO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-mo/{id}")
def delete_pa_eq_mo(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_MO).filter(models.PA_EQ_MO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_MR
@app.get("/pa-eq-mr/", response_model=List[schemas.PA_EQ_MR])
def list_pa_eq_mr(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_MR).offset(skip).limit(limit).all()

@app.post("/pa-eq-mr/", response_model=schemas.PA_EQ_MR)
def create_pa_eq_mr(item: schemas.PA_EQ_MRCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_MR(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-mr/{id}", response_model=schemas.PA_EQ_MR)
def update_pa_eq_mr(id: str, item: schemas.PA_EQ_MRUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_MR).filter(models.PA_EQ_MR.codigo_interno == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-mr/{id}")
def delete_pa_eq_mr(id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_MR).filter(models.PA_EQ_MR.codigo_interno == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_MV
@app.get("/pa-eq-mv/", response_model=List[schemas.PA_EQ_MV])
def list_pa_eq_mv(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_MV).offset(skip).limit(limit).all()

@app.post("/pa-eq-mv/", response_model=schemas.PA_EQ_MV)
def create_pa_eq_mv(item: schemas.PA_EQ_MVCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_MV(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-mv/{id}", response_model=schemas.PA_EQ_MV)
def update_pa_eq_mv(id: int, item: schemas.PA_EQ_MVUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_MV).filter(models.PA_EQ_MV.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-mv/{id}")
def delete_pa_eq_mv(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_MV).filter(models.PA_EQ_MV.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_PA
@app.get("/pa-eq-pa/", response_model=List[schemas.PA_EQ_PA])
def list_pa_eq_pa(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_PA).offset(skip).limit(limit).all()

@app.post("/pa-eq-pa/", response_model=schemas.PA_EQ_PA)
def create_pa_eq_pa(item: schemas.PA_EQ_PACreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_PA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-pa/{id}", response_model=schemas.PA_EQ_PA)
def update_pa_eq_pa(id: int, item: schemas.PA_EQ_PAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_PA).filter(models.PA_EQ_PA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-pa/{id}")
def delete_pa_eq_pa(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_PA).filter(models.PA_EQ_PA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_PR
@app.get("/pa-eq-pr/", response_model=List[schemas.PA_EQ_PR])
def list_pa_eq_pr(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_PR).offset(skip).limit(limit).all()

@app.post("/pa-eq-pr/", response_model=schemas.PA_EQ_PR)
def create_pa_eq_pr(item: schemas.PA_EQ_PRCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_PR(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-pr/{id}", response_model=schemas.PA_EQ_PR)
def update_pa_eq_pr(id: int, item: schemas.PA_EQ_PRUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_PR).filter(models.PA_EQ_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-pr/{id}")
def delete_pa_eq_pr(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_PR).filter(models.PA_EQ_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_RE
@app.get("/pa-eq-re/", response_model=List[schemas.PA_EQ_RE])
def list_pa_eq_re(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_RE).offset(skip).limit(limit).all()

@app.post("/pa-eq-re/", response_model=schemas.PA_EQ_RE)
def create_pa_eq_re(item: schemas.PA_EQ_RECreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_RE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-re/{id}", response_model=schemas.PA_EQ_RE)
def update_pa_eq_re(id: str, item: schemas.PA_EQ_REUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_RE).filter(models.PA_EQ_RE.id_reactivo == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-re/{id}")
def delete_pa_eq_re(id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_RE).filter(models.PA_EQ_RE.id_reactivo == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_RP
@app.get("/pa-eq-rp/", response_model=List[schemas.PA_EQ_RP])
def list_pa_eq_rp(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_RP).offset(skip).limit(limit).all()

@app.post("/pa-eq-rp/", response_model=schemas.PA_EQ_RP)
def create_pa_eq_rp(item: schemas.PA_EQ_RPCreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_RP(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-rp/{id}", response_model=schemas.PA_EQ_RP)
def update_pa_eq_rp(id: int, item: schemas.PA_EQ_RPUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_RP).filter(models.PA_EQ_RP.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-rp/{id}")
def delete_pa_eq_rp(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_RP).filter(models.PA_EQ_RP.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_EQ_VE
@app.get("/pa-eq-ve/", response_model=List[schemas.PA_EQ_VE])
def list_pa_eq_ve(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_EQ_VE).offset(skip).limit(limit).all()

@app.post("/pa-eq-ve/", response_model=schemas.PA_EQ_VE)
def create_pa_eq_ve(item: schemas.PA_EQ_VECreate, db: Session = Depends(get_db)):
    db_item = models.PA_EQ_VE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-eq-ve/{id}", response_model=schemas.PA_EQ_VE)
def update_pa_eq_ve(id: int, item: schemas.PA_EQ_VEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_VE).filter(models.PA_EQ_VE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-eq-ve/{id}")
def delete_pa_eq_ve(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_EQ_VE).filter(models.PA_EQ_VE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_AH
@app.get("/pa-ia-ah/", response_model=List[schemas.PA_IA_AH])
def list_pa_ia_ah(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_AH).offset(skip).limit(limit).all()

@app.post("/pa-ia-ah/", response_model=schemas.PA_IA_AH)
def create_pa_ia_ah(item: schemas.PA_IA_AHCreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_AH(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-ah/{id}", response_model=schemas.PA_IA_AH)
def update_pa_ia_ah(id: int, item: schemas.PA_IA_AHUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_AH).filter(models.PA_IA_AH.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-ah/{id}")
def delete_pa_ia_ah(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_AH).filter(models.PA_IA_AH.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_AM
@app.get("/pa-ia-am/", response_model=List[schemas.PA_IA_AM])
def list_pa_ia_am(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_AM).offset(skip).limit(limit).all()

@app.post("/pa-ia-am/", response_model=schemas.PA_IA_AM)
def create_pa_ia_am(item: schemas.PA_IA_AMCreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_AM(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-am/{id}", response_model=schemas.PA_IA_AM)
def update_pa_ia_am(id: int, item: schemas.PA_IA_AMUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_AM).filter(models.PA_IA_AM.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-am/{id}")
def delete_pa_ia_am(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_AM).filter(models.PA_IA_AM.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_AR
@app.get("/pa-ia-ar/", response_model=List[schemas.PA_IA_AR])
def list_pa_ia_ar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_AR).offset(skip).limit(limit).all()

@app.post("/pa-ia-ar/", response_model=schemas.PA_IA_AR)
def create_pa_ia_ar(item: schemas.PA_IA_ARCreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_AR(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-ar/{id}", response_model=schemas.PA_IA_AR)
def update_pa_ia_ar(id: int, item: schemas.PA_IA_ARUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_AR).filter(models.PA_IA_AR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-ar/{id}")
def delete_pa_ia_ar(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_AR).filter(models.PA_IA_AR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_CA
@app.get("/pa-ia-ca/", response_model=List[schemas.PA_IA_CA])
def list_pa_ia_ca(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_CA).offset(skip).limit(limit).all()

@app.post("/pa-ia-ca/", response_model=schemas.PA_IA_CA)
def create_pa_ia_ca(item: schemas.PA_IA_CACreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_CA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-ca/{id}", response_model=schemas.PA_IA_CA)
def update_pa_ia_ca(id: int, item: schemas.PA_IA_CAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_CA).filter(models.PA_IA_CA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-ca/{id}")
def delete_pa_ia_ca(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_CA).filter(models.PA_IA_CA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_LE
@app.get("/pa-ia-le/", response_model=List[schemas.PA_IA_LE])
def list_pa_ia_le(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_LE).offset(skip).limit(limit).all()

@app.post("/pa-ia-le/", response_model=schemas.PA_IA_LE)
def create_pa_ia_le(item: schemas.PA_IA_LECreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_LE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-le/{id}", response_model=schemas.PA_IA_LE)
def update_pa_ia_le(id: int, item: schemas.PA_IA_LEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_LE).filter(models.PA_IA_LE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-le/{id}")
def delete_pa_ia_le(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_LE).filter(models.PA_IA_LE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_LI
@app.get("/pa-ia-li/", response_model=List[schemas.PA_IA_LI])
def list_pa_ia_li(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_LI).offset(skip).limit(limit).all()

@app.post("/pa-ia-li/", response_model=schemas.PA_IA_LI)
def create_pa_ia_li(item: schemas.PA_IA_LICreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_LI(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-li/{id}", response_model=schemas.PA_IA_LI)
def update_pa_ia_li(id: int, item: schemas.PA_IA_LIUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_LI).filter(models.PA_IA_LI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-li/{id}")
def delete_pa_ia_li(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_LI).filter(models.PA_IA_LI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_RA
@app.get("/pa-ia-ra/", response_model=List[schemas.PA_IA_RA])
def list_pa_ia_ra(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_RA).offset(skip).limit(limit).all()

@app.post("/pa-ia-ra/", response_model=schemas.PA_IA_RA)
def create_pa_ia_ra(item: schemas.PA_IA_RACreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_RA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-ra/{id}", response_model=schemas.PA_IA_RA)
def update_pa_ia_ra(id: int, item: schemas.PA_IA_RAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_RA).filter(models.PA_IA_RA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-ra/{id}")
def delete_pa_ia_ra(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_RA).filter(models.PA_IA_RA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_RI
@app.get("/pa-ia-ri/", response_model=List[schemas.PA_IA_RI])
def list_pa_ia_ri(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_RI).offset(skip).limit(limit).all()

@app.post("/pa-ia-ri/", response_model=schemas.PA_IA_RI)
def create_pa_ia_ri(item: schemas.PA_IA_RICreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_RI(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-ri/{id}", response_model=schemas.PA_IA_RI)
def update_pa_ia_ri(id: int, item: schemas.PA_IA_RIUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_RI).filter(models.PA_IA_RI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-ri/{id}")
def delete_pa_ia_ri(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_RI).filter(models.PA_IA_RI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_SA
@app.get("/pa-ia-sa/", response_model=List[schemas.PA_IA_SA])
def list_pa_ia_sa(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_SA).offset(skip).limit(limit).all()

@app.post("/pa-ia-sa/", response_model=schemas.PA_IA_SA)
def create_pa_ia_sa(item: schemas.PA_IA_SACreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_SA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-sa/{id}", response_model=schemas.PA_IA_SA)
def update_pa_ia_sa(id: int, item: schemas.PA_IA_SAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_SA).filter(models.PA_IA_SA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-sa/{id}")
def delete_pa_ia_sa(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_SA).filter(models.PA_IA_SA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_IA_SI
@app.get("/pa-ia-si/", response_model=List[schemas.PA_IA_SI])
def list_pa_ia_si(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_IA_SI).offset(skip).limit(limit).all()

@app.post("/pa-ia-si/", response_model=schemas.PA_IA_SI)
def create_pa_ia_si(item: schemas.PA_IA_SICreate, db: Session = Depends(get_db)):
    db_item = models.PA_IA_SI(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ia-si/{id}", response_model=schemas.PA_IA_SI)
def update_pa_ia_si(id: int, item: schemas.PA_IA_SIUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_SI).filter(models.PA_IA_SI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ia-si/{id}")
def delete_pa_ia_si(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_IA_SI).filter(models.PA_IA_SI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_AU
@app.get("/pa-pe-au/", response_model=List[schemas.PA_PE_AU])
def list_pa_pe_au(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_AU).offset(skip).limit(limit).all()

@app.post("/pa-pe-au/", response_model=schemas.PA_PE_AU)
def create_pa_pe_au(item: schemas.PA_PE_AUCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_AU(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-au/{id}", response_model=schemas.PA_PE_AU)
def update_pa_pe_au(id: int, item: schemas.PA_PE_AUUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_AU).filter(models.PA_PE_AU.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-au/{id}")
def delete_pa_pe_au(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_AU).filter(models.PA_PE_AU.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_CV
@app.get("/pa-pe-cv/", response_model=List[schemas.PA_PE_CV])
def list_pa_pe_cv(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_CV).offset(skip).limit(limit).all()

@app.post("/pa-pe-cv/", response_model=schemas.PA_PE_CV)
def create_pa_pe_cv(item: schemas.PA_PE_CVCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_CV(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-cv/{id}", response_model=schemas.PA_PE_CV)
def update_pa_pe_cv(id: int, item: schemas.PA_PE_CVUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_CV).filter(models.PA_PE_CV.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-cv/{id}")
def delete_pa_pe_cv(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_CV).filter(models.PA_PE_CV.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_DE
@app.get("/pa-pe-de/", response_model=List[schemas.PA_PE_DE])
def list_pa_pe_de(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_DE).offset(skip).limit(limit).all()

@app.post("/pa-pe-de/", response_model=schemas.PA_PE_DE)
def create_pa_pe_de(item: schemas.PA_PE_DECreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_DE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-de/{id}", response_model=schemas.PA_PE_DE)
def update_pa_pe_de(id: str, item: schemas.PA_PE_DEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_DE).filter(models.PA_PE_DE.abreviacion == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-de/{id}")
def delete_pa_pe_de(id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_DE).filter(models.PA_PE_DE.abreviacion == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_EC
@app.get("/pa-pe-ec/", response_model=List[schemas.PA_PE_EC])
def list_pa_pe_ec(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_EC).offset(skip).limit(limit).all()

@app.post("/pa-pe-ec/", response_model=schemas.PA_PE_EC)
def create_pa_pe_ec(item: schemas.PA_PE_ECCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_EC(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-ec/{id}", response_model=schemas.PA_PE_EC)
def update_pa_pe_ec(id: str, item: schemas.PA_PE_ECUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_EC).filter(models.PA_PE_EC.elemento_de_competencia == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-ec/{id}")
def delete_pa_pe_ec(id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_EC).filter(models.PA_PE_EC.elemento_de_competencia == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_EF
@app.get("/pa-pe-ef/", response_model=List[schemas.PA_PE_EF])
def list_pa_pe_ef(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_EF).offset(skip).limit(limit).all()

@app.post("/pa-pe-ef/", response_model=schemas.PA_PE_EF)
def create_pa_pe_ef(item: schemas.PA_PE_EFCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_EF(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-ef/{id}", response_model=schemas.PA_PE_EF)
def update_pa_pe_ef(id: int, item: schemas.PA_PE_EFUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_EF).filter(models.PA_PE_EF.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-ef/{id}")
def delete_pa_pe_ef(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_EF).filter(models.PA_PE_EF.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_FG
@app.get("/pa-pe-fg/", response_model=List[schemas.PA_PE_FG])
def list_pa_pe_fg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_FG).offset(skip).limit(limit).all()

@app.post("/pa-pe-fg/", response_model=schemas.PA_PE_FG)
def create_pa_pe_fg(item: schemas.PA_PE_FGCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_FG(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-fg/{id}", response_model=schemas.PA_PE_FG)
def update_pa_pe_fg(id: int, item: schemas.PA_PE_FGUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_FG).filter(models.PA_PE_FG.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-fg/{id}")
def delete_pa_pe_fg(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_FG).filter(models.PA_PE_FG.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_IE
@app.get("/pa-pe-ie/", response_model=List[schemas.PA_PE_IE])
def list_pa_pe_ie(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_IE).offset(skip).limit(limit).all()

@app.post("/pa-pe-ie/", response_model=schemas.PA_PE_IE)
def create_pa_pe_ie(item: schemas.PA_PE_IECreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_IE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-ie/{id}", response_model=schemas.PA_PE_IE)
def update_pa_pe_ie(id: int, item: schemas.PA_PE_IEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_IE).filter(models.PA_PE_IE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-ie/{id}")
def delete_pa_pe_ie(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_IE).filter(models.PA_PE_IE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_IS
@app.get("/pa-pe-is/", response_model=List[schemas.PA_PE_IS])
def list_pa_pe_is(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_IS).offset(skip).limit(limit).all()

@app.post("/pa-pe-is/", response_model=schemas.PA_PE_IS)
def create_pa_pe_is(item: schemas.PA_PE_ISCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_IS(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-is/{id}", response_model=schemas.PA_PE_IS)
def update_pa_pe_is(id: int, item: schemas.PA_PE_ISUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_IS).filter(models.PA_PE_IS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-is/{id}")
def delete_pa_pe_is(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_IS).filter(models.PA_PE_IS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_PE
@app.get("/pa-pe-pe/", response_model=List[schemas.PA_PE_PE])
def list_pa_pe_pe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_PE).offset(skip).limit(limit).all()

@app.post("/pa-pe-pe/", response_model=schemas.PA_PE_PE)
def create_pa_pe_pe(item: schemas.PA_PE_PECreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_PE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-pe/{id}", response_model=schemas.PA_PE_PE)
def update_pa_pe_pe(id: int, item: schemas.PA_PE_PEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_PE).filter(models.PA_PE_PE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-pe/{id}")
def delete_pa_pe_pe(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_PE).filter(models.PA_PE_PE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_PL
@app.get("/pa-pe-pl/", response_model=List[schemas.PA_PE_PL])
def list_pa_pe_pl(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_PL).offset(skip).limit(limit).all()

@app.post("/pa-pe-pl/", response_model=schemas.PA_PE_PL)
def create_pa_pe_pl(item: schemas.PA_PE_PLCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_PL(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-pl/{id}", response_model=schemas.PA_PE_PL)
def update_pa_pe_pl(id: int, item: schemas.PA_PE_PLUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_PL).filter(models.PA_PE_PL.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-pl/{id}")
def delete_pa_pe_pl(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_PL).filter(models.PA_PE_PL.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_PO
@app.get("/pa-pe-po/", response_model=List[schemas.PA_PE_PO])
def list_pa_pe_po(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_PO).offset(skip).limit(limit).all()

@app.post("/pa-pe-po/", response_model=schemas.PA_PE_PO)
def create_pa_pe_po(item: schemas.PA_PE_POCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_PO(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-po/{id}", response_model=schemas.PA_PE_PO)
def update_pa_pe_po(id: int, item: schemas.PA_PE_POUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_PO).filter(models.PA_PE_PO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-po/{id}")
def delete_pa_pe_po(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_PO).filter(models.PA_PE_PO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_PR
@app.get("/pa-pe-pr/", response_model=List[schemas.PA_PE_PR])
def list_pa_pe_pr(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_PR).offset(skip).limit(limit).all()

@app.post("/pa-pe-pr/", response_model=schemas.PA_PE_PR)
def create_pa_pe_pr(item: schemas.PA_PE_PRCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_PR(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-pr/{id}", response_model=schemas.PA_PE_PR)
def update_pa_pe_pr(id: int, item: schemas.PA_PE_PRUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_PR).filter(models.PA_PE_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-pr/{id}")
def delete_pa_pe_pr(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_PR).filter(models.PA_PE_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_RQ
@app.get("/pa-pe-rq/", response_model=List[schemas.PA_PE_RQ])
def list_pa_pe_rq(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_RQ).offset(skip).limit(limit).all()

@app.post("/pa-pe-rq/", response_model=schemas.PA_PE_RQ)
def create_pa_pe_rq(item: schemas.PA_PE_RQCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_RQ(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-rq/{id}", response_model=schemas.PA_PE_RQ)
def update_pa_pe_rq(id: int, item: schemas.PA_PE_RQUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_RQ).filter(models.PA_PE_RQ.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-rq/{id}")
def delete_pa_pe_rq(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_RQ).filter(models.PA_PE_RQ.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_SE
@app.get("/pa-pe-se/", response_model=List[schemas.PA_PE_SE])
def list_pa_pe_se(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_SE).offset(skip).limit(limit).all()

@app.post("/pa-pe-se/", response_model=schemas.PA_PE_SE)
def create_pa_pe_se(item: schemas.PA_PE_SECreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_SE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-se/{id}", response_model=schemas.PA_PE_SE)
def update_pa_pe_se(id: int, item: schemas.PA_PE_SEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_SE).filter(models.PA_PE_SE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-se/{id}")
def delete_pa_pe_se(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_SE).filter(models.PA_PE_SE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_SP
@app.get("/pa-pe-sp/", response_model=List[schemas.PA_PE_SP])
def list_pa_pe_sp(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_SP).offset(skip).limit(limit).all()

@app.post("/pa-pe-sp/", response_model=schemas.PA_PE_SP)
def create_pa_pe_sp(item: schemas.PA_PE_SPCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_SP(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-sp/{id}", response_model=schemas.PA_PE_SP)
def update_pa_pe_sp(id: int, item: schemas.PA_PE_SPUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_SP).filter(models.PA_PE_SP.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-sp/{id}")
def delete_pa_pe_sp(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_SP).filter(models.PA_PE_SP.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PE_SU
@app.get("/pa-pe-su/", response_model=List[schemas.PA_PE_SU])
def list_pa_pe_su(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PE_SU).offset(skip).limit(limit).all()

@app.post("/pa-pe-su/", response_model=schemas.PA_PE_SU)
def create_pa_pe_su(item: schemas.PA_PE_SUCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PE_SU(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-pe-su/{id}", response_model=schemas.PA_PE_SU)
def update_pa_pe_su(id: int, item: schemas.PA_PE_SUUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_SU).filter(models.PA_PE_SU.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-pe-su/{id}")
def delete_pa_pe_su(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PE_SU).filter(models.PA_PE_SU.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PS_AD
@app.get("/pa-ps-ad/", response_model=List[schemas.PA_PS_AD])
def list_pa_ps_ad(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PS_AD).offset(skip).limit(limit).all()

@app.post("/pa-ps-ad/", response_model=schemas.PA_PS_AD)
def create_pa_ps_ad(item: schemas.PA_PS_ADCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PS_AD(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ps-ad/{id}", response_model=schemas.PA_PS_AD)
def update_pa_ps_ad(id: int, item: schemas.PA_PS_ADUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_AD).filter(models.PA_PS_AD.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ps-ad/{id}")
def delete_pa_ps_ad(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_AD).filter(models.PA_PS_AD.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PS_CR
@app.get("/pa-ps-cr/", response_model=List[schemas.PA_PS_CR])
def list_pa_ps_cr(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PS_CR).offset(skip).limit(limit).all()

@app.post("/pa-ps-cr/", response_model=schemas.PA_PS_CR)
def create_pa_ps_cr(item: schemas.PA_PS_CRCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PS_CR(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ps-cr/{id}", response_model=schemas.PA_PS_CR)
def update_pa_ps_cr(id: str, item: schemas.PA_PS_CRUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_CR).filter(models.PA_PS_CR.id_criterio == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ps-cr/{id}")
def delete_pa_ps_cr(id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_CR).filter(models.PA_PS_CR.id_criterio == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PS_DE
@app.get("/pa-ps-de/", response_model=List[schemas.PA_PS_DE])
def list_pa_ps_de(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PS_DE).offset(skip).limit(limit).all()

@app.post("/pa-ps-de/", response_model=schemas.PA_PS_DE)
def create_pa_ps_de(item: schemas.PA_PS_DECreate, db: Session = Depends(get_db)):
    db_item = models.PA_PS_DE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ps-de/{id}", response_model=schemas.PA_PS_DE)
def update_pa_ps_de(id: int, item: schemas.PA_PS_DEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_DE).filter(models.PA_PS_DE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ps-de/{id}")
def delete_pa_ps_de(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_DE).filter(models.PA_PS_DE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PS_EV
@app.get("/pa-ps-ev/", response_model=List[schemas.PA_PS_EV])
def list_pa_ps_ev(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PS_EV).offset(skip).limit(limit).all()

@app.post("/pa-ps-ev/", response_model=schemas.PA_PS_EV)
def create_pa_ps_ev(item: schemas.PA_PS_EVCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PS_EV(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ps-ev/{id}", response_model=schemas.PA_PS_EV)
def update_pa_ps_ev(id: int, item: schemas.PA_PS_EVUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_EV).filter(models.PA_PS_EV.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ps-ev/{id}")
def delete_pa_ps_ev(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_EV).filter(models.PA_PS_EV.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PS_OS
@app.get("/pa-ps-os/", response_model=List[schemas.PA_PS_OS])
def list_pa_ps_os(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PS_OS).offset(skip).limit(limit).all()

@app.post("/pa-ps-os/", response_model=schemas.PA_PS_OS)
def create_pa_ps_os(item: schemas.PA_PS_OSCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PS_OS(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ps-os/{id}", response_model=schemas.PA_PS_OS)
def update_pa_ps_os(id: int, item: schemas.PA_PS_OSUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_OS).filter(models.PA_PS_OS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ps-os/{id}")
def delete_pa_ps_os(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_OS).filter(models.PA_PS_OS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PS_PR
@app.get("/pa-ps-pr/", response_model=List[schemas.PA_PS_PR])
def list_pa_ps_pr(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PS_PR).offset(skip).limit(limit).all()

@app.post("/pa-ps-pr/", response_model=schemas.PA_PS_PR)
def create_pa_ps_pr(item: schemas.PA_PS_PRCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PS_PR(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ps-pr/{id}", response_model=schemas.PA_PS_PR)
def update_pa_ps_pr(id: int, item: schemas.PA_PS_PRUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_PR).filter(models.PA_PS_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ps-pr/{id}")
def delete_pa_ps_pr(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_PR).filter(models.PA_PS_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PA_PS_PS
@app.get("/pa-ps-ps/", response_model=List[schemas.PA_PS_PS])
def list_pa_ps_ps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PA_PS_PS).offset(skip).limit(limit).all()

@app.post("/pa-ps-ps/", response_model=schemas.PA_PS_PS)
def create_pa_ps_ps(item: schemas.PA_PS_PSCreate, db: Session = Depends(get_db)):
    db_item = models.PA_PS_PS(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pa-ps-ps/{id}", response_model=schemas.PA_PS_PS)
def update_pa_ps_ps(id: int, item: schemas.PA_PS_PSUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_PS).filter(models.PA_PS_PS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pa-ps-ps/{id}")
def delete_pa_ps_ps(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PA_PS_PS).filter(models.PA_PS_PS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_ES_ES
@app.get("/pc-es-es/", response_model=List[schemas.PC_ES_ES])
def list_pc_es_es(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_ES_ES).offset(skip).limit(limit).all()

@app.post("/pc-es-es/", response_model=schemas.PC_ES_ES)
def create_pc_es_es(item: schemas.PC_ES_ESCreate, db: Session = Depends(get_db)):
    db_item = models.PC_ES_ES(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-es-es/{id}", response_model=schemas.PC_ES_ES)
def update_pc_es_es(id: int, item: schemas.PC_ES_ESUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_ES_ES).filter(models.PC_ES_ES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-es-es/{id}")
def delete_pc_es_es(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_ES_ES).filter(models.PC_ES_ES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_LAB_PATRONES
@app.get("/pc-lab-patrones/", response_model=List[schemas.PC_LAB_PATRONES])
def list_pc_lab_patrones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_LAB_PATRONES).offset(skip).limit(limit).all()

@app.post("/pc-lab-patrones/", response_model=schemas.PC_LAB_PATRONES)
def create_pc_lab_patrones(item: schemas.PC_LAB_PATRONESCreate, db: Session = Depends(get_db)):
    db_item = models.PC_LAB_PATRONES(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-lab-patrones/{id}", response_model=schemas.PC_LAB_PATRONES)
def update_pc_lab_patrones(id: int, item: schemas.PC_LAB_PATRONESUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_LAB_PATRONES).filter(models.PC_LAB_PATRONES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-lab-patrones/{id}")
def delete_pc_lab_patrones(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_LAB_PATRONES).filter(models.PC_LAB_PATRONES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_LAB_SOLUCIONES
@app.get("/pc-lab-soluciones/", response_model=List[schemas.PC_LAB_SOLUCIONES])
def list_pc_lab_soluciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_LAB_SOLUCIONES).offset(skip).limit(limit).all()

@app.post("/pc-lab-soluciones/", response_model=schemas.PC_LAB_SOLUCIONES)
def create_pc_lab_soluciones(item: schemas.PC_LAB_SOLUCIONESCreate, db: Session = Depends(get_db)):
    db_item = models.PC_LAB_SOLUCIONES(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-lab-soluciones/{id}", response_model=schemas.PC_LAB_SOLUCIONES)
def update_pc_lab_soluciones(id: int, item: schemas.PC_LAB_SOLUCIONESUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_LAB_SOLUCIONES).filter(models.PC_LAB_SOLUCIONES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-lab-soluciones/{id}")
def delete_pc_lab_soluciones(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_LAB_SOLUCIONES).filter(models.PC_LAB_SOLUCIONES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_LAB_SOLUCIONES_DET
@app.get("/pc-lab-soluciones-det/", response_model=List[schemas.PC_LAB_SOLUCIONES_DET])
def list_pc_lab_soluciones_det(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_LAB_SOLUCIONES_DET).offset(skip).limit(limit).all()

@app.post("/pc-lab-soluciones-det/", response_model=schemas.PC_LAB_SOLUCIONES_DET)
def create_pc_lab_soluciones_det(item: schemas.PC_LAB_SOLUCIONES_DETCreate, db: Session = Depends(get_db)):
    db_item = models.PC_LAB_SOLUCIONES_DET(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-lab-soluciones-det/{id}", response_model=schemas.PC_LAB_SOLUCIONES_DET)
def update_pc_lab_soluciones_det(id: int, item: schemas.PC_LAB_SOLUCIONES_DETUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_LAB_SOLUCIONES_DET).filter(models.PC_LAB_SOLUCIONES_DET.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-lab-soluciones-det/{id}")
def delete_pc_lab_soluciones_det(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_LAB_SOLUCIONES_DET).filter(models.PC_LAB_SOLUCIONES_DET.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_LAB_VALIDACIONMETODOS
@app.get("/pc-lab-validacionmetodos/", response_model=List[schemas.PC_LAB_VALIDACIONMETODOS])
def list_pc_lab_validacionmetodos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_LAB_VALIDACIONMETODOS).offset(skip).limit(limit).all()

@app.post("/pc-lab-validacionmetodos/", response_model=schemas.PC_LAB_VALIDACIONMETODOS)
def create_pc_lab_validacionmetodos(item: schemas.PC_LAB_VALIDACIONMETODOSCreate, db: Session = Depends(get_db)):
    db_item = models.PC_LAB_VALIDACIONMETODOS(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-lab-validacionmetodos/{id}", response_model=schemas.PC_LAB_VALIDACIONMETODOS)
def update_pc_lab_validacionmetodos(id: int, item: schemas.PC_LAB_VALIDACIONMETODOSUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_LAB_VALIDACIONMETODOS).filter(models.PC_LAB_VALIDACIONMETODOS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-lab-validacionmetodos/{id}")
def delete_pc_lab_validacionmetodos(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_LAB_VALIDACIONMETODOS).filter(models.PC_LAB_VALIDACIONMETODOS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_QR_QU
@app.get("/pc-qr-qu/", response_model=List[schemas.PC_QR_QU])
def list_pc_qr_qu(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_QR_QU).offset(skip).limit(limit).all()

@app.post("/pc-qr-qu/", response_model=schemas.PC_QR_QU)
def create_pc_qr_qu(item: schemas.PC_QR_QUCreate, db: Session = Depends(get_db)):
    db_item = models.PC_QR_QU(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-qr-qu/{id}", response_model=schemas.PC_QR_QU)
def update_pc_qr_qu(id: int, item: schemas.PC_QR_QUUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_QR_QU).filter(models.PC_QR_QU.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-qr-qu/{id}")
def delete_pc_qr_qu(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_QR_QU).filter(models.PC_QR_QU.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_AC
@app.get("/pc-re-ac/", response_model=List[schemas.PC_RE_AC])
def list_pc_re_ac(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_AC).offset(skip).limit(limit).all()

@app.post("/pc-re-ac/", response_model=schemas.PC_RE_AC)
def create_pc_re_ac(item: schemas.PC_RE_ACCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_AC(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-ac/{id}", response_model=schemas.PC_RE_AC)
def update_pc_re_ac(id: int, item: schemas.PC_RE_ACUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_AC).filter(models.PC_RE_AC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-ac/{id}")
def delete_pc_re_ac(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_AC).filter(models.PC_RE_AC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_ANALISIS
@app.get("/pc-re-analisis/", response_model=List[schemas.PC_RE_ANALISIS])
def list_pc_re_analisis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_ANALISIS).offset(skip).limit(limit).all()

@app.post("/pc-re-analisis/", response_model=schemas.PC_RE_ANALISIS)
def create_pc_re_analisis(item: schemas.PC_RE_ANALISISCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_ANALISIS(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-analisis/{id}", response_model=schemas.PC_RE_ANALISIS)
def update_pc_re_analisis(id: int, item: schemas.PC_RE_ANALISISUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_ANALISIS).filter(models.PC_RE_ANALISIS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-analisis/{id}")
def delete_pc_re_analisis(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_ANALISIS).filter(models.PC_RE_ANALISIS.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_CC
@app.get("/pc-re-cc/", response_model=List[schemas.PC_RE_CC])
def list_pc_re_cc(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_CC).offset(skip).limit(limit).all()

@app.post("/pc-re-cc/", response_model=schemas.PC_RE_CC)
def create_pc_re_cc(item: schemas.PC_RE_CCCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_CC(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-cc/{id}", response_model=schemas.PC_RE_CC)
def update_pc_re_cc(id: int, item: schemas.PC_RE_CCUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_CC).filter(models.PC_RE_CC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-cc/{id}")
def delete_pc_re_cc(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_CC).filter(models.PC_RE_CC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_CL
@app.get("/pc-re-cl/", response_model=List[schemas.PC_RE_CL])
def list_pc_re_cl(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_CL).offset(skip).limit(limit).all()

@app.post("/pc-re-cl/", response_model=schemas.PC_RE_CL)
def create_pc_re_cl(item: schemas.PC_RE_CLCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_CL(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-cl/{id}", response_model=schemas.PC_RE_CL)
def update_pc_re_cl(id: int, item: schemas.PC_RE_CLUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_CL).filter(models.PC_RE_CL.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-cl/{id}")
def delete_pc_re_cl(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_CL).filter(models.PC_RE_CL.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_CO
@app.get("/pc-re-co/", response_model=List[schemas.PC_RE_CO])
def list_pc_re_co(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_CO).offset(skip).limit(limit).all()

@app.post("/pc-re-co/", response_model=schemas.PC_RE_CO)
def create_pc_re_co(item: schemas.PC_RE_COCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_CO(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-co/{id}", response_model=schemas.PC_RE_CO)
def update_pc_re_co(id: int, item: schemas.PC_RE_COUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_CO).filter(models.PC_RE_CO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-co/{id}")
def delete_pc_re_co(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_CO).filter(models.PC_RE_CO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_MU
@app.get("/pc-re-mu/", response_model=List[schemas.PC_RE_MU])
def list_pc_re_mu(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_MU).offset(skip).limit(limit).all()

@app.post("/pc-re-mu/", response_model=schemas.PC_RE_MU)
def create_pc_re_mu(item: schemas.PC_RE_MUCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_MU(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-mu/{id}", response_model=schemas.PC_RE_MU)
def update_pc_re_mu(id: int, item: schemas.PC_RE_MUUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_MU).filter(models.PC_RE_MU.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-mu/{id}")
def delete_pc_re_mu(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_MU).filter(models.PC_RE_MU.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_OF
@app.get("/pc-re-of/", response_model=List[schemas.PC_RE_OF])
def list_pc_re_of(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_OF).offset(skip).limit(limit).all()

@app.post("/pc-re-of/", response_model=schemas.PC_RE_OF)
def create_pc_re_of(item: schemas.PC_RE_OFCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_OF(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-of/{id}", response_model=schemas.PC_RE_OF)
def update_pc_re_of(id: int, item: schemas.PC_RE_OFUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_OF).filter(models.PC_RE_OF.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-of/{id}")
def delete_pc_re_of(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_OF).filter(models.PC_RE_OF.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_PI
@app.get("/pc-re-pi/", response_model=List[schemas.PC_RE_PI])
def list_pc_re_pi(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_PI).offset(skip).limit(limit).all()

@app.post("/pc-re-pi/", response_model=schemas.PC_RE_PI)
def create_pc_re_pi(item: schemas.PC_RE_PICreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_PI(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-pi/{id}", response_model=schemas.PC_RE_PI)
def update_pc_re_pi(id: int, item: schemas.PC_RE_PIUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_PI).filter(models.PC_RE_PI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-pi/{id}")
def delete_pc_re_pi(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_PI).filter(models.PC_RE_PI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_PR
@app.get("/pc-re-pr/", response_model=List[schemas.PC_RE_PR])
def list_pc_re_pr(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_PR).offset(skip).limit(limit).all()

@app.post("/pc-re-pr/", response_model=schemas.PC_RE_PR)
def create_pc_re_pr(item: schemas.PC_RE_PRCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_PR(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-pr/{id}", response_model=schemas.PC_RE_PR)
def update_pc_re_pr(id: int, item: schemas.PC_RE_PRUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_PR).filter(models.PC_RE_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-pr/{id}")
def delete_pc_re_pr(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_PR).filter(models.PC_RE_PR.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_SE
@app.get("/pc-re-se/", response_model=List[schemas.PC_RE_SE])
def list_pc_re_se(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_SE).offset(skip).limit(limit).all()

@app.post("/pc-re-se/", response_model=schemas.PC_RE_SE)
def create_pc_re_se(item: schemas.PC_RE_SECreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_SE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-se/{id}", response_model=schemas.PC_RE_SE)
def update_pc_re_se(id: int, item: schemas.PC_RE_SEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_SE).filter(models.PC_RE_SE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-se/{id}")
def delete_pc_re_se(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_SE).filter(models.PC_RE_SE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_SG
@app.get("/pc-re-sg/", response_model=List[schemas.PC_RE_SG])
def list_pc_re_sg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_SG).offset(skip).limit(limit).all()

@app.post("/pc-re-sg/", response_model=schemas.PC_RE_SG)
def create_pc_re_sg(item: schemas.PC_RE_SGCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_SG(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-sg/{id}", response_model=schemas.PC_RE_SG)
def update_pc_re_sg(id: int, item: schemas.PC_RE_SGUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_SG).filter(models.PC_RE_SG.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-sg/{id}")
def delete_pc_re_sg(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_SG).filter(models.PC_RE_SG.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_SH
@app.get("/pc-re-sh/", response_model=List[schemas.PC_RE_SH])
def list_pc_re_sh(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_SH).offset(skip).limit(limit).all()

@app.post("/pc-re-sh/", response_model=schemas.PC_RE_SH)
def create_pc_re_sh(item: schemas.PC_RE_SHCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_SH(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-sh/{id}", response_model=schemas.PC_RE_SH)
def update_pc_re_sh(id: int, item: schemas.PC_RE_SHUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_SH).filter(models.PC_RE_SH.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-sh/{id}")
def delete_pc_re_sh(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_SH).filter(models.PC_RE_SH.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_RE_SO
@app.get("/pc-re-so/", response_model=List[schemas.PC_RE_SO])
def list_pc_re_so(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_RE_SO).offset(skip).limit(limit).all()

@app.post("/pc-re-so/", response_model=schemas.PC_RE_SO)
def create_pc_re_so(item: schemas.PC_RE_SOCreate, db: Session = Depends(get_db)):
    db_item = models.PC_RE_SO(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-re-so/{id}", response_model=schemas.PC_RE_SO)
def update_pc_re_so(id: int, item: schemas.PC_RE_SOUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_SO).filter(models.PC_RE_SO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-re-so/{id}")
def delete_pc_re_so(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_RE_SO).filter(models.PC_RE_SO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PC_TC_TC
@app.get("/pc-tc-tc/", response_model=List[schemas.PC_TC_TC])
def list_pc_tc_tc(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PC_TC_TC).offset(skip).limit(limit).all()

@app.post("/pc-tc-tc/", response_model=schemas.PC_TC_TC)
def create_pc_tc_tc(item: schemas.PC_TC_TCCreate, db: Session = Depends(get_db)):
    db_item = models.PC_TC_TC(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pc-tc-tc/{id}", response_model=schemas.PC_TC_TC)
def update_pc_tc_tc(id: int, item: schemas.PC_TC_TCUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_TC_TC).filter(models.PC_TC_TC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pc-tc-tc/{id}")
def delete_pc_tc_tc(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PC_TC_TC).filter(models.PC_TC_TC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_PL_AC
@app.get("/pe-pl-ac/", response_model=List[schemas.PE_PL_AC])
def list_pe_pl_ac(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_PL_AC).offset(skip).limit(limit).all()

@app.post("/pe-pl-ac/", response_model=schemas.PE_PL_AC)
def create_pe_pl_ac(item: schemas.PE_PL_ACCreate, db: Session = Depends(get_db)):
    db_item = models.PE_PL_AC(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-pl-ac/{id}", response_model=schemas.PE_PL_AC)
def update_pe_pl_ac(id: int, item: schemas.PE_PL_ACUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_AC).filter(models.PE_PL_AC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-pl-ac/{id}")
def delete_pe_pl_ac(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_AC).filter(models.PE_PL_AC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_PL_CO
@app.get("/pe-pl-co/", response_model=List[schemas.PE_PL_CO])
def list_pe_pl_co(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_PL_CO).offset(skip).limit(limit).all()

@app.post("/pe-pl-co/", response_model=schemas.PE_PL_CO)
def create_pe_pl_co(item: schemas.PE_PL_COCreate, db: Session = Depends(get_db)):
    db_item = models.PE_PL_CO(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-pl-co/{id}", response_model=schemas.PE_PL_CO)
def update_pe_pl_co(id: int, item: schemas.PE_PL_COUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_CO).filter(models.PE_PL_CO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-pl-co/{id}")
def delete_pe_pl_co(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_CO).filter(models.PE_PL_CO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_PL_ES
@app.get("/pe-pl-es/", response_model=List[schemas.PE_PL_ES])
def list_pe_pl_es(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_PL_ES).offset(skip).limit(limit).all()

@app.post("/pe-pl-es/", response_model=schemas.PE_PL_ES)
def create_pe_pl_es(item: schemas.PE_PL_ESCreate, db: Session = Depends(get_db)):
    db_item = models.PE_PL_ES(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-pl-es/{id}", response_model=schemas.PE_PL_ES)
def update_pe_pl_es(id: int, item: schemas.PE_PL_ESUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_ES).filter(models.PE_PL_ES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-pl-es/{id}")
def delete_pe_pl_es(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_ES).filter(models.PE_PL_ES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_PL_OB
@app.get("/pe-pl-ob/", response_model=List[schemas.PE_PL_OB])
def list_pe_pl_ob(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_PL_OB).offset(skip).limit(limit).all()

@app.post("/pe-pl-ob/", response_model=schemas.PE_PL_OB)
def create_pe_pl_ob(item: schemas.PE_PL_OBCreate, db: Session = Depends(get_db)):
    db_item = models.PE_PL_OB(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-pl-ob/{id}", response_model=schemas.PE_PL_OB)
def update_pe_pl_ob(id: int, item: schemas.PE_PL_OBUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_OB).filter(models.PE_PL_OB.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-pl-ob/{id}")
def delete_pe_pl_ob(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_OB).filter(models.PE_PL_OB.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_PL_PC
@app.get("/pe-pl-pc/", response_model=List[schemas.PE_PL_PC])
def list_pe_pl_pc(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_PL_PC).offset(skip).limit(limit).all()

@app.post("/pe-pl-pc/", response_model=schemas.PE_PL_PC)
def create_pe_pl_pc(item: schemas.PE_PL_PCCreate, db: Session = Depends(get_db)):
    db_item = models.PE_PL_PC(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-pl-pc/{id}", response_model=schemas.PE_PL_PC)
def update_pe_pl_pc(id: int, item: schemas.PE_PL_PCUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_PC).filter(models.PE_PL_PC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-pl-pc/{id}")
def delete_pe_pl_pc(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_PC).filter(models.PE_PL_PC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_PL_PI
@app.get("/pe-pl-pi/", response_model=List[schemas.PE_PL_PI])
def list_pe_pl_pi(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_PL_PI).offset(skip).limit(limit).all()

@app.post("/pe-pl-pi/", response_model=schemas.PE_PL_PI)
def create_pe_pl_pi(item: schemas.PE_PL_PICreate, db: Session = Depends(get_db)):
    db_item = models.PE_PL_PI(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-pl-pi/{id}", response_model=schemas.PE_PL_PI)
def update_pe_pl_pi(id: int, item: schemas.PE_PL_PIUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_PI).filter(models.PE_PL_PI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-pl-pi/{id}")
def delete_pe_pl_pi(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_PI).filter(models.PE_PL_PI.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_PL_PL
@app.get("/pe-pl-pl/", response_model=List[schemas.PE_PL_PL])
def list_pe_pl_pl(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_PL_PL).offset(skip).limit(limit).all()

@app.post("/pe-pl-pl/", response_model=schemas.PE_PL_PL)
def create_pe_pl_pl(item: schemas.PE_PL_PLCreate, db: Session = Depends(get_db)):
    db_item = models.PE_PL_PL(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-pl-pl/{id}", response_model=schemas.PE_PL_PL)
def update_pe_pl_pl(id: int, item: schemas.PE_PL_PLUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_PL).filter(models.PE_PL_PL.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-pl-pl/{id}")
def delete_pe_pl_pl(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_PL).filter(models.PE_PL_PL.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_PL_RO
@app.get("/pe-pl-ro/", response_model=List[schemas.PE_PL_RO])
def list_pe_pl_ro(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_PL_RO).offset(skip).limit(limit).all()

@app.post("/pe-pl-ro/", response_model=schemas.PE_PL_RO)
def create_pe_pl_ro(item: schemas.PE_PL_ROCreate, db: Session = Depends(get_db)):
    db_item = models.PE_PL_RO(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-pl-ro/{id}", response_model=schemas.PE_PL_RO)
def update_pe_pl_ro(id: int, item: schemas.PE_PL_ROUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_RO).filter(models.PE_PL_RO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-pl-ro/{id}")
def delete_pe_pl_ro(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_PL_RO).filter(models.PE_PL_RO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_AC
@app.get("/pe-se-ac/", response_model=List[schemas.PE_SE_AC])
def list_pe_se_ac(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_AC).offset(skip).limit(limit).all()

@app.post("/pe-se-ac/", response_model=schemas.PE_SE_AC)
def create_pe_se_ac(item: schemas.PE_SE_ACCreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_AC(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-ac/{id}", response_model=schemas.PE_SE_AC)
def update_pe_se_ac(id: int, item: schemas.PE_SE_ACUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_AC).filter(models.PE_SE_AC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-ac/{id}")
def delete_pe_se_ac(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_AC).filter(models.PE_SE_AC.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_CA
@app.get("/pe-se-ca/", response_model=List[schemas.PE_SE_CA])
def list_pe_se_ca(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_CA).offset(skip).limit(limit).all()

@app.post("/pe-se-ca/", response_model=schemas.PE_SE_CA)
def create_pe_se_ca(item: schemas.PE_SE_CACreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_CA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-ca/{id}", response_model=schemas.PE_SE_CA)
def update_pe_se_ca(id: int, item: schemas.PE_SE_CAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_CA).filter(models.PE_SE_CA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-ca/{id}")
def delete_pe_se_ca(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_CA).filter(models.PE_SE_CA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_CO
@app.get("/pe-se-co/", response_model=List[schemas.PE_SE_CO])
def list_pe_se_co(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_CO).offset(skip).limit(limit).all()

@app.post("/pe-se-co/", response_model=schemas.PE_SE_CO)
def create_pe_se_co(item: schemas.PE_SE_COCreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_CO(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-co/{id}", response_model=schemas.PE_SE_CO)
def update_pe_se_co(id: int, item: schemas.PE_SE_COUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_CO).filter(models.PE_SE_CO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-co/{id}")
def delete_pe_se_co(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_CO).filter(models.PE_SE_CO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_EE
@app.get("/pe-se-ee/", response_model=List[schemas.PE_SE_EE])
def list_pe_se_ee(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_EE).offset(skip).limit(limit).all()

@app.post("/pe-se-ee/", response_model=schemas.PE_SE_EE)
def create_pe_se_ee(item: schemas.PE_SE_EECreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_EE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-ee/{id}", response_model=schemas.PE_SE_EE)
def update_pe_se_ee(id: str, item: schemas.PE_SE_EEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_EE).filter(models.PE_SE_EE.entradas == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-ee/{id}")
def delete_pe_se_ee(id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_EE).filter(models.PE_SE_EE.entradas == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_EN
@app.get("/pe-se-en/", response_model=List[schemas.PE_SE_EN])
def list_pe_se_en(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_EN).offset(skip).limit(limit).all()

@app.post("/pe-se-en/", response_model=schemas.PE_SE_EN)
def create_pe_se_en(item: schemas.PE_SE_ENCreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_EN(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-en/{id}", response_model=schemas.PE_SE_EN)
def update_pe_se_en(id: int, item: schemas.PE_SE_ENUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_EN).filter(models.PE_SE_EN.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-en/{id}")
def delete_pe_se_en(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_EN).filter(models.PE_SE_EN.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_MA
@app.get("/pe-se-ma/", response_model=List[schemas.PE_SE_MA])
def list_pe_se_ma(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_MA).offset(skip).limit(limit).all()

@app.post("/pe-se-ma/", response_model=schemas.PE_SE_MA)
def create_pe_se_ma(item: schemas.PE_SE_MACreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_MA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-ma/{id}", response_model=schemas.PE_SE_MA)
def update_pe_se_ma(id: int, item: schemas.PE_SE_MAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_MA).filter(models.PE_SE_MA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-ma/{id}")
def delete_pe_se_ma(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_MA).filter(models.PE_SE_MA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_ME
@app.get("/pe-se-me/", response_model=List[schemas.PE_SE_ME])
def list_pe_se_me(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_ME).offset(skip).limit(limit).all()

@app.post("/pe-se-me/", response_model=schemas.PE_SE_ME)
def create_pe_se_me(item: schemas.PE_SE_MECreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_ME(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-me/{id}", response_model=schemas.PE_SE_ME)
def update_pe_se_me(id: int, item: schemas.PE_SE_MEUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_ME).filter(models.PE_SE_ME.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-me/{id}")
def delete_pe_se_me(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_ME).filter(models.PE_SE_ME.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_RE
@app.get("/pe-se-re/", response_model=List[schemas.PE_SE_RE])
def list_pe_se_re(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_RE).offset(skip).limit(limit).all()

@app.post("/pe-se-re/", response_model=schemas.PE_SE_RE)
def create_pe_se_re(item: schemas.PE_SE_RECreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_RE(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-re/{id}", response_model=schemas.PE_SE_RE)
def update_pe_se_re(id: int, item: schemas.PE_SE_REUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_RE).filter(models.PE_SE_RE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-re/{id}")
def delete_pe_se_re(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_RE).filter(models.PE_SE_RE.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_SA
@app.get("/pe-se-sa/", response_model=List[schemas.PE_SE_SA])
def list_pe_se_sa(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_SA).offset(skip).limit(limit).all()

@app.post("/pe-se-sa/", response_model=schemas.PE_SE_SA)
def create_pe_se_sa(item: schemas.PE_SE_SACreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_SA(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-sa/{id}", response_model=schemas.PE_SE_SA)
def update_pe_se_sa(id: int, item: schemas.PE_SE_SAUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_SA).filter(models.PE_SE_SA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-sa/{id}")
def delete_pe_se_sa(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_SA).filter(models.PE_SE_SA.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para PE_SE_SS
@app.get("/pe-se-ss/", response_model=List[schemas.PE_SE_SS])
def list_pe_se_ss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.PE_SE_SS).offset(skip).limit(limit).all()

@app.post("/pe-se-ss/", response_model=schemas.PE_SE_SS)
def create_pe_se_ss(item: schemas.PE_SE_SSCreate, db: Session = Depends(get_db)):
    db_item = models.PE_SE_SS(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/pe-se-ss/{id}", response_model=schemas.PE_SE_SS)
def update_pe_se_ss(id: str, item: schemas.PE_SE_SSUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_SS).filter(models.PE_SE_SS.salidas == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/pe-se-ss/{id}")
def delete_pe_se_ss(id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.PE_SE_SS).filter(models.PE_SE_SS.salidas == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para SYS_FACTORESK
@app.get("/sys-factoresk/", response_model=List[schemas.SYS_FACTORESK])
def list_sys_factoresk(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.SYS_FACTORESK).offset(skip).limit(limit).all()

@app.post("/sys-factoresk/", response_model=schemas.SYS_FACTORESK)
def create_sys_factoresk(item: schemas.SYS_FACTORESKCreate, db: Session = Depends(get_db)):
    db_item = models.SYS_FACTORESK(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/sys-factoresk/{id}", response_model=schemas.SYS_FACTORESK)
def update_sys_factoresk(id: int, item: schemas.SYS_FACTORESKUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.SYS_FACTORESK).filter(models.SYS_FACTORESK.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/sys-factoresk/{id}")
def delete_sys_factoresk(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.SYS_FACTORESK).filter(models.SYS_FACTORESK.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para TBL_LUGARES
@app.get("/tbl-lugares/", response_model=List[schemas.TBL_LUGARES])
def list_tbl_lugares(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.TBL_LUGARES).offset(skip).limit(limit).all()

@app.post("/tbl-lugares/", response_model=schemas.TBL_LUGARES)
def create_tbl_lugares(item: schemas.TBL_LUGARESCreate, db: Session = Depends(get_db)):
    db_item = models.TBL_LUGARES(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/tbl-lugares/{id}", response_model=schemas.TBL_LUGARES)
def update_tbl_lugares(id: int, item: schemas.TBL_LUGARESUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.TBL_LUGARES).filter(models.TBL_LUGARES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/tbl-lugares/{id}")
def delete_tbl_lugares(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.TBL_LUGARES).filter(models.TBL_LUGARES.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}


# API para TBL_POSICIONES_HORNO
@app.get("/tbl-posiciones-horno/", response_model=List[schemas.TBL_POSICIONES_HORNO])
def list_tbl_posiciones_horno(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.TBL_POSICIONES_HORNO).offset(skip).limit(limit).all()

@app.post("/tbl-posiciones-horno/", response_model=schemas.TBL_POSICIONES_HORNO)
def create_tbl_posiciones_horno(item: schemas.TBL_POSICIONES_HORNOCreate, db: Session = Depends(get_db)):
    db_item = models.TBL_POSICIONES_HORNO(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/tbl-posiciones-horno/{id}", response_model=schemas.TBL_POSICIONES_HORNO)
def update_tbl_posiciones_horno(id: int, item: schemas.TBL_POSICIONES_HORNOUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.TBL_POSICIONES_HORNO).filter(models.TBL_POSICIONES_HORNO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/tbl-posiciones-horno/{id}")
def delete_tbl_posiciones_horno(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.TBL_POSICIONES_HORNO).filter(models.TBL_POSICIONES_HORNO.id == id).first()
    if not db_item: raise HTTPException(404, detail="No encontrado")
    db.delete(db_item)
    db.commit()
    return {"status": "eliminado"}
