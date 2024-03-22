<script>
    import atosLoad from './assets/notstonks.png'
    import StonksGraph from './lib/StonksGraph.svelte';
    import StonksTitle from "./lib/StonksTitle.svelte"
    async function getStonks(){
        let stonksRes = await fetch("http://localhost:5000/stonks")

        if(stonksRes.ok){
            return await stonksRes.json()
        }
    }

    let stonksPromise = getStonks();

</script>

<main>
    {#await stonksPromise}
        <h1>ATOS: STONKS</h1>
        <img src={atosLoad} alt="">
    {:then stonksData} 
        <StonksTitle stonks={stonksData}/>
        <StonksGraph stonks={stonksData.stonks} />
    {:catch error}
        <h2>Flash est une tanche</h2>
    {/await}

</main>

<style>

</style>
