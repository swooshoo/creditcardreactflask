import React, {useState, useEffect} from 'react'

function App() {
	const [data, setData] = useState([{}])

// 	useEffect(() => {
// 		fetch("/members").then(
// 			res => res.json()
// 		).then(
// 			data => {
// 				setData(data)
// 				console.log(data)
// 			}
// 		)
// 	}, [])

//   return (
//     <div>
// 		{(typeof data.members === 'undefined') ? (
// 			<p>Loading...</p>
// 		) : (
// 			data.members.map((member, i) => (
// 				<p key={i}>{member}</p>
// 			))
// 		)}
//     </div>
//   )

  useEffect(() => {
	fetch("/creditcards").then(
		res => res.json()
	).then(
		data => {
			setData(data)
			console.log(data)
		}
	)
}, [])

return (
<div>
	{(typeof data.creditcards === 'undefined') ? (
		<p>Loading...</p>
	) : (
		data.creditcards.map((creditcard, i) => (
			<p key={i}>{creditcard}</p>
		))
	)}
</div>
)

}

export default App
