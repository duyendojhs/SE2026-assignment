#!/usr/bin/env python3
"""
Generate simple fallback placeholder diagrams using PIL.
Minimal dependencies for guaranteed compilation success.
"""
try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

from pathlib import Path

ASSETS_DIR = Path(__file__).parent
WIDTH, HEIGHT = 1200, 800
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (31, 41, 55)


def create_fallback_image(filename, title, content_lines):
    """Create a simple fallback diagram with title and content"""
    if PIL_AVAILABLE:
        img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(img)

        # Try to use a system font, fall back to default
        try:
            title_font = ImageFont.truetype("arial.ttf", 36)
            content_font = ImageFont.truetype("arial.ttf", 24)
        except:
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()

        # Draw title
        draw.text((WIDTH//2, 80), title, fill=TEXT_COLOR, font=title_font, anchor="mm")

        # Draw content
        y_offset = 200
        for line in content_lines:
            draw.text((WIDTH//2, y_offset), line, fill=TEXT_COLOR, font=content_font, anchor="mm")
            y_offset += 60

        # Draw border
        draw.rectangle([10, 10, WIDTH-10, HEIGHT-10], outline=(100, 116, 139), width=3)

        img.save(ASSETS_DIR / filename)
        print(f"✓ {filename} generated (PIL)")
    else:
        # Ultra-minimal SVG fallback
        svg_content = f'''<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="white" stroke="#64748b" stroke-width="3"/>
  <text x="{WIDTH//2}" y="80" font-size="32" font-weight="bold" text-anchor="middle" fill="#1f2937">{title}</text>
'''
        y_offset = 200
        for line in content_lines:
            svg_content += f'  <text x="{WIDTH//2}" y="{y_offset}" font-size="20" text-anchor="middle" fill="#1f2937">{line}</text>\n'
            y_offset += 50
        svg_content += '</svg>'

        # Save as SVG, convert notice
        svg_path = ASSETS_DIR / filename.replace('.png', '.svg')
        with open(svg_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✓ {filename.replace('.png', '.svg')} generated (SVG fallback - PIL not available)")


def main():
    print("Generating fallback diagrams for Variant RE-027...\n")

    # Diagram 1: Process
    create_fallback_image(
        'diagram_process.png',
        '1-Week AI-Augmented Software Process',
        [
            'Days 1-7: Inception → Behavioral Spec → Quality Scenarios → Risk → Implementation → Traceability → Certification',
            'GATE-01 through GATE-05: Quality checkpoints at each phase',
            'Inner Loop (Hours): AI Draft → Lint → Test → Human Gate',
            'Outer Loop (Days): Load Test → Compliance → SLA Drill → Certification',
            'Variant RE-027: 302 concurrent users | 41-day retention | 20-hour SLA'
        ]
    )

    # Diagram 2: Architecture
    create_fallback_image(
        'diagram_architecture.png',
        'Architectural Separation: Identity vs Audit Store',
        [
            'Primary Identity Store → Purged under Personal-Data-Deletion-on-Request',
            'Irreversible Tokenization (Surrogate Keys)',
            'Audit Log Store → Retained for 41 days with pseudonymized records',
            'Day 42 automated purge enforces retention limit',
            'CONFLICT-01 Resolution: Audit traceability vs PII elimination'
        ]
    )

    # Diagram 3: Sequence
    create_fallback_image(
        'diagram_sequence.png',
        'UML Sequence: Concurrent Privilege Revocation (302 Users)',
        [
            'Access Admin → Deletion Queue → Identity Store → Audit Log → Session Manager → Escalation',
            'Flow: Submit request (hour 19.5) → Query PII → Revoke sessions (302 concurrent)',
            '→ Tokenize PII (irreversible) → Write audit event → Purge identity store',
            'Failure: Request ages past 20h → SLA breach alert → Escalation to Admin + DPO',
            'AC-03.2: Race condition boundary under peak load with policy re-evaluation'
        ]
    )

    # Diagram 4: Conflicts
    create_fallback_image(
        'diagram_conflicts.png',
        'Stakeholder Tension Grid (Variant RE-027)',
        [
            '4 Stakeholders: Access Administrator (Focus) | Data Subject | SecOps & Auditor | DPO',
            'CONFLICT-01: 41-day audit retention vs zero direct PII exposure',
            'CONFLICT-02: 20-hour SLA vs 302 concurrent load processing',
            'CONFLICT-03: Instant access revocation vs audit logging latency',
            'Resolution: OUTCOME-01 (100% ≤20h) | OUTCOME-02 (41-day, 0% PII) | OUTCOME-03 (<0.1% error @302)'
        ]
    )

    print("\n✓ All 4 fallback diagrams generated successfully")
    return 0


if __name__ == '__main__':
    exit(main())
