import React from "react"
import './App.css'
import { Routes,Route, Navigate } from 'react-router-dom';
import AddTaskPage from "./pages/AddTaskPage.jsx"
import CalendarPage from "./pages/CalendarPage.jsx"
import StatsPage from "./pages/StatsPage.jsx"
import TodayPage from "./pages/TodayPage.jsx"
import NavBar from "./comp/Navbar.jsx";

function App() {


  return (
    <>
    <NavBar/>
    <Routes>
      <Route path='/' element={<AddTaskPage />} />
      <Route path='/calendar' element={<CalendarPage />} />
      <Route path='/today' element={<TodayPage />} />
      <Route path='/stats' element={<StatsPage />} />
    </Routes>
    </>
  )
}

export default App
