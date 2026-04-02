# API Documentation

This document outlines the API structure required for the dynamic content of the portfolio, including CV data and Project details.

## Base URL
`https://api.nekocorp.fr/v1` (Placeholder)

---

## 1. CV Data

Retrieves all information related to the professional profile and resume.

### Get CV Profile
`GET /cv`

**Response Body (`CVData`):**

| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | Full name of the profile |
| `role` | `string` | Professional title/role |
| `contact` | `object` | Contact information |
| `contact.email` | `string` | Professional email address |
| `contact.phone` | `string` | Contact phone number |
| `contact.linkedin` | `string` | LinkedIn profile URL |
| `contact.drivingLicense` | `string` | Driving license status/category |
| `aboutMe` | `string` | Short professional biography |
| `technicalSkills` | `array` | List of technical skill categories |
| `experience` | `array` | Professional work experience |
| `education` | `array` | Academic background |
| `projects` | `array` | Highlights of key projects (CV version) |
| `aeronautical` | `array<string>` | Aeronautical skills or certifications |
| `languages` | `array` | Languages spoken and levels |
| `interests` | `array<string>` | Personal interests and hobbies |

#### Technical Skill Category Object
```json
{
  "category": "SYSTEMS & DEVSECOPS",
  "skills": [
    { "name": "Automation", "details": "Ansible, n8n" }
  ]
}
```

#### Experience Object
```json
{
  "date": "10/2025 – 08/2026",
  "company": "TOTALENERGIES (TGITS) PAU",
  "role": "IT Process Automation Engineer"
}
```

#### Education Object
```json
{
  "date": "02/2024 – 06/2026",
  "institution": "IUT MONT DE MARSAN",
  "details": [
    "3rd Year BUT R&T specialized in Cybersecurity"
  ]
}
```

---

## 2. Projects Portfolio

Manages the list and details of portfolio projects.

### List Projects
`GET /projects`

Returns an array of project summaries for the main listing.

**Response Body (`ProjectSummary[]`):**

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | Unique identifier (slug) |
| `title` | `string` | Project name |
| `image` | `string` | URL to the project cover image |
| `link` | `string` | URL to source code (e.g., Gitea/GitHub) |
| `preview` | `string` | URL to live demo or production site |
| `status` | `string` | Current status (e.g., "Deployed", "In development") |

### Get Project Details
`GET /projects/{id}`

Returns the full details for a specific project.

**Response Body (`ProjectDetail`):**

Inherits all fields from `ProjectSummary` plus:

| Field | Type | Description |
| :--- | :--- | :--- |
| `description` | `string` | Short summary for cards |
| `fullDescription` | `string` | Detailed overview for the sidebar |
| `content` | `string` | Main body content in **Markdown** format |
| `technologies` | `array<string>` | List of technologies used |
| `date` | `string` | Year or date range of the project |

#### Example Content (Markdown)
The `content` field should support standard Markdown, including headers, lists, and blockquotes.

```markdown
# Overview
This project focuses on...

## Key Features
- Feature A
- Feature B

> "A quote about the project impact."
```

---

## Data Types Summary (TypeScript)

```typescript
export interface CVData {
  name: string;
  role: string;
  contact: {
    email: string;
    phone: string;
    linkedin: string;
    drivingLicense: string;
  };
  aboutMe: string;
  technicalSkills: Array<{
    category: string;
    skills: Array<{ name: string; details: string }>;
  }>;
  experience: Array<{ date: string; company: string; role: string }>;
  education: Array<{ date: string; institution: string; details: string[] }>;
  projects: Array<{ title: string; tasks: string[] }>;
  aeronautical: string[];
  languages: Array<{ name: string; level: string }>;
  interests: string[];
}

export interface ProjectDetail {
  id: string;
  title: string;
  image: string; // URL
  link: string;
  preview: string;
  status: string;
  description: string;
  fullDescription: string;
  content: string; // Markdown
  technologies: string[];
  date: string;
}
```

---

## 3. Current Implementation Data (Reference)

This section contains the actual mock data currently used in the frontend implementation.

### CV Mock Data
```json
{
  "name": "LÉONARD-ANTON LLOSA",
  "role": "Future Network & Security Engineer",
  "contact": {
    "email": "leonard@nekocorp.fr",
    "phone": "+33 6 62 38 65 96",
    "linkedin": "https://www.linkedin.com/in/leonard-anton-llosa/",
    "drivingLicense": "Category B - Vehicle Owner"
  },
  "aboutMe": "Passionate about complex systems, from IT to aeronautics, I maintain a dual requirement for technical proficiency and security. My background in the BUT R&T, combined with my field experience at TotalEnergies, has enabled me to master the challenges of network deployment and automation using Ansible and Docker. As a student pilot accustomed to strict procedures, I am aiming for an engineering degree to tackle the ever-evolving challenges of cybersecurity.",
  "technicalSkills": [
    {
      "category": "SYSTEMS & DEVSECOPS",
      "skills": [
        { "name": "Virtualization/Containers", "details": "Docker (Standalone, Portainer), KVM, Kasm Workspaces (Zero Trust)" },
        { "name": "Automation", "details": "Ansible, n8n (Industrial environment)" },
        { "name": "Services", "details": "Apache 2, Bind (DNS), Redis" },
        { "name": "OS", "details": "Linux (Debian/RHEL), Windows 10/11, macOS" }
      ]
    },
    {
      "category": "NETWORKS & CYBERSECURITY",
      "skills": [
        { "name": "Security", "details": "SSO (Authentik, Cisco DUO), LDAP, WAF (Cloudflare/SafeLine)" },
        { "name": "Infrastructure", "details": "Hardware deployment (Cisco, UniFi), ToIP (3CX PBX)" },
        { "name": "Databases", "details": "MariaDB, PostgreSQL" }
      ]
    },
    {
      "category": "DEVELOPMENT & SCRIPTING",
      "skills": [
        { "name": "Languages", "details": "Python, PHP, HTML5/CSS3" },
        { "name": "Scripting", "details": "Bash (Linux), Batch/PowerShell (Windows)" }
      ]
    }
  ],
  "experience": [
    {
      "date": "10/2025 – 08/2026",
      "company": "TOTALENERGIES (TGITS) PAU",
      "role": "IT Process Automation Engineer"
    },
    {
      "date": "04/2025 – 06/2025",
      "company": "TOTALENERGIES (TGITS) PAU",
      "role": "IT Process Automation Engineer"
    }
  ],
  "education": [
    {
      "date": "02/2024 – 06/2026",
      "institution": "IUT MONT DE MARSAN",
      "details": [
        "09/2025 – 06/2026: 3rd Year BUT R&T specialized in Cybersecurity",
        "09/2024 – 06/2025: 2nd Year BUT R&T specialized in Cybersecurity",
        "02/2024 – 06/2024: 1st Year BUT R&T"
      ]
    },
    {
      "date": "09/2023 – 01/2024",
      "institution": "CPGE ALBI",
      "details": ["1st Year Preparatory Class (TSI)"]
    },
    {
      "date": "2022 – 2023",
      "institution": "LYCÉE SAINT CRICQ PAU",
      "details": ["Baccalauréat STI2D specialized in Information Systems & Digital"]
    }
  ],
  "projects": [
    {
      "title": "Deployment of an IT Network (Homelab \"Nekocorp\")",
      "tasks": [
        "Analyzed and designed network architecture (router on a stick)",
        "Sizing, hardware selection, and cost study",
        "Installation and cabling of network equipment",
        "Configuration of IP, routing, NAT/PAT, and services (DHCP, DNS, RADIUS)",
        "Diagnostics, incident resolution, and security hardening (Firewall, IDS/IPS, SIEM)"
      ]
    },
    {
      "title": "Automated Watering System (Final Year High School Project)",
      "tasks": [
        "Coded in Arduino",
        "Managed using Microsoft Office and Nextcloud project management suite",
        "Weekly progress meetings followed by drafting progress reports",
        "Conducted extensive testing"
      ]
    }
  ],
  "aeronautical": [
    "Aircraft Piloting: 20h flight time (+50h on simulator) on Robin DR400",
    "LAPL Student Pilot",
    "Professional Simulator: Airbus A320"
  ],
  "languages": [
    { "name": "French", "level": "Native" },
    { "name": "English", "level": "TOEIC 940 (Full linguistic proficiency)" }
  ],
  "interests": [
    "Server, endpoint, and network management",
    "PC Gaming",
    "Automobiles & Driving",
    "Aviation",
    "Automotive electronics and mechanics",
    "Video Editing (Adobe Premiere Pro)"
  ]
}
```

