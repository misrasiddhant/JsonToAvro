# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:12:56 2018

@author: Siddhant
"""

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


schemafile=open("D:/Projects/JsonToAvro/MOCK_DATA.avsc","rb").read()


schema = avro.schema.Parse(schemafile)
writer = DataFileWriter(open("D:/Projects/JsonToAvro/MOCK_DATA.avro","wb"), DatumWriter(),schema)

with open("D:/Projects/JsonToAvro/MOCK_DATA.json") as datafile:
    for d in datafile.readlines():
        writer.append(d)

writer.close()
        