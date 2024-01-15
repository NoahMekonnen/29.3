const ul = $('ul')
const form = $('form')
const body = $('body')


async function getList(){
    const resp = await axios.get('/api/cupcakes')
    return resp.data
}

const listOfCupcakes = getList()
console.log(listOfCupcakes)
for (cupcake of listOfCupcakes){
    body.append(`<li>
    flavor: ${cupcake.flavor}
    size: ${cupcake.size}
    rating: ${cupcake.rating}
    <img src=${cupcake.image}>
    </li>`)
}

form.on('submit', postRequest)

async function postRequest(e){
    e.preventDefault()
    const flavor = $('#flavor')[0].value
    const size = $('#size')[0].value
    const rating = $('#rating')[0].value
    const image = $('#image')[0].value
    axios.post("/api/cupcakes",
    {"flavor":flavor,
    "size":size,
    "rating":parseFloat(rating),
    "image":image})
}