# Symbiote Research Planning

## Storage and Data Plane

The initial focus of the Symbiote research program will be targeting data storage, data bases, and data infrastructure.  The target is to flesh out a core method for managing and working with the data that Symbiote needs to function properly.

### Considerations
- File System:
This is where Symbiote stores the actual files - images, videos, and documents. The filesystem management needs to be capable of running on the Symbiote Pod architecture as well as core cloud infrastructure for Pod backups, retrieval and model fine-tuning.

- Document Database:
For storing file metadata, queries, and other structured and semi-structured data, a document-oriented NoSQL database would be a good fit. MongoDB is a popular choice for this kind of use case because it's designed to store, process, and query large amounts of data in various formats, and it's highly scalable.

- Data Processing and Analysis:
For processing and analyzing the data, you might consider a data processing framework like Apache Spark or Hadoop MapReduce. These are designed to handle large amounts of data and can process complex computations across distributed systems.

- Data Ingestion and Stream Processing:
If you're dealing with real-time or near-real-time data, tools like Apache Kafka or Google Cloud Pub/Sub can be used to ingest and process this data in a timely manner.

- Data Governance and Security:
Given the personal nature of the data being stored, it's crucial to consider data governance and security from the outset. This includes encryption at rest and in transit, access controls, and compliance with relevant regulations.

### Data Types
- Images: jpeg, gif, HEIC, png, bmp, tiff, raw, Webp, svg, heif, ico, psd, etc...
- Video: mp4, mov, avi, wmv, flv, mkv webm, avchd, mpeg-2, 3gp, etc...
- Audio: mp3, wav, aac, flac, ogg, m4a, wma
- Document:
    -- unstructured: pdf, doc/docx, ppt/pptx, txt, rtf, odt
    -- structured: json, html, xml, csv, toml, markdown, yaml
- 3D modeling: stl, obj, fbx 3ds, dae, ply, gltf/glb, step, iges, dxf, gcode
- Database: sql, db, mdb, accdb, dbf
- Archival: zip, rar, tar, gz, 7z

#### Data Type Considerations
Text Files (.txt, .log, .md, .rtf): These are basic file types that contain unformatted text. They are very common and can contain anything from user notes to system logs.

Database Files (.sql, .db, .mdb, .accdb, .dbf): These files are used by various database systems like MySQL, SQLite, Microsoft Access, and others.

Archives (.zip, .rar, .tar, .gz, .7z): Archives can contain multiple files and directories. They can also be compressed to save space.

eBooks (.epub, .mobi, .pdf): If Symbiote is going to be used for personal data, eBooks might very well be part of that data.

Spreadsheet Files (.xls, .xlsx, .ods, .csv): Excel and other spreadsheet files are common for data storage and analysis.

Presentation Files (.ppt, .pptx, .odp): PowerPoint and other presentation files can be important, especially in a business context.

Email Files (.eml, .msg): These files are commonly used to store individual emails.

Calendar and Contact Files (.ics, .vcf): These file types are commonly used for storing calendar events and contact information.

HTML and XML Files (.html, .htm, .xml, .json): These files are primarily used in web development but are also used for configuration and data storage.

Script and Programming Files (.py, .js, .php, .java, .c, .cpp, .h, .sh): If Symbiote is going to be used by developers or in a development environment, handling these file types might be beneficial.

Executable and Binary Files (.exe, .bin, .app, .dll): While it's less likely that Symbiote would need to analyze these types of files, it may still need to manage and catalog them.

CAD Files (.dwg, .dxf): These are used for 2D and 3D drawings in industries like architecture and engineering.

### Infrastructure Considerations

#### Symbiote POD
Storage: High-capacity, high-speed storage will be required for housing all the user's personal data. Solid State Drives (SSDs) are a good option due to their speed, but they can be expensive for high-capacity drives. Hard Disk Drives (HDDs) are slower but cheaper and could be used for older or less frequently accessed data.

Processing Power: The Pod will need to perform a lot of data processing, from indexing new files to running complex AI models. A high-performance CPU, possibly with GPU acceleration for AI tasks, will be necessary.

Memory: To support processing tasks, a generous amount of RAM will be needed.

Network Interface: The Pod will need to communicate with the Symbiote Infrastructure regularly. A high-speed, reliable network interface is required.

Operating System: Linux, BSD*, RedoxOS 

Security: Both physical and digital security measures will be needed to protect the user's data.

    -- Pod Storage Architecture
        --- Redundancy
            ---- RAID
            ---- Remote Backups

        --- Filesystem
            ---- Easily grown

        --- Data Management
            ---- Deduplication

        --- Data CRUD
            ---- API Access
            ---- Browsing Capabilities

        --- Security

#### Symbiote Cloud
Storage: High-capacity, distributed storage systems will be needed to store user data, backups, and AI models.

Processing Power: Large-scale data processing tasks, such as training AI models, will need to be performed in the cloud. High-performance processing power, likely with GPU acceleration, will be necessary.

Network: A high-speed, reliable network infrastructure is needed to handle communication between Pods and the infrastructure.

Security: Robust security measures, including encryption at rest and in transit, intrusion detection systems, and regular security audits, are necessary to protect user data.

Scalability: The infrastructure should be designed to scale smoothly as more Pods and users are added.

Datacenters: Depending on the size and scope of Symbiote, multiple data centers may be necessary for redundancy, load balancing, and to ensure fast and reliable access for users around the world.

Software Stack: The software stack should be robust, secure, and capable of handling the complex tasks required by Symbiote. This would likely involve a range of technologies, from databases to AI libraries to web servers.

Monitoring and Alerting: A comprehensive monitoring and alerting system is needed to ensure the smooth operation of the infrastructure and to quickly detect and address any issues.

    -- Cloud Storage Architecture
        --- Filesystem
            ---- Clustered Filesystems
                ----- HadoopFS
                ----- GlusterFS

        --- Redundancy
            ---- RAID
            ---- Regional 

        --- Databases
            ---- Haddop
            ---- ElasticSearch
            ---- MongoDB
            ---- ...

        --- Data Management
            ---- Symbiote partitioning: Ensure Symbiotes are cordened off from one another when active processing takes place.
            ---- Deduplication

        --- Data CRUD
            ---- API Access

        --- Security


