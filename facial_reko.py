import boto3
from botocore.exceptions import ClientError

def obtener_bytes_imagen(ruta_imagen):
    with open(ruta_imagen,'rb')as imagen:
        return imagen.read()


def comparar_rostros(ruta_imagen1, ruta_imagen2):
    bytes_1 = obtener_bytes_imagen(ruta_imagen1)
    bytes_2 = obtener_bytes_imagen(ruta_imagen2)

    cliente = boto3.client('rekognition')   


    try:
        respuesta = cliente.compare_faces(SourceImage = {'Bytes': bytes_1},
        TargetImage = {'Bytes': bytes_2}, SimilarityThreshold = 60,QualityFilter = 'AUTO')
        #Quality Filter = NONE|AUTO|LOW|MEDIUM|HIGH

        if respuesta and respuesta['ResponseMetadata']["HTTPStatusCode"] == 200:
            #No Coincide
            for i in respuesta["UnmatchedFaces"]:
                print(i + ' \n')


        #FaceMatches(Coincide)
        for i in respuesta["FaceMatches"]:
            print("Similarity: " + str(i["Similarity"]))



    except ClientError as error:
        print("Ocurrió un error al llamar a la API de Rekognition: " + str(error))


if __name__ == "__main__":
    ruta_imagen1 = r"C:\\Users\\RafaelCheco\Desktop\\pic1.jpg" #Colocar con doble \\ para evitar problemas de lectura
    ruta_imagen2 = r"C:\\Users\\RafaelCheco\Desktop\\pic2.jpg"

    comparar_rostros(ruta_imagen1, ruta_imagen2)
     
     
     
 











  
