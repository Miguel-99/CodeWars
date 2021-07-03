/*
Input

The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters
Output

Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
Examples

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
*/
function songDecoder(song){
  return song.split("WUB").filter( x => x).join(" ")
}

console.log(songDecoder("AWUBBWUBC")) //"A B C"
console.log(songDecoder("AWUBWUBWUBBWUBWUBWUBC")) // "A B C"
console.log(songDecoder("WUBAWUBBWUBCWUB")) // "A B C"

/*
Test.assertEquals(songDecoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space");
Test.assertEquals(songDecoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space");
Test.assertEquals(songDecoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed");
*/
