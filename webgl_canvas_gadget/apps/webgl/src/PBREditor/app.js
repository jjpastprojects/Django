window.addEventListener('DOMContentLoaded', function () {
    var canvas = document.getElementById('renderCanvas');
    var engine = new BABYLON.Engine(canvas, true);
    var gui = new dat.GUI();
    var hdrTexture;
    var oldPos;
    var meshes = [];
    var currSphere;
    function generateJson(pbr, display) {
        var txt = '{' +
            '"name":"' + pbr.name + '",' +
            '"isGlass":"' + (pbr.refractionTexture ? "true" : "false") + '",' +
            '"indexOfRefraction":' + pbr.indexOfRefraction.toPrecision(2) + ',' +
            '"alpha":' + pbr.alpha.toPrecision(2) + ',' +
            '"directIntensity":' + pbr.directIntensity.toPrecision(2) + ',' +
            '"emissiveIntensity":' + pbr.emissiveIntensity.toPrecision(2) + ',' +
            '"environmentIntensity":' + pbr.environmentIntensity.toPrecision(2) + ',' +
            '"specularIntensity":' + pbr.specularIntensity.toPrecision(2) + ',' +
            '"overloadedShadowIntensity":' + pbr.overloadedShadowIntensity.toPrecision(2) + ',' +
            '"overloadedShadeIntensity":' + pbr.overloadedShadeIntensity.toPrecision(2) + ',' +
            '"cameraExposure":' + pbr.cameraExposure.toPrecision(2) + ',' +
            '"cameraContrast":' + pbr.cameraContrast.toPrecision(2) + ',' +
            '"microSurface":' + pbr.microSurface.toPrecision(2) + ',' +
            '"reflectivityColor":{"r":' + pbr.reflectivityColor.r.toPrecision(2) + ', "g":' + pbr.reflectivityColor.g.toPrecision(2) + ', "b":' + pbr.reflectivityColor.b.toPrecision(2) + '}' +
            '}';
        if (display) {
            var txtAre = document.getElementById("txt");
            var btn = document.getElementById("btn");
            txtAre.textContent = txt;
        }
        return txt;
    }
    function displayMaterialValues(material, scene) {
        var folder = gui.addFolder(material.name);
        var name = folder.add(material, "name").listen();
        name.onFinishChange(function (value) {
            if (value.indexOf("{") > -1) {
                var jsonMat = JSON.parse(value);
                material.name = jsonMat.name;
                material.indexOfRefraction = jsonMat.indexOfRefraction;
                material.alpha = jsonMat.alpha;
                material.directIntensity = jsonMat.directIntensity;
                material.emissiveColor = jsonMat.emissiveColor;
                material.emissiveIntensity = jsonMat.emissiveIntensity;
                material.environmentIntensity = jsonMat.environmentIntensity;
                material.specularIntensity = jsonMat.specularIntensity;
                material.overloadedShadowIntensity = jsonMat.overloadedShadowIntensity;
                material.overloadedShadeIntensity = jsonMat.overloadedShadeIntensity;
                material.cameraExposure = jsonMat.cameraExposure;
                material.cameraContrast = jsonMat.cameraContrast;
                material.microSurface = jsonMat.microSurface;
                material.reflectivityColor = new BABYLON.Color3(jsonMat.reflectivityColor.r, jsonMat.reflectivityColor.g, jsonMat.reflectivityColor.b);
            }
        });
        folder.add(material, "indexOfRefraction", 0, 2).listen();
        folder.add(material, "alpha", 0, 1).listen();
        folder.add(material, "directIntensity", 0, 2).listen();
        var emissive = folder.addColor(material, "emissiveColor").listen();
        emissive.onChange(function (value) {
            material.emissiveColor = new BABYLON.Color3(value.r / 255.0, value.g / 255.0, value.b / 255.0);
        });
        folder.add(material, "emissiveIntensity", 0, 2).listen();
        folder.add(material, "environmentIntensity", 0, 2).listen();
        folder.add(material, "specularIntensity", 0, 2).listen();
        folder.add(material, "overloadedShadowIntensity", 0, 2).listen();
        folder.add(material, "overloadedShadeIntensity", 0, 2).listen();
        folder.add(material, "cameraExposure", 0, 2).listen();
        folder.add(material, "cameraContrast", 0, 2).listen();
        folder.add(material, "microSurface", 0, 1).listen();
        var color = folder.addColor(material, "albedoColor").listen();
        color.onChange(function (value) {
            material.albedoColor = new BABYLON.Color3(value.r / 255.0, value.g / 255.0, value.b / 255.0);
        });
        folder.add(material.reflectivityColor, "r", 0, 1.0).listen();
        folder.add(material.reflectivityColor, "g", 0, 1.0).listen();
        folder.add(material.reflectivityColor, "b", 0, 1.0).listen();
        var obj = {
            Generate_Json: function () {
                var txt = '{' +
                    '"name":"' + material.name + '",' +
                    '"isGlass":"' + (material.refractionTexture ? "true" : "false") + '",' +
                    '"indexOfRefraction":' + material.indexOfRefraction.toPrecision(2) + ',' +
                    '"alpha":' + material.alpha.toPrecision(2) + ',' +
                    '"directIntensity":' + material.directIntensity.toPrecision(2) + ',' +
                    '"emissiveIntensity":' + material.emissiveIntensity.toPrecision(2) + ',' +
                    '"environmentIntensity":' + material.environmentIntensity.toPrecision(2) + ',' +
                    '"specularIntensity":' + material.specularIntensity.toPrecision(2) + ',' +
                    '"overloadedShadowIntensity":' + material.overloadedShadowIntensity.toPrecision(2) + ',' +
                    '"overloadedShadeIntensity":' + material.overloadedShadeIntensity.toPrecision(2) + ',' +
                    '"cameraExposure":' + material.cameraExposure.toPrecision(2) + ',' +
                    '"cameraContrast":' + material.cameraContrast.toPrecision(2) + ',' +
                    '"microSurface":' + material.microSurface.toPrecision(2) + ',' +
                    '"reflectivityColor":{"r":' + material.reflectivityColor.r.toPrecision(2) + ', "g":' + material.reflectivityColor.g.toPrecision(2) + ', "b":' + material.reflectivityColor.b.toPrecision(2) + '}' +
                    '}';
                var txtAre = document.getElementById("txt");
                var btn = document.getElementById("btn");
                txtAre.textContent = txt;
            }
        };
        folder.add(obj, 'Generate_Json');
    }
    function updateTexture(scene) {
        var file = document.querySelector('#groundImg').files[0];
        var reader = new FileReader();
        if (file) {
            reader.readAsDataURL(file);
        }
        else {
            this.environments[this.currentEnvironment].groundTexture = null;
        }
        reader.onloadend = function () {
            console.log(file.name);
            for (var i = 0; i < meshes.length; i++) {
                var mesh = meshes[i];
                if (mesh.material.albedoTexture)
                    mesh.material.albedoTexture.dispose();
                mesh.material.albedoTexture = BABYLON.Texture.CreateFromBase64String(reader.result, file.name, scene);
            }
        };
    }
    function createScene() {
        var scene = new BABYLON.Scene(engine);
        var camera = new BABYLON.FreeCamera("Camera", new BABYLON.Vector3(0, 30, 30), scene);
        camera.setTarget(BABYLON.Vector3.Zero());
        camera.attachControl(canvas, false);
        scene.activeCamera = camera;
        scene.clearColor = BABYLON.Color3.Gray();
        var hemilight = new BABYLON.HemisphericLight("hemilight", new BABYLON.Vector3(0, 1, 0), scene);
        hemilight.range = 1;
        hemilight.intensity = 1;
        hdrTexture = new BABYLON.CubeTexture("./skybox/skybox", scene);
        var hdrSkybox = BABYLON.Mesh.CreateBox("hdrSkyBox", 1000.0, scene);
        var hdrSkyboxMaterial = new BABYLON.PBRMaterial("skyBox", scene);
        hdrSkyboxMaterial.backFaceCulling = false;
        hdrSkyboxMaterial.reflectionTexture = hdrTexture.clone();
        hdrSkyboxMaterial.reflectionTexture.coordinatesMode = BABYLON.Texture.SKYBOX_MODE;
        hdrSkyboxMaterial.microSurface = .99;
        hdrSkyboxMaterial.cameraExposure = 0.6;
        hdrSkyboxMaterial.cameraContrast = 1.6;
        hdrSkybox.material = hdrSkyboxMaterial;
        hdrSkybox.infiniteDistance = true;
        var meshMaterial = new BABYLON.PBRMaterial("mat", scene);
        meshMaterial.reflectivityColor = BABYLON.Color3.Black();
        displayMaterialValues(meshMaterial, scene);
        meshMaterial.reflectionTexture = hdrTexture;
        {
            var Sphere = BABYLON.Mesh.CreateSphere("Sphere", 100, 6, scene, true);
            Sphere.material = meshMaterial;
            Sphere.position.addInPlace(new BABYLON.Vector3(8, 0, 0));
            meshes.push(Sphere);
        }
        {
            var Cube = BABYLON.Mesh.CreateBox("Cube", 6, scene, true);
            Cube.material = meshMaterial;
            Cube.position.addInPlace(new BABYLON.Vector3(0, 0, 0));
            meshes.push(Cube);
        }
        {
            var Plane = BABYLON.Mesh.CreatePlane("Plane", 6, scene, true);
            Plane.material = meshMaterial;
            Plane.position.addInPlace(new BABYLON.Vector3(-8, 0, 0));
            Plane.rotate(new BABYLON.Vector3(1, 0, 0), 1.5708);
            meshes.push(Plane);
        }
        var txtAre = document.getElementById("txt");
        var btn = document.getElementById("btn");
        btn.onclick = function (ev) {
            var txt = "[";
            for (var i = 0; i < scene.meshes.length; i++) {
                if (scene.meshes[i].material instanceof BABYLON.PBRMaterial && scene.meshes[i].material.name != "skyBox") {
                    txt += generateJson(scene.meshes[i].material, false);
                    txt += ",";
                }
            }
            txt = txt.substr(0, txt.length - 2);
            txt += "]";
            txtAre.textContent = txt;
        };
        return scene;
    }
    ;
    var scene = createScene();
    document.getElementById("groundImg").onchange = function (e) { return updateTexture(scene); };
    engine.runRenderLoop(function () {
        scene.render();
    });
    window.addEventListener('resize', function () {
        engine.resize();
    });
});
