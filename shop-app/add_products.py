import sqlite3

products = [
    ("Chaussures Antigravité", 120.00, 4.9, "https://image.made-in-china.com/202f0j00uvhiLEMdARkA/Kangoo-Jump-Shoes-Kangaroo-Anti-Gravity-Running-Jumping-Bouncing-Shoes.webp", "DH"),
    ("Miel ZCH", 15.99, 4.7, "https://media.istockphoto.com/id/598241944/fr/photo/miel-en-pot-et-bouquet-de-lavande-s%C3%A8che.jpg?s=612x612&w=0&k=20&c=N8QEPGZuQWQMjRHBW0RgRMn-heqdqZiThVCDq2H990g=", "DH"),
    ("Dattes el mejhoul", 8.50, 4.8, "https://media.istockphoto.com/id/1178070137/fr/photo/dates-medjool-frais-dans-un-bol-fond-gris-copiez-lespace.jpg?s=612x612&w=0&k=20&c=KSqmRxA-pKyP14HTQaT3NuGxHE5ZJ5SGpV047HwRbWM=", "DH"),
    ("Jus Dattes el mejhoul", 6.20, 4.5, "https://thumbs.dreamstime.com/b/boisson-de-jus-dattes-d%C3%A9licieux-avec-des-fra%C3%AEches-sur-table-en-bois-une-photo-closeup-r%C3%A9v%C3%A8le-un-verre-sa-riche-teinte-d-ambre-365116944.jpg", "DH"),
    ("Huile d'Argan", 12.90, 4.9, "https://img.passeportsante.net/1200x675/2021-05-03/i104245-huile-argan.webp", "DH"),
    ("Amandes Maroc", 7.80, 4.6, "https://www.bladi.net/img/logo/amande-americaine-maroc.jpg", "DH"),
    ("Safran Premium", 20.00, 4.8, "https://m.media-amazon.com/images/I/71Prfvax+PS._AC_UF1000,1000_QL80_.jpg", "DH"),
    ("Eau de Rose", 11.40, 4.4, "https://media.istockphoto.com/id/506669699/fr/photo/eau-de-rose-rose-et-de-magnifiques-fleurs-macro-horizontal.jpg?s=612x612&w=0&k=20&c=8SS9jnyWel63PyxvAEnwwuCNumdVQSqxN_1qla8FPTk=", "DH"),
    ("Pistaches Grillées", 14.20, 4.8, "https://www.goji.ma/cdn/shop/products/Pistachesgrilleessaleesbio.jpg?v=1672009454&width=1445", "DH")
]

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

for name, price, rating, image_url, currency in products:
    cursor.execute("""
        INSERT INTO products (name, price, rating, image_url, currency)
        VALUES (?, ?, ?, ?, ?)
    """, (name, price, rating, image_url, currency))

conn.commit()
conn.close()
print("Produits ajoutés avec succès.")