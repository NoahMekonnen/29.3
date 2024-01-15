const ul = $('ul')
const form = $('form')

listOfCupcakes = axios.get('/api/cupcakes')

form.on('submit', postRequest)

function postRequest(e){
    e.preventDefault()
    const flavor = $('#flavor').value
    const size = $('#size').value
    const rating = $('#rating').value
    const image = $('#image').value
    axios.post({url:'/api/cupcakes',
    data:{"flavor":flavor,
    "size":size,
    "rating":rating,
    "image":image}})
}