<template>
  <div id="sigma-container" style="width: 75%; height: 75%"></div>
</template>

<script>
import { onMounted } from "vue";

export default {
  setup() {
    onMounted(() => {
      const s = new sigma({
        graph: {
          nodes: [
            { id: "1", label: "Quinn Hou", x: 0, y: 0, size: 3, color: "#f00" },
            {
              id: "2",
              label: "Furkan Uzumcu",
              x: 1,
              y: 1,
              size: 3,
              color: "#0f0",
            },
            { id: "3", label: "MeiMei", x: 2, y: 0, size: 3, color: "#00f" },
          ],
          edges: [
            { id: "e1", source: "1", target: "2", size: 1, color: "#ccc" },
            { id: "e2", source: "2", target: "3", size: 1, color: "#ccc" },
          ],
        },
        container: "sigma-container",
        settings: {
          defaultNodeColor: "#ec5148",
          defaultEdgeColor: "#ec5148",
          edgeColor: "default",
          minNodeSize: 1,
          maxNodeSize: 10,
          minEdgeSize: 0.5,
          maxEdgeSize: 4,
        },
      });
    });
  },
};
</script>
