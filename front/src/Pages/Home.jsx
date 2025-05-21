import React from "react";
import Winxcarrossel from '../components/WinxCarrossel'
import Navbar from '../components/NavBar'
import '../styles/Home.css';


const Home = () => {
    return (
        <div>
            <Navbar />
            <section className="home-container">
            <div className="home-hero">
                <h1 className="home-title">Clube das Winx</h1>
                <p className="home-subtitle">Explore o mundo mágico das fadas</p>
            </div>
            <Winxcarrossel />
            </section>

        </div>
    )
}

export default Home
