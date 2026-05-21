import React from "react";
import ReactDOM from "react-dom";
import VoiceRecorder from "./components/VoiceRecorder";
import AppointmentUI from "./components/AppointmentUI";

const App = () => {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>🩺 Voice AI Agent Demo</h1>
      <VoiceRecorder />
      <AppointmentUI />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));
