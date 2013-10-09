import sys
import os
import zlib

COMPRESSIONLEVEL = 6

def NCDkernel(doc1,doc2,doc1_compressed_size = -1, doc2_compressed_size = -1):

  if doc1_compressed_size == -1:
    doc1_compressed_size = sys.getsizeof(zlib.compress(doc1, COMPRESSIONLEVEL),-1)
    if doc1_compressed_size == -1:
      sys.exit('document_error')
      
  if doc2_compressed_size == -1:
    doc2_compressed_size = sys.getsizeof(zlib.compress(doc2, COMPRESSIONLEVEL),-1)
    if doc2_compressed_size == -1:
      sys.exit('document_error')  
  
  bothdocs_compressed_size = sys.getsizeof(zlib.compress(''.join([doc1,doc2]), COMPRESSIONLEVEL),-1)
  if bothdocs_compressed_size == -1:
    sys.exit('document_error')
    
  NCD = 1.0*(bothdocs_compressed_size - min(doc1_compressed_size, doc2_compressed_size))/max(doc1_compressed_size, doc2_compressed_size)
  
  #print doc1_compressed_size
  #print doc2_compressed_size
  #print bothdocs_compressed_size
  
  
  return NCD
