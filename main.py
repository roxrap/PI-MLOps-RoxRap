import pandas as pd
import os

# Funciones para Endpoints / ML

def PlayTimeGenre(genero: str):  #Devuelve año con mas horas jugadas para un género
    result_df = pd.read_csv('PlayTimeGenre.csv')
    filtered_df = result_df[result_df['genres'] == genero]
    grouped_df = filtered_df.groupby('year')['hours_game'].sum()
    max_hours_year = grouped_df.idxmax()
    response_data = {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero, max_hours_year)}
    return response_data

def UserForGenre(genero:str):    #Devuelve el usuario con más hs jugadas para un género y lista hs x año
    consulta2 = pd.read_csv('UserForGenre.csv')
    genre_data = consulta2[consulta2['genres'] == genero]
    top_user = genre_data.loc[genre_data['hours_game'].idxmax()]['user_id']
    hours_by_year = genre_data.groupby('year')['hours_game'].sum().reset_index()
    hours_by_year = hours_by_year.rename(columns={'year': 'Año', 'hours_game': 'Horas'})
    hours_list = hours_by_year.to_dict(orient='records')
    result = {
        "Usuario con más horas jugadas para Género {}".format(genero): top_user,
        "Horas jugadas": hours_list
    }
    return result

def UsersRecommend(year: int):  #Top 3 de juegos + recomendados en un año (reviews.recommend=True y comentarios positivos/neutrales)
    df = pd.read_csv('UsersRecommend.csv')
    result_df = df[df['fecha'] == year]
    response_data = [{"Puesto 1": result_df.iloc[0]['app_name']},
                     {"Puesto 2": result_df.iloc[1]['app_name']},
                     {"Puesto 3": result_df.iloc[2]['app_name']}]
    return response_data

def UsersNotRecommend(year: int): #Top 3 de juegos - recomendados en un año (reviews.recommend = False y comentarios negativos)
    df = pd.read_csv('UsersNotRecommend.csv')
    result_df = df[df['fecha'] == year]
    response_data = [{"Puesto 1": result_df.iloc[0]['app_name']},
                    {"Puesto 2": result_df.iloc[1]['app_name']},
                    {"Puesto 3": result_df.iloc[2]['app_name']}]
    return response_data

def sentiment_analysis(empresa_desarrolladora: str): #Lista con la cantidad de reseñas con análisis de sentimiento
    df = pd.read_csv('sentiment_analysis.csv')
    result_df = df[df['developer'] == empresa_desarrolladora]
    response_data = result_df.set_index('developer').to_dict(orient='index')
    return response_data

def recomendacion_usuario(item_id): #Devuelve lista con 5 juegos recomendados para un usuario
    df = pd.read_csv('recomienda_item_item.csv')
    result_df = df[df['item_id'] == item_id]
    response_data = result_df['Recomendaciones']
    return response_data

# FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import traceback  
from typing import List, Dict

app = FastAPI()  #instancia de la aplicación FastAPI

@app.get("/")
async def root():
    return {"Mensaje": "Proyecto Individual N° 1 - Roxana Rapali"}

@app.get("/PlayTimeGenre/{genero}", tags=['Año con mas hs jugadas para un género'])
async def endpoint_1_Ingrese_un_género(genero: str):
    try:
        if not genero or not genero.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'genero' no puede ser nulo o estar vacío.")

        result = PlayTimeGenre(genero)

        if not result:
            raise HTTPException(status_code=404, detail=f"No se encontró información para el género '{genero}'.")

        return result

    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo PlayTimeGenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/UserForGenre/{genero}", tags=['El usuario con más hs jugadas para un género'])
async def endpoint_2_Ingrese_un_género(genero: str):
    try:
        if not genero or not genero.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'genero' no puede ser nulo o estar vacío.")

        result = UserForGenre(genero)

        if not result:
            raise HTTPException(status_code=404, detail=f"No se encontró información para el género '{genero}'.")

        return result

    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo UserForGenre.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/UsersRecommend/{year}", tags=['Top 3 de juegos + recomendados en un año'])
async def endpoint_3_Ingrese_un_año(year: str):
    try:
        year = int(year)

        if not (2000 <= year <= 2100):
            error_message = f"El año debe estar en el rango entre 2000 y 2100 {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})

        result = UsersRecommend(year)

        if result:
            return result
        else:
            error_message = "No se encontraron recomendaciones para el año {year} {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})

    except FileNotFoundError as e:
        error_message = f"Error al cargar el archivo UsersRecommend.csv: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})

    except Exception as e:
        error_message = f"Error interno del servidor: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})


@app.get("/UsersNotRecommend/{year}", tags=['Top 3 de juego - recomendados en un año'])
async def endpoint_4_Ingrese_un_año(year: str):
    try:
        year = int(year)

        if not (2000 <= year <= 2100):
            error_message = f"El año debe estar en el rango entre 2000 y 2100 {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})

        result = UsersNotRecommend(year)

        if result:
            return result
        else:
            error_message = "No se encontraron recomendaciones para el año {year} {str(e)}"
            return JSONResponse(status_code=500, content={"error": error_message})

    except FileNotFoundError as e:
        error_message = f"Error al cargar el archivo UsersNotRecommend.csv: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})

    except Exception as e:
        error_message = f"Error interno del servidor: {str(e)}"
        return JSONResponse(status_code=500, content={"error": error_message})


@app.get("/sentiment_analysis/{empresa_desarrolladora}", tags=['Análisis de sentimiento'])
async def enpoint_5_Ingrese_un_desarrollador(empresa_desarrolladora: str):
    try:
        result = sentiment_analysis(empresa_desarrolladora)
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar el archivo sentiment_analysis.csv: {str(e)}")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/recomendacion_usuario/{item_id}", tags=['Recomendacion 5 juegos similares'])
async def MML_Ingrese_un_ITEM_ID(item_id: int):
    try:
        item_id = int(item_id) 
        resultado= recomendacion_usuario(item_id)
        return resultado
    except Exception as e:
        return {"error":str(e)}
