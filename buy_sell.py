# classes

class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return '%s. "%s". %s, %s. %s, %s.' % (self.artist, self.title, self.medium, self.year, self.owner.name, self.owner.location)


class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listings(self, new_listing):
    return self.listings.append(new_listing)

  def remove_listings(self, removed_listing):
    return self.listings.remove(removed_listing)

  def show_listings(self):
    for piece in self.listings:
      print(piece)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = "Private Collection"

  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_list = Listing(artwork, price, self)
      veneer.add_listings(new_list)

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == listing:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.artwork.owner = self
        veneer.remove_listing(art_listing)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return "%s. %s." % (self.art.title, self.price)



#instance of Marketplace
veneer = Marketplace()
print(veneer.show_listings())

#instance of Client edytta
edytta = Client("Edytta Halpirt", None, False)

#instance of grlw/mndln
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)
print(girl_with_mandolin)
#instance of Client Moma
moma = Client("The Moma", "New York", True)

#edytta lists grlw/mdln
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
