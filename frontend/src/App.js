import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Dashboard from './pages/Dashboard';

function App() {	
	return (
	<Router>
		<Routes>
			<Route exact path='/*' element={<Dashboard />} />
			<Route path='/about' element={<Dashboard/>} />
			
		</Routes>
	</Router>
);
}

export default App;