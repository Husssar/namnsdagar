# namnsdagar

This is just a small project I did to keep track of my wife names day (namnsdag in sweden)
I know here is a lot of other projects, but not with python. I wanted to do one in python because I wanted to.

## To use:
`docker buildx build --tag namesday .`
`docker run --rm --publish 8080:8080 namesday `

To show this days namesday
`curl http://localhost:8080/all `
curl http://localhost:8080/today

To show all namesday
`curl http://localhost:8080/all`

## Example
 curl http://localhost:8080/today
{"Day":15,"Month":"November","namesday":"Leopold"}

