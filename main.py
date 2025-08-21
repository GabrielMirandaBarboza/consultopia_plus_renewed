import uvicorn
import json
from config import app,verificar_codigo
from prompts import prepareDataDescricao,prepareDataInovacao,prepareDataBarreira,prepareDataMetodologia,prepareDataComplementar
from fastapi import HTTPException, Depends
from baseModel import Relacao, InputDataStr
from fastapi.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST


@app.get("/")
def get_root():
    return {"message":"Hello World"}

@app.post('/evaluateDescricao')
def evaluateDescricao(relacao : Relacao, dep=Depends(verificar_codigo)):

    data = prepareDataDescricao(relacao)    
    
    return data

@app.post('/evaluateInovacao')
def evaluateInovacao(relacao : Relacao, dep=Depends(verificar_codigo)):

    data = prepareDataInovacao(relacao)    

    return data

@app.post('/evaluateBarreira')
def evaluateBarreira(relacao : Relacao, dep=Depends(verificar_codigo)):

    data = prepareDataBarreira(relacao)    
    
    return data

@app.post('/evaluateMetodologia')
def evaluateMetodologia(relacao : Relacao, dep=Depends(verificar_codigo)):

    data = prepareDataMetodologia(relacao)    
    
    return data

@app.post('/evaluateMetodologia')
def evaluateComplementar(relacao : Relacao, dep=Depends(verificar_codigo)):

    data = prepareDataComplementar(relacao)    
    
    return data

@app.post("/evaluate")
def evaluateall(relacao:InputDataStr, dep=Depends(verificar_codigo)):

    descricao = prepareDataDescricao(relacao.descricao)
    inovacao = prepareDataInovacao(relacao.elemento_tecnologico)
    barreira = prepareDataBarreira(relacao.desafio)
    metodologia = prepareDataMetodologia(relacao.metodologia)
    complementar = prepareDataComplementar(relacao.complemento)

    return {
        "descricao":descricao.feedback,
        "elemento_tecnologico":inovacao.feedback,
        "desafio":barreira.feedback,
        "metodologia":metodologia.feedback,
        "complementar":complementar.feedback,
        "probability":"0",
        "class":"1",
        "message":"success"
    }
    



@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)







if __name__ == "__main__":
    config = uvicorn.Config("main:app",host="0.0.0.0",port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()