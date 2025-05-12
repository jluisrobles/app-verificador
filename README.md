# Validador de Correos Empresariales

Este proyecto es una herramienta sencilla para validar direcciones de correo electrónico empresariales. Se utiliza un archivo Excel con una columna que contiene correos electrónicos, y el script valida si cada correo tiene un formato adecuado y si el dominio del correo electrónico tiene un servidor de correo (MX) válido.

## Requisitos

- **Columna 'E-mail'**: El archivo Excel que subas debe contener una columna con el nombre **exacto** de "E-mail". El script utilizará esta columna para realizar las validaciones de los correos electrónicos. Si el archivo no contiene esta columna, el proceso no podrá comenzar.
  
- **Formato del archivo**: El archivo debe ser de tipo `.xlsx`.

## Descripción del Código

Este script realiza los siguientes pasos:

1. **Subir archivo Excel**: El usuario sube un archivo Excel (.xlsx) que contiene una columna llamada 'E-mail' con los correos a validar.
   
2. **Validación de formato**: El código verifica que los correos tengan un formato adecuado utilizando expresiones regulares.
   
3. **Verificación de dominio**: El script revisa si el dominio del correo electrónico tiene un servidor de correo válido (registro MX). Si el dominio es uno de los correos públicos comunes (por ejemplo, `gmail.com`, `hotmail.com`, etc.), se considera no válido para fines empresariales.

4. **Resultado**: El código genera un archivo Excel con tres columnas adicionales:
   - `formato_valido`: Indica si el correo tiene un formato válido.
   - `dominio_valido`: Indica si el dominio del correo tiene un registro MX.
   - `correo_valido`: Indica si el correo es válido, es decir, si tiene un formato válido y un dominio con un registro MX.

5. **Descarga del archivo**: El usuario puede descargar el archivo Excel con los resultados de la validación.

## Uso

1. Ejecuta el script en un entorno que soporte Streamlit.
2. Sube el archivo Excel con la columna 'E-mail'.
3. El código validará cada dirección de correo electrónico en el archivo y te mostrará los resultados.
4. Descarga el archivo resultante con las validaciones realizadas.

## Ejemplo de Archivo Excel

Asegúrate de que tu archivo Excel tenga una columna llamada **E-mail** con
# 📧 Validador de Correos Empresariales

Esta aplicación desarrollada con **Streamlit** permite verificar listas de correos electrónicos empresariales cargadas desde un archivo Excel. Evalúa la validez de cada dirección tanto por su **formato** como por la existencia de **registros MX del dominio**, y genera un gráfico visual con los resultados.

---

## 🚀 ¿Qué hace esta app?

- Valida que los correos tengan el **formato correcto** (`usuario@dominio.com`)
- Verifica si el **dominio del correo tiene registros MX** (correo empresarial real)
- Clasifica los correos como:
  - ✅ Válidos
  - ❌ Inválidos por formato
  - ⚠️ Inválidos por dominio
  - 🟥 Vacíos
- Genera un **gráfico interactivo** con los resultados
- Permite descargar un archivo Excel con la validación de cada correo

---

## 📥 Requisitos del archivo Excel

El archivo que subas **debe tener una columna llamada exactamente**:


