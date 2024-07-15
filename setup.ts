import { defineSetup } from '@slidev/types'

export default defineSetup(() => {
  return {
    head: {
      script: [
        {
          src: 'https://cdnjs.cloudflare.com/ajax/libs/sigma.js/3.0.0-alpha2/sigma.min.js',
          defer: true,
        },
      ],
    },
  }
})

