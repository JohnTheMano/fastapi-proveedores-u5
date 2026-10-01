import type { Producto } from '../types/producto'

type ProductoCardProps = {
    producto: Producto
}

export const ProductoCard = ({ producto }: ProductoCardProps) => {
    return (
    <article className="group rounded-2xl border border-stone-200 bg-white p-6 shadow-sm transition duration-200 hover:-translate-y-1 hover:shadow-md">
        <div className="mb-5 flex items-start justify-between gap-4">
        <span className="rounded-full bg-stone-100 px-3 py-1 text-xs font-medium text-stone-500">
            Producto #{producto.id}
        </span>

        <span className="text-xs text-stone-400">
            Disponible
        </span>
        </div>

        <h3 className="text-xl font-semibold tracking-tight text-stone-900">
        {producto.nombre}
        </h3>

        <p className="mt-2 min-h-12 text-sm leading-relaxed text-stone-500">
        {producto.descripcion}
        </p>

        <div className="mt-6 flex items-end justify-between border-t border-stone-100 pt-5">
        <div>
            <p className="text-xs font-medium uppercase tracking-wider text-stone-400">
            Precio
            </p>

            <p className="mt-1 text-2xl font-semibold tracking-tight text-stone-900">
            ${producto.precio.toFixed(2)}
            </p>
        </div>

        <button
            type="button"
            className="rounded-lg bg-stone-900 px-4 py-2.5 text-sm font-medium text-white transition hover:bg-stone-700"
        >
            Ver producto
        </button>
        </div>
    </article>
    )
}
