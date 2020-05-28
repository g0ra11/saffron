import React from "react";

function Header() {
  return (
    <div
      className="jumbotron text-white jumbotron-image shadow"
      style={{
        backgroundImage: `url(https://www.ecopetit.cat/wpic/mpic/50-506143_royal-blue-background-wallpaper-luxury-blue-wallpaper-hd.png)`,
        backgroundPosition: 'center',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        marginBottom: 0
      }}
    >
      <h1>Your dummyshop is online now.</h1>
      <p>Don't miss exclusive deals!</p>
      </div>
  )
}

export default Header;