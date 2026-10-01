import type { Producto } from '../types/producto'
import { ProductoCard } from './ProductoCard'

type ProductoListProps = {
    productos: Producto[]
}

export const ProductoList = ({ productos }: ProductoListProps) => {
    return (
    <section className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        {productos.map((producto) => (
        <ProductoCard key={producto.id} producto={producto} />
        ))}
    </section>
    )
}
