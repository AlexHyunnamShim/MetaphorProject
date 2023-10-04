import React, { useState } from 'react';
import axios from 'axios';

function ChatbotUI() {
  const [inputValue, setInputValue] = useState('');
  const [messages, setMessages] = useState([]);

  async function handleSubmit(event) {
    event.preventDefault();
    const response = await axios.post('http://localhost:5000/api/link_summarizer', { message: inputValue });
    const newMessages = [...messages, { text: inputValue, isUser: true }, { text: response.data.response, isUser: false }];
    setMessages(newMessages);
    setInputValue('');
  }

  function handleInputChange(event) {
    setInputValue(event.target.value);
  }

  return (
    <div className="chatbot-ui">
      <div className="messages">
        {messages.map((message, index) => {
          if (index % 2 === 0) {
            // this is a user message
            return (
              <div key={index} className="user-message">
                {message.text}
              </div>
            );
          } else {
            // this is a bot message
            return (
              <div key={index} className="bot-message">
                {message.text}
              </div>
            );
          }
        })}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Type your message here..."
          value={inputValue}
          onChange={handleInputChange}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default ChatbotUI;
