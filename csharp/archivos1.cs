using System.IO;
using System;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamWriter flujoEscritura = File.CreateText("archivoCriminal.txt");

            flujoEscritura.WriteLine("Esta es la primera linea");
            flujoEscritura.WriteLine("Esta es la segunda linea");
            flujoEscritura.Close();

            //Creamos el objeto para trabajar con el archivo. Lo hacemos en modo lectura
            FileStream archivo = new FileStream("archivoCriminal.txt", FileMode.Open, FileAccess.Read);

            //Creamos un StreamReader para leer el archivo
            StreamReader flujoLectura = new StreamReader(archivo);

            //Creamos una variable para almacenar las lineas que vayamos leyendo del archivo
            string linea = "";
            int num_lineas = 0;

            //
            while((linea = flujoLectura.ReadLine()) != null){
                num_lineas++;
            }

            flujoLectura.Close();

            Console.WriteLine("El archivo tiene {0} lineas", num_lineas);

        }
    }
}
