export default function Register() {
  return (
    <div className="max-w-md mx-auto bg-white shadow-lg rounded-lg p-6 mt-10">
      <h2 className="text-2xl font-bold mb-4 text-center">Register</h2>
      <form className="space-y-4">
        <input 
          type="text" 
          placeholder="Username" 
          className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring focus:ring-indigo-200"
        />
        <input 
          type="email" 
          placeholder="Email" 
          className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring focus:ring-indigo-200"
        />
        <input 
          type="password" 
          placeholder="Password" 
          className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring focus:ring-indigo-200"
        />
        <button 
          type="submit" 
          className="w-full bg-indigo-600 text-white py-2 rounded hover:bg-indigo-700"
        >
          Register
        </button>
      </form>
    </div>
  );
}
