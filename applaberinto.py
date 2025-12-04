import streamlit as st
from maze_solver import MAZE, START, END, solve_maze_bfs, solve_maze_dfs, solve_maze_a_star

st.title("Visualizador de Algoritmo de Busqueda en Laberinto")

# Funcion para renderizar el laberinto usando emojis
def render_maze(maze, path=None):
    if path is None:
        path = []

    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🚀")  # Inicio
            elif (r_idx, c_idx) == END:
                display_row.append("🏁")  # Fin
            elif (r_idx, c_idx) in path:
                display_row.append("🔹")  # Camino resuelto
            elif col == 1:
                display_row.append("⬛")  # Muro
            else:
                display_row.append("⬜")  # Camino libre
        display_maze.append("".join(display_row))

    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)


# Sidebar para controles
st.sidebar.header("Opciones")
available_algorithms = {
    "BFS": solve_maze_bfs,
    "DFS": solve_maze_dfs,
    "A*": solve_maze_a_star,
}
algorithm = st.sidebar.selectbox(
    "Selecciona el algoritmo",
    list(available_algorithms.keys()),
)
solve_button = st.sidebar.button("Resolver Laberinto")

# Mostrar laberinto inicial
render_maze(MAZE)

if solve_button:
    if algorithm in available_algorithms:
        solver = available_algorithms[algorithm]
        path = solver(MAZE, START, END)
        if path:
            st.success(f"Camino encontrado con {algorithm}!")
            render_maze(MAZE, path)
        else:
            st.error("No se encontro un camino.")
    else:
        st.warning(f"El algoritmo {algorithm} aun no esta implementado. Usa BFS.")
