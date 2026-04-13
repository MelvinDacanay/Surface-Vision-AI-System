import { useState } from 'react';

function App() {
  const [image, imageAdd] = useState(null);
  const [confidence, confidenceAdd] = useState(.03)
  const [sqfeet, sqfeetAdd] = useState(0)
  
  const newImg = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('file', file);
    const res = await fetch('http://localhost:8000/static',
      {method: 'POST', body: formData}
    );
    const data = await res.json();
    sqfeetAdd(data.sq_feet)
    imageAdd(`${data.url}?t=${Date.now()}`);
  }

  const confChanged = async (e) => {
    const value = e.target.value;
    confidenceAdd(value)

    const formData = new FormData();
    formData.append('conf', value);
    // formData.append('file', 'Backend/static/new.jpg');

    const res = await fetch('http://localhost:8000/static', {method: 'PUT', body: formData})
    const data = await res.json() 
    imageAdd(`${data.url}/new.jpg?t=${Date.now()}`)
    sqfeetAdd(data.sq_feet)
  }

  const reset = () => {
    fetch('http://localhost:8000/static', {method: 'DELETE'});
    window.location.reload();
  };

  return (
    <div>
      <h1>
        <img src='src\assets\logo.PNG' style={{maxWidth: '50px', padding: 5}}/>
        Driveway Square Feet Calculator 
      <div style={{padding: 10}}/>
      </h1>
      <input type='file' onChange={newImg}/>
    <div style={{padding: 5}}/>
      <input type='number' onChange={confChanged}/>
    <div></div>
      <button onClick={reset}>
        reset
      </button>
      <div style={{padding: 20}}>
        {image && <img src={image} style={{maxWidth: '400px'}}/>}
      </div>
      <h3>
        {sqfeet} square feet
      </h3>
    </div>
  );
};

export default App;
