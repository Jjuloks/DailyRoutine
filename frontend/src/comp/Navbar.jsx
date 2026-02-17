import React from 'react';
import { NavLink } from 'react-router-dom';
import "./Navbar.css"


const NavBar =() => {
    return (
        <nav className="whole-navbar"> 
        <div className="navbar">
            <div className="navbarlinks">
                <NavLink to='/'>Add Task</NavLink>
                <NavLink to='/today'>Today</NavLink>
                <NavLink to='/calendar'>Calendar</NavLink>
                <NavLink to='/stats'>Stats</NavLink>
            </div>
        </div>
        </nav>
    )
}
export default NavBar;