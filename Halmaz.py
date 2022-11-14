'''
Halmaz (set):
- rendezetlen (elemeknek nincs indexe)
- egy elem csak egyszer szerepelhet
- többféle típust tárolhat egyszerre is
- a halmaz eleme maga nem változtatható meg
'''
    
# halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}
    
# üres halmaz létrehozása
# ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

# bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True]) 

print(ebed) 
  


# Halmaz módosítása

# egy elem hozzáadása
reggeli.add('lekvár')
print(reggeli)

# egy nem meghatározott elem eltávolítása
reggeli.pop()
    
# egy bizonyos elem eltávolítása
# ha nincs ilyen elem, akkor hibát eredményez
# reggeli.remove('sajt')

# egy bizonyos elem eltávolítása
# ha nincs ilyen elem, nem eredményez hibát
reggeli.discard('sajt')
    
  

# Halmazműveletek


reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}

# metszet
print(reggeli & ebed)
# unio
print(reggeli | ebed)
# különbség
print(reggeli - ebed)
# csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)
    
  

