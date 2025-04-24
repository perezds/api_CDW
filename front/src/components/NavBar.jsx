import React from 'react'
import './NavBar.css'

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2 className="logo">Clube das Winx</h2>
      <ul className="nav-links">
        <li>Home</li>
        <li>Fadas</li>
      </ul>
    </nav>
  )
}

export default Navbar
