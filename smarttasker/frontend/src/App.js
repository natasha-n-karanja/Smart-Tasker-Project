import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";

function App() {
  return (
    <Router>
      {/* Navbar */}
      <nav className="bg-indigo-600 text-white px-6 py-4 flex justify-between items-center shadow">
        <h1 className="text-xl font-bold">SmartTasker</h1>
        <div className="space-x-4">
          <Link to="/" className="hover:text-indigo-200">Home</Link>
          <Link to="/login" className="hover:text-indigo-200">Login</Link>
          <Link to="/register" className="hover:text-indigo-200">Register</Link>
        </div>
      </nav>

      {/* Page Content */}
      <div className="p-6">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
