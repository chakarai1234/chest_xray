import React, { useState, useEffect } from "react";
import "./App.css";
import { browser, loadLayersModel } from "@tensorflow/tfjs";

function App() {
  const [image, setImage] = useState();
  const [pred, setPred] = useState("");
  const [showLabel, setShowLabel] = useState("visible");

  const uploadImage = (e) => {
    setImage(e.target.files[0]);
    // console.log(e.target.files[0]);
  };
  useEffect(() => {
    if (image !== undefined) {
      // console.log(fs.readFileSync(image));
      const im = new Image();
      let fr = new FileReader();
      fr.onload = () => {
        im.src = fr.result;
      };
      fr.readAsDataURL(image);
      im.onload = () => {
        const a = browser.fromPixels(im).resizeNearestNeighbor([224, 224]).expandDims().toFloat().reverse(-1);
        console.log(a);
        const chakara = async () => {
          const model = await loadLayersModel("https://mlchakaraproj.herokuapp.com/chest_xray/model.json");

          return model;
        };
        chakara().then((model) =>
          model
            .predict(a)
            .data()
            .then((data) => {
              if (data[0] > data[1]) {
                setPred("Normal");
              } else {
                setPred("Pneumonia");
              }
            }),
        );
        setShowLabel("hidden");
      };
    }
    return () => {};
  }, [image]);

  return (
    <div className="app">
      <label htmlFor="images" className="label" style={{ visibility: showLabel }}>
        Upload image
        <input type="file" name="images" id="images" className="images" style={{ display: "none" }} accept="image/*" onChange={uploadImage} />
      </label>
      {image === undefined ? <div></div> : <img src={URL.createObjectURL(image)} className="uploadedImage" alt="PleaseUploadanImageForSuggesting" />}
      {pred !== "" ? pred === "Normal" ? <h1 style={{ color: "green" }}>NORMAL</h1> : <h1 style={{ color: "red" }}>PNEUMONIA</h1> : <h1>No Pred Yet</h1>}
    </div>
  );
}

export default App;
