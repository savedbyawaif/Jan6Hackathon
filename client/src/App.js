import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from "react"

function App() {
  const [data,setData] = useState([])
  useEffect(() => {
    fetch("/registration").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  })

  return (
    <div>
      <script>
        function myFunc(){
          console.log("hi")
        }
      </script>
      <header>
        <button type="button" onclick="myFunc()">
          djaidw
        </button>
        myFunc()
        <p>{data}</p>
      </header>

      hjidhaoiwd
    </div>
  );
}

function PharmList() {
  return (
    <div>
      hello
    </div>
  )
}

export default App;
