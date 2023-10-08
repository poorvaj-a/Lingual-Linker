import './App.css';
import { useState } from 'react';
function App() {
  const [text, setText] = useState('')
  const [from_lang, setFrom_lang] = useState('English')
  const [to_lang, setTo_lang] = useState('English')
  const [from_Number, setFrom_Number] = useState('')
  const [to_Number, setTo_Number] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    const message = { text, from_lang, to_lang, from_Number, to_Number }
    console.log(message)
    const response = await fetch('/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(message)
    })
    if (response.ok) {
      // console.log('message sent')
      alert("Message queued successfully")
    }
    else {
      alert("Please check the inputs again")
    }
  }

  return (
    // <div class="form-body">
      // <div class="row">
        <div class="form-holder">
          <div class="form-content">
            <div class="form-items">
            <form className='create' onSubmit={handleSubmit}>
              <h3>
                Send a message
              </h3>
              
              <div class="form-button" id="form-button"></div>
              
              <label>
                Message:
              </label>
              <input type="text" value={text} onChange={(e) => setText(e.target.value)} />
              
              <div class="form-button" id="form-button"></div>

              <label>
                From Number:
              </label>
              <input type="tel" value={from_Number} onChange={(e) => setFrom_Number(e.target.value)} />
              
              <div class="form-button" id="form-button"></div>
              
              <label> To Number: </label>
              <input type="tel" value={to_Number} onChange={(e) => setTo_Number(e.target.value)} />
              
              <div class="form-button" id="form-button"></div>
              
              <label>
        From Language:
      </label>
      
        <select  onChange={ (e) => setFrom_lang(e.target.value)}> 
        <option value="English">English</option> 
        <option value="Hindi">Hindi</option>
        <option value="Spanish">Spanish</option>
        <option value="French">French</option>
        </select>

        <div class="form-button" id="form-button"></div>

        <label>
        To Language:
      </label>
      
      <select onChange={ (e) => setTo_lang(e.target.value)}> 
        <option value="English">English</option> 
        <option value="Hindi">Hindi</option>
        <option value="Spanish">Spanish</option>
        <option value="French">French</option>
        </select>
              {/* <button type="submit">Send</button> */}
              <div class="form-button" id="form-button">
              <div class="form-button" id="form-button"></div> 
                <button id="submit" type="submit" class="btn btn-primary" onClick={handleSubmit}>Submit</button>
              </div>
            </form>
          </div>
          </div>
          </div>
          // </div>
    // </div>
  )

}

export default App;
