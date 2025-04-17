import React from "react";
import Winxcarrossel from '../components/WinxCarrossel'
import Navbar from '../components/NavBar'

const Home = () => {
    return (
        <div>
            <Navbar />

            <section className="home-container">
            <h1 className="home-title">Clube das Winxs </h1>
            <p className="home-subtitle">Explore o mundo mágico das fadas</p>   
           <Winxcarrossel/>
            </section>
        </div>
    )
}

export default Home
