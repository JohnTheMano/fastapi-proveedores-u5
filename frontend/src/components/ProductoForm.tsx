export const ProductoForm = () => {
    return (
    <section className="rounded-2xl border border-stone-200 bg-white p-6 shadow-sm">
        <div className="mb-6">
        <h2 className="text-xl font-semibold tracking-tight text-stone-900">
            Agregar producto
        </h2>

        <p className="mt-1 text-sm text-stone-500">
            Completá los datos del nuevo producto.
        </p>
        </div>

        <form className="space-y-5">
        <div>
            <label
            htmlFor="nombre"
            className="mb-2 block text-sm font-medium text-stone-700"
            >
            Nombre
            </label>

            <input
            id="nombre"
            type="text"
            placeholder="Ej. Silla de Oficina"
            className="w-full rounded-lg border border-stone-200 bg-stone-50 px-4 py-3 text-sm text-stone-900 outline-none transition placeholder:text-stone-400 focus:border-stone-400 focus:bg-white"
            />
        </div>

        <div>
            <label
            htmlFor="categoria"
            className="mb-2 block text-sm font-medium text-stone-700"
            >
            Categoría
            </label>

            <input
            id="categoria"
            type="text"
            placeholder="Ej. MUE-01"
            className="w-full rounded-lg border border-stone-200 bg-stone-50 px-4 py-3 text-sm text-stone-900 outline-none transition placeholder:text-stone-400 focus:border-stone-400 focus:bg-white"
            />
        </div>

        <div className="grid gap-5 sm:grid-cols-2">
            <div>
            <label
                htmlFor="precio"
                className="mb-2 block text-sm font-medium text-stone-700"
            >
                Precio
            </label>

            <input
                id="precio"
                type="number"
                placeholder="0.00"
                className="w-full rounded-lg border border-stone-200 bg-stone-50 px-4 py-3 text-sm text-stone-900 outline-none transition placeholder:text-stone-400 focus:border-stone-400 focus:bg-white"
            />
            </div>

            <div>
            <label
                htmlFor="stock"
                className="mb-2 block text-sm font-medium text-stone-700"
            >
                Stock
            </label>

            <input
                id="stock"
                type="number"
                placeholder="0"
                className="w-full rounded-lg border border-stone-200 bg-stone-50 px-4 py-3 text-sm text-stone-900 outline-none transition placeholder:text-stone-400 focus:border-stone-400 focus:bg-white"
            />
            </div>
        </div>

        <button
            type="button"
            className="w-full rounded-lg bg-stone-900 px-5 py-3 text-sm font-medium text-white transition hover:bg-stone-700"
        >
            Agregar producto
        </button>
        </form>
    </section>
    )
}
