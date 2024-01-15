const ul = $('ul')
const form = $('form')
const body = $('body')


async function getList(){
    const resp = await axios.get('/api/cupcakes')
    listOfCupcakes = resp.data
    for (cupcake of listOfCupcakes.cupcakes){
        ul.append(`<li>
        flavor: ${cupcake.flavor}
        size: ${cupcake.size}
        rating: ${cupcake.rating}
        <img src=${cupcake.image}>
        </li>`)
    }
}

async function postRequest(e){
    e.preventDefault()
    const flavor = $('#flavor')[0].value
    const size = $('#size')[0].value
    const rating = $('#rating')[0].value
    console.log(rating)
    const image = $('#image')[0].value
    axios.post("/api/cupcakes",
    {"flavor":flavor,
    "size":size,
    "rating":parseFloat(rating),
    "image":image})
    ul.append(`<li>
    flavor: ${flavor}
    size: ${size}
    rating: ${rating}
    <img src=${image}></li>`)
}

getList()
form.on('submit', postRequest)