const fs = require("fs");

global.window = {
    location: {
        hostname: "snapinsta.ai"
    }
};

global.location = {
    hostname: "snapinsta.ai"
};

const elementos = {};

global.document = {
    getElementById: (id) => {

        console.log("getElementById:", id);

        if (!elementos[id]) {

            elementos[id] = {
                innerHTML: "",
                style: {},
                appendChild: () => {},
                setAttribute: () => {},
                remove: () => {}
            };

        }

        return elementos[id];
    }
};

global.navigator = {};

global.localStorage = {
    getItem: () => null,
    setItem: () => {}
};

global.sessionStorage = {
    getItem: () => null,
    setItem: () => {}
};

global.turnstile = {
    render: () => {}
};

global.gtag = () => {};

const codigo = fs.readFileSync(
    "docs/action2_response.js",
    "utf8"
);

try {

    eval(codigo);

    fs.writeFileSync(
        "docs/html_final.html",
        JSON.stringify(
            elementos,
            null,
            2
        )
    );

   for (const chave in elementos) {

    console.log("\nID:", chave);

    console.log(
        elementos[chave].innerHTML
    );
}

} catch (e) {

    console.log("ERRO:");
    console.log(e);

}