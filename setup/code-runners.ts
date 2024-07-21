import { defineCodeRunnersSetup } from '@slidev/types'
import { exec } from 'child_process'

async function executeLispCodeRemotely(code) {
  return new Promise((resolve, reject) => {
    exec(`sbcl --script -`, { input: code }, (error, stdout, stderr) => {
      if (error) {
        reject(stderr);
      } else {
        resolve(stdout);
      }
    });
  });
}

export default defineCodeRunnersSetup(() => {
  return {
    async python(code, ctx) {
      const result = await executePythonCodeRemotely(code)
      return {
        text: result
      }
    },
    html(code, ctx) {
      return {
        html: sanitizeHtml(code)
      }
    },
    async lisp(code, ctx) {
      const result = await executeLispCodeRemotely(code)
      return {
        text: result
      }
    }
  }
})
