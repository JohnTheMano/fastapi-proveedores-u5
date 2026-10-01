
Food Store — Frontend
Frontend del Trabajo Práctico Integrador de Programación IV.

La aplicación fue desarrollada utilizando React + TypeScript + Vite + Tailwind CSS, aplicando componentización, tipado estático y una estructura organizada por responsabilidades.

Tecnologías utilizadas
React

TypeScript

Vite

Tailwind CSS 4

pnpm

Estructura del proyecto
frontend/
├── public/
├── src/
│   ├── components/
│   │   ├── Navbar.tsx
│   │   ├── ProductoCard.tsx
│   │   ├── ProductoList.tsx
│   │   ├── ProductoForm.tsx
│   │   └── Footer.tsx
│   │
│   ├── types/
│   │   └── producto.ts
│   │
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css
│
├── package.json
├── vite.config.ts
├── tsconfig.json
└── README.md

Componentes
Navbar
Barra superior de navegación que muestra el nombre de la aplicación.

ProductoCard
Representa individualmente un producto y muestra sus datos mediante props tipadas.

ProductoList
Recibe un arreglo de productos mediante props y genera múltiples componentes ProductoCard.

ProductoForm
Formulario visual para el alta de productos. No posee funcionalidad ni manejo de estado, ya que el objetivo del trabajo es realizar únicamente el maquetado.

Footer
Pie de página de la aplicación.

Tipado
El tipo Producto se encuentra definido en:

src/types/producto.ts

Los productos utilizados en la pantalla se encuentran hardcodeados en App.tsx y están tipados como Producto[].

Tailwind CSS
Los estilos de la interfaz se implementan utilizando clases utilitarias de Tailwind CSS directamente en los componentes JSX.

Se utilizan clases para:

Colores.

Espaciado.

Tipografía.

Bordes.

Sombras.

Flexbox.

Grid.

Diseño responsive.

Componentes puros
Los componentes del proyecto son funciones y no utilizan hooks de React.

No se utilizan:

useState

useEffect

Llamadas a API.

Manejo de estado.

any.

Los datos se pasan mediante props tipadas.

Instalación
Desde la carpeta frontend:

pnpm install

Ejecución
Para iniciar el servidor de desarrollo:

pnpm dev

La aplicación estará disponible en:

http://localhost:5173

Objetivo
El objetivo de este frontend es maquetar una pantalla de productos para el proyecto Food Store, aplicando React, TypeScript, Tailwind CSS y buenas prácticas de componentización.