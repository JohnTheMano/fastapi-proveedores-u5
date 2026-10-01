import { Navbar } from './components/Navbar'
import { ProductoList } from './components/ProductoList'
import { ProductoForm } from './components/ProductoForm'
import { Footer } from './components/Footer'
import type { Producto } from './types/producto'

const productos: Producto[] = [
  {
    id: 1,
    nombre: 'Silla de Oficina',
    descripcion: 'Silla ergonómica para oficina con respaldo acolchado.',
    precio: 150.5,
  },
  {
    id: 2,
    nombre: 'Mesa de Oficina',
    descripcion: 'Mesa amplia y resistente para espacios de trabajo.',
    precio: 250.5,
  },
  {
    id: 3,
    nombre: 'Escritorio Ejecutivo',
    descripcion: 'Escritorio moderno con amplio espacio de trabajo.',
    precio: 420.0,
  },
]

export const App = () => {
  return (
    <div className="flex min-h-screen flex-col bg-gray-100">
      <Navbar />

      <main className="mx-auto w-full max-w-6xl flex-1 px-6 py-10">
        <header className="mb-10">
          <h2 className="text-4xl font-extrabold text-gray-900">
            Catálogo de productos
          </h2>

          <p className="mt-2 text-lg text-gray-600">
            Productos disponibles en Food Store
          </p>
        </header>

        <div className="mb-10">
          <ProductoList productos={productos} />
        </div>

        <div className="mx-auto max-w-2xl">
          <ProductoForm />
        </div>
      </main>

      <Footer />
    </div>
  )
}
