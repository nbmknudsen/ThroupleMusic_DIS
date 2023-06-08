from SpotifyProject import db_cursor, conn
from SpotifyProject.models import Artist, Album, Song, Has, MustHave, BelongsTo


# INSERT QUERIES
def insert_artist(artist: Artist):
    sql = """
    INSERT INTO Artist(art_ID, art_name)
    VALUES (%s, %s)
    """
    db_cursor.execute(sql, (artist.id, artist.name))
    conn.commit()


def insert_album(album: Album):
    sql = """
    INSERT INTO Album(alb_ID, alb_name, alb_duration)
    VALUES (%s, %s, %d)
    """
    db_cursor.execute(sql, (album.id, album.name, album.duration))
    conn.commit()


def insert_song(song: Song):
    sql = """
    INSERT INTO Song(song_ID, song_name, track_num, song_duration, release_date)
    VALUES (%s, %s, %d, %d, '%s')
    """
    db_cursor.execute(sql, (
        song.id, 
        song.name, 
        song.track_num, 
        song.duration, 
        song.release_date
    ))
    conn.commit()


def insert_has(has: Has):
    sql = """
    INSERT INTO Has(alb_ID, art_ID)
    VALUES (%s, %s)
    """
    db_cursor.execute(sql, (has.alb_id, has.art_id))
    conn.commit()

def insert_must(must: MustHave):
    sql = """
    INSERT INTO Must_Have(art_ID, song_ID)
    VALUES (%s, %s)
    """
    db_cursor.execute(sql, (must.art_id, must.song_id))
    conn.commit()

def insert_belongs(belongs: BelongsTo):
    sql = """
    INSERT INTO Belongs_To(alb_ID, song_ID)
    VALUES (%s, %s)
    """
    db_cursor.execute(sql, (belongs.alb_id, belongs.song_id))
    conn.commit()


# SELECT QUERIES
def get_song_by_name(name):
    sql = """
    SELECT * FROM Song
    WHERE song_name = %s
    """
    db_cursor.execute(sql, (name,))
    song = Song(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
    return song
    


# def get_farmer_by_pk(pk):
#     sql = """
#     SELECT * FROM Farmers
#     WHERE pk = %s
#     """
#     db_cursor.execute(sql, (pk,))
#     farmer = Farmer(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
#     return farmer


# def get_produce_by_filters(category=None, item=None, variety=None,
#                            farmer_pk=None, farmer_name=None, price=None):
#     sql = """
#     SELECT * FROM vw_produce
#     WHERE
#     """
#     conditionals = []
#     if category:
#         conditionals.append(f"category='{category}'")
#     if item:
#         conditionals.append(f"item='{item}'")
#     if variety:
#         conditionals.append(f"variety = '{variety}'")
#     if farmer_pk:
#         conditionals.append(f"farmer_pk = '{farmer_pk}'")
#     if farmer_name:
#         conditionals.append(f"farmer_name LIKE '%{farmer_name}%'")
#     if price:
#         conditionals.append(f"price <= {price}")

#     args_str = ' AND '.join(conditionals)
#     order = " ORDER BY price "
#     db_cursor.execute(sql + args_str + order)
#     produce = [Produce(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
#     return produce


# def get_customer_by_pk(pk):
#     sql = """
#     SELECT * FROM Customers
#     WHERE pk = %s
#     """
#     db_cursor.execute(sql, (pk,))
#     customer = Customer(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
#     return customer


# def get_produce_by_pk(pk):
#     sql = """
#     SELECT produce_pk as pk, * FROM vw_produce
#     WHERE produce_pk = %s
#     """
#     db_cursor.execute(sql, (pk,))
#     produce = Produce(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
#     return produce


# def get_all_produce_by_farmer(pk):
#     sql = """
#     SELECT * FROM vw_produce
#     WHERE farmer_pk = %s
#     ORDER BY available DESC, price
#     """
#     db_cursor.execute(sql, (pk,))
#     produce = [Produce(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
#     return produce


# def get_user_by_user_name(user_name):
#     sql = """
#     SELECT * FROM Users
#     WHERE user_name = %s
#     """
#     db_cursor.execute(sql, (user_name,))
#     user = User(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
#     return user


# def get_all_produce():
#     sql = """
#     SELECT produce_pk as pk, category, item, variety, unit, price, farmer_name, available, farmer_pk
#     FROM vw_produce
#     ORDER BY available DESC, price
#     """
#     db_cursor.execute(sql)
#     produce = [Produce(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
#     return produce


# def get_available_produce():
#     sql = """
#     SELECT * FROM vw_produce
#     WHERE available = true
#     ORDER BY price  
#     """
#     db_cursor.execute(sql)
#     produce = [Produce(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
#     return produce


# def get_orders_by_customer_pk(pk):
#     sql = """
#     SELECT * FROM ProduceOrder po
#     JOIN Produce p ON p.pk = po.produce_pk
#     WHERE customer_pk = %s
#     """
#     db_cursor.execute(sql, (pk,))
#     orders = [ProduceOrder(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
#     return orders


# # UPDATE QUERIES
# def update_sell(available, produce_pk, farmer_pk):
#     sql = """
#     UPDATE Sell
#     SET available = %s
#     WHERE produce_pk = %s
#     AND farmer_pk = %s
#     """
#     db_cursor.execute(sql, (available, produce_pk, farmer_pk))
#     conn.commit()