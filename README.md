# hexagonal-architecture-python

The main goal is to structure a clean and maintainable architecture by separating core business logic from external concerns (such as databases, APIs, or user interfaces). This approach improves testability, flexibility, and adaptability to future changes.

The planned use case is a **gym management system**, which will include features such as:

- **Gym Clients**: register, update, archive, and export client data to cloud storage (e.g., S3 or Dropbox).
- **Gym Passes**: handle lifecycle operations like creation, pause, renewal, and status validation.
- **Gym Classes**: support full CRUD operations, organized by schedule.

As development progresses, the focus will be on applying clean code principles and showcasing a real-world example of hexagonal architecture in Python.
