import { useState } from "react";

export default function Home() {
  const [task, setTask] = useState("");
  const [tasks, setTasks] = useState([]);

  const addTask = (e) => {
    e.preventDefault();
    if (!task.trim()) return; // ignore empty tasks
    setTasks([...tasks, task]);
    setTask("");
  };

  return (
    <div className="max-w-2xl mx-auto mt-10 p-6 bg-white shadow-lg rounded-lg">
      <h2 className="text-3xl font-bold text-gray-800 text-center">SmartTasker 🚀</h2>
      <p className="text-gray-600 mt-2 text-center">
        Track your tasks, build habits, and boost productivity.
      </p>

      {/* Add Task Form */}
      <form onSubmit={addTask} className="flex gap-2 mt-6">
        <input
          type="text"
          placeholder="Enter your task..."
          value={task}
          onChange={(e) => setTask(e.target.value)}
          className="flex-1 border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring focus:ring-indigo-200"
        />
        <button
          type="submit"
          className="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700"
        >
          Add
        </button>
      </form>

      {/* Task List */}
      <ul className="mt-6 space-y-2">
        {tasks.length === 0 ? (
          <li className="text-gray-500 text-center">No tasks yet. Add one above!</li>
        ) : (
          tasks.map((t, index) => (
            <li
              key={index}
              className="p-3 bg-gray-100 rounded-lg flex justify-between items-center"
            >
              <span>{t}</span>
              <button
                onClick={() => setTasks(tasks.filter((_, i) => i !== index))}
                className="text-red-500 hover:text-red-700"
              >
                ✕
              </button>
            </li>
          ))
        )}
      </ul>
    </div>
  );
}
