## Qué es esto?

Un mod para el **World Editor** en español que corrige la traducción del editor, arregla casi completamente la UI del mismo y traduce los detonadores.

## Archivos

### WorldEditStrings.txt

El archivo de cadenas principal del editor, prácticamente utilizado en cualquier faceta del editor.

### WorldEditGameStrings.txt

Cadenas compartidas con el juego.

### WorldEditLayout.txt

Contiene muchos de los esquemas de interfaz utilizados por el editor.

### TriggerStrings.txt

Contiene todas las cadenas necesarias para formar el esqueleto de una función, las cadenas de valores se encuentran definidas en `WorldEditStrings.txt` y las cadenas de error de compilación en `WorldEditGameStrings.txt`.

### TriggerData.txt

Utilizado para realizar cambios y mejorías en el Editor de detonadores. Con este archivo se puede: crear nuevas funciones, modificar valores predeterminados en funciones, agregar variables (siempre y cuando exista un análogo en jass), reordenar listas de funciones, etc.

## Modalidades

### General - "No me toques (tanto) los detonadores!"

* `WorldEditStrings.txt`
* `WorldEditGameStrings.txt`
* `WorldEditLayout.txt`

Instalar solo estos 3 archivos arregla la mayoría de los problemas y mala IU resultado de la traducción con la que viene el editor, conteniendo bastantes cambios sobre su uso; con el eje general de categorizar donde sea posible. También contiene nuevos tips de ayuda y valores de detonadores con una mejor traducción y uso.

### +Detonadores

* `TriggerStrings.txt` - Instalar este archivo traduce completamente los detonadores y por ende implica un cambio de uso importante, si sabes bastante bien qué hace cada detonador y algo de inglés puede que te vaya mejor ignorandolo. Además contiene nuevos tips de ayuda y cambios en estos.
* `TriggerData.txt` - Este archivo cumple la función de mejorar el uso de los detonadores a través del cambio de valores por defecto en funciones, cambios en el orden de listas y agregado de variables predeterminadas.

## Cómo usar

### Editor normal

Copiar y pegar la carpeta `UI` con los archivos elegidos en el directorio del juego y listo. Una vez se abre el editor debería cargar los archivos.

### Editor custom

Un editor custom puede ocasionar errores si este espera que no se modifique el editor posteriomente con archivos locales como lo hace este mod. Por ende la instalación para uno depende de cómo este hecho el editor.
