<script>
    import {onMount} from "svelte"

    import Chart from "chart.js/auto"
    export let stonks
    let portfolio
    
    const data = {
        labels: stonks.map((x) => x.time),
        datasets: [{
            label: "Stonks €",
            data: stonks.map((x) => x.price)
        }]
    }

    let config = {
        type: 'line',
        data: data,
        options: {
            responsive: true,

        }
    }

    onMount(()=> {
        const ctx = portfolio.getContext('2d');
        // Initialize chart using default config set
        var myChart = new Chart(ctx, config);
    })

</script>

<canvas bind:this={portfolio} width={1200} height={800}></canvas>