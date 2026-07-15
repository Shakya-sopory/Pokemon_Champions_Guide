
export default async function Home(){
  type Pokemon={
    name: string,
    usage: number
  }
  const response=await fetch("http://127.0.0.1:8000/home");
  const rankings: Pokemon[]=await response.json();
  return(
    <main>
      <h1>Pokemon Champions VGC guide re-b</h1>
    <ol>
      {rankings.map((pokemon)=>(
        <li key={pokemon.name}>
          {pokemon.name}-{(pokemon.usage*100).toFixed(2)}%
        </li>
      ))}
    </ol>
    </main>
  );
}