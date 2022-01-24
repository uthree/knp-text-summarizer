

ws = new WebSocket("ws://localhost:9999/ws");

console.log("connected");
ws.onopen = async function() {
    elements = document.getElementsByTagName("*");
    for (i = 0; i < elements.length; i++) {
        element = elements[i];
        text = element.textContent;
        if ( text.match(/[亜-熙ぁ-んァ-ヶ]/) && (! text.match(/<javascript>|<script>|ur(l|i)=/) ) && text.length < 1000 ) {

            await ws.send(text);
            ws.onmessage = await function(event) {
                console.log(text + " -> " + event.data);
                element.textContent = event.data;
            };
        }
    }
}
