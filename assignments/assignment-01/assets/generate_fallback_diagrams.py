#!/usr/bin/env python3
"""
Generate fallback placeholder diagrams for Assignment 01, Variant RE-027.
These serve as safe defaults if Kroki API rendering fails or times out.
"""
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

# Output directory
ASSETS_DIR = Path(__file__).parent

def create_process_diagram():
    """diagram_process.png: 1-Week AI-Augmented Lifecycle"""
    fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(5, 7.5, '1-Week AI-Augmented Software Process (Days 1-7)',
            ha='center', va='top', fontsize=14, fontweight='bold')

    # Days and Gates
    days = [
        ("Day 1\nInception", "GATE-01\nFraming"),
        ("Day 2\nBehavioral Spec", "GATE-02\nBoundary"),
        ("Day 3\nQuality Scenarios", "GATE-03\nArchitecture"),
        ("Day 4\nRisk Analysis", ""),
        ("Day 5\nImplementation", "GATE-04\nSecurity"),
        ("Day 6\nTraceability", "GATE-05\nClosure"),
        ("Day 7\nCertification", "GATE-05\n(Final)")
    ]

    y_pos = 6
    for i, (day, gate) in enumerate(days):
        x = 1 + i * 1.3
        # Day box
        rect = patches.FancyBboxPatch((x-0.5, y_pos-0.3), 1, 0.6,
                                       boxstyle="round,pad=0.05",
                                       edgecolor='#2563eb', facecolor='#dbeafe', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y_pos, day, ha='center', va='center', fontsize=8, fontweight='bold')

        # Gate
        if gate:
            gate_rect = patches.FancyBboxPatch((x-0.4, y_pos-1.2), 0.8, 0.5,
                                                boxstyle="round,pad=0.03",
                                                edgecolor='#dc2626', facecolor='#fee2e2', linewidth=1.5)
            ax.add_patch(gate_rect)
            ax.text(x, y_pos-0.95, gate, ha='center', va='center', fontsize=7)

        # Arrow
        if i < len(days) - 1:
            ax.arrow(x+0.5, y_pos, 0.25, 0, head_width=0.15, head_length=0.1,
                     fc='#64748b', ec='#64748b', linewidth=1.5)

    # Verification Loops
    ax.text(5, 4.5, 'Inner Verification Loop (Hours): AI Draft → Lint → Test → Human Gate',
            ha='center', va='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='#fef3c7', alpha=0.8))
    ax.text(5, 3.8, 'Outer Stakeholder Loop (Days): Load Test → Compliance Review → SLA Drill → Certification',
            ha='center', va='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='#d1fae5', alpha=0.8))

    # Variant parameters
    ax.text(5, 2.5, 'Variant RE-027 Constraints:', ha='center', va='top',
            fontsize=10, fontweight='bold')
    ax.text(5, 2, '302 concurrent users | 41-day retention | 20-hour SLA window',
            ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='#e5e7eb', alpha=0.9))

    # Trade-offs
    ax.text(1, 1, 'Trade-off 1: Velocity vs Verification Depth → Verification wins',
            ha='left', va='center', fontsize=7)
    ax.text(1, 0.5, 'Trade-off 2: Automation vs Human Gates → Human gates win',
            ha='left', va='center', fontsize=7)
    ax.text(1, 0, 'Trade-off 3: Agile Flexibility vs Rigid SLA → Rigid SLA wins',
            ha='left', va='center', fontsize=7)

    plt.tight_layout()
    plt.savefig(ASSETS_DIR / 'diagram_process.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ diagram_process.png generated")


def create_architecture_diagram():
    """diagram_architecture.png: Identity Store separation from Audit Log Store"""
    fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(5, 7.5, 'Architectural Separation: Identity vs Audit Store',
            ha='center', va='top', fontsize=14, fontweight='bold')

    # Identity Store (LEFT - Purged under deletion policy)
    identity_box = patches.FancyBboxPatch((0.5, 4), 3.5, 2.5,
                                           boxstyle="round,pad=0.1",
                                           edgecolor='#dc2626', facecolor='#fee2e2', linewidth=3)
    ax.add_patch(identity_box)
    ax.text(2.25, 6.2, 'Primary Identity Store', ha='center', va='top',
            fontsize=11, fontweight='bold', color='#991b1b')
    ax.text(2.25, 5.8, '(Purged under Personal-Data-', ha='center', va='top', fontsize=9)
    ax.text(2.25, 5.5, 'Deletion-on-Request)', ha='center', va='top', fontsize=9)
    ax.text(2.25, 5, '• Direct PII', ha='left', va='top', fontsize=8, x=1)
    ax.text(2.25, 4.7, '• User profiles', ha='left', va='top', fontsize=8, x=1)
    ax.text(2.25, 4.4, '• Session tokens', ha='left', va='top', fontsize=8, x=1)

    # Deletion Arrow
    ax.annotate('', xy=(2.25, 3.5), xytext=(2.25, 4),
                arrowprops=dict(arrowstyle='->', lw=3, color='#dc2626'))
    ax.text(2.25, 3.3, 'DELETION\nRequest triggers\nirreversible purge',
            ha='center', va='top', fontsize=8, fontweight='bold', color='#dc2626')

    # Audit Log Store (RIGHT - Retained with pseudonymized surrogates)
    audit_box = patches.FancyBboxPatch((6, 4), 3.5, 2.5,
                                        boxstyle="round,pad=0.1",
                                        edgecolor='#2563eb', facecolor='#dbeafe', linewidth=3)
    ax.add_patch(audit_box)
    ax.text(7.75, 6.2, 'Audit Log Store', ha='center', va='top',
            fontsize=11, fontweight='bold', color='#1e40af')
    ax.text(7.75, 5.8, '(Retained for 41 days with', ha='center', va='top', fontsize=9)
    ax.text(7.75, 5.5, 'pseudonymized surrogates)', ha='center', va='top', fontsize=9)
    ax.text(7.75, 5, '• Surrogate tokens', ha='left', va='top', fontsize=8, x=6.5)
    ax.text(7.75, 4.7, '• Access events', ha='left', va='top', fontsize=8, x=6.5)
    ax.text(7.75, 4.4, '• Timestamps', ha='left', va='top', fontsize=8, x=6.5)

    # Retention Arrow
    ax.annotate('', xy=(7.75, 3.5), xytext=(7.75, 4),
                arrowprops=dict(arrowstyle='->', lw=3, color='#2563eb'))
    ax.text(7.75, 3.3, 'RETENTION\nDay 42 purge\n(automated)',
            ha='center', va='top', fontsize=8, fontweight='bold', color='#2563eb')

    # Tokenization Flow (Middle)
    ax.annotate('', xy=(5.8, 5.25), xytext=(4.2, 5.25),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='#059669', linestyle='dashed'))
    ax.text(5, 5.6, 'Irreversible', ha='center', va='bottom', fontsize=9,
            fontweight='bold', color='#059669')
    ax.text(5, 4.9, 'Tokenization', ha='center', va='top', fontsize=9,
            fontweight='bold', color='#059669')

    # Variant parameters
    ax.text(5, 2, 'Variant RE-027: 302 concurrent users | 41-day audit retention | 20-hour response window',
            ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='#e5e7eb', alpha=0.9))

    # Key principle
    ax.text(5, 1, 'CONFLICT-01 Resolution: Audit traceability preserved via surrogate keys while direct PII eliminated',
            ha='center', va='center', fontsize=8, style='italic',
            bbox=dict(boxstyle='round', facecolor='#fef3c7', alpha=0.8))

    plt.tight_layout()
    plt.savefig(ASSETS_DIR / 'diagram_architecture.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ diagram_architecture.png generated")


def create_sequence_diagram():
    """diagram_sequence.png: Concurrent privilege revocation under peak load"""
    fig, ax = plt.subplots(figsize=(12, 10), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Title
    ax.text(5, 11.5, 'UML Sequence: Concurrent Privilege Revocation Under Peak Load (302 Users)',
            ha='center', va='top', fontsize=13, fontweight='bold')

    # Actors
    actors = [
        ("Access\nAdmin", 1.5),
        ("Deletion\nQueue", 3),
        ("Identity\nStore", 4.5),
        ("Audit\nLog", 6),
        ("Session\nManager", 7.5),
        ("Escalation\nSubsystem", 9)
    ]

    for name, x in actors:
        # Actor box
        rect = patches.FancyBboxPatch((x-0.4, 10.5), 0.8, 0.6,
                                       boxstyle="round,pad=0.05",
                                       edgecolor='#374151', facecolor='#f3f4f6', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, 10.8, name, ha='center', va='center', fontsize=8, fontweight='bold')

        # Lifeline
        ax.plot([x, x], [10.5, 0.5], 'k--', linewidth=1, alpha=0.5)

    # Sequence flow
    y = 9.8
    sequences = [
        (1.5, 3, "1: Submit bulk\ndeletion request\n(hour 19.5)", y),
        (3, 4.5, "2: Query target\nuser PII", y-0.8),
        (4.5, 3, "3: Return user\nrecord + active\nsessions", y-1.6),
        (3, 7.5, "4: Revoke all\nactive sessions\n(302 concurrent)", y-2.4),
        (7.5, 3, "5: Confirm\nrevocation\n(atomic)", y-3.2),
        (3, 4.5, "6: Tokenize PII\n(irreversible)", y-4),
        (4.5, 6, "7: Write audit\nevent with\nsurrogate key", y-4.8),
        (6, 4.5, "8: Purge direct\nPII from\nidentity store", y-5.6),
        (4.5, 3, "9: Confirm\ndeletion\ncomplete", y-6.4),
        (3, 1.5, "10: Return\nfulfillment\n(within 20h)", y-7.2),
    ]

    for x1, x2, label, y_pos in sequences:
        ax.annotate('', xy=(x2, y_pos), xytext=(x1, y_pos),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color='#2563eb'))
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, y_pos + 0.15, label, ha='center', va='bottom', fontsize=7)

    # Failure scenario
    y_fail = y - 8
    ax.text(5, y_fail, 'Failure Scenario: Request ages past 20h due to deadlock',
            ha='center', va='top', fontsize=9, fontweight='bold', color='#dc2626')
    ax.annotate('', xy=(9, y_fail-0.5), xytext=(3, y_fail-0.5),
                arrowprops=dict(arrowstyle='->', lw=2, color='#dc2626', linestyle='dashed'))
    ax.text(6, y_fail-0.35, '11: Emit SLA breach alert + escalation',
            ha='center', va='bottom', fontsize=7, color='#dc2626', fontweight='bold')
    ax.annotate('', xy=(1.5, y_fail-1), xytext=(9, y_fail-1),
                arrowprops=dict(arrowstyle='->', lw=2, color='#dc2626', linestyle='dashed'))
    ax.text(5.25, y_fail-0.85, '12: Notify Admin + DPO with root cause',
            ha='center', va='bottom', fontsize=7, color='#dc2626', fontweight='bold')

    plt.tight_layout()
    plt.savefig(ASSETS_DIR / 'diagram_sequence.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ diagram_sequence.png generated")


def create_conflicts_diagram():
    """diagram_conflicts.png: Stakeholder Tension Grid"""
    fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(5, 9.5, 'Stakeholder Tension Grid (Variant RE-027)',
            ha='center', va='top', fontsize=14, fontweight='bold')

    # Stakeholders (4 corners)
    stakeholders = [
        ("Access\nAdministrator\n(Focus)", 1.5, 7.5, '#2563eb', '#dbeafe'),
        ("Data Subject /\nEnd User", 8.5, 7.5, '#7c3aed', '#ede9fe'),
        ("SecOps &\nCompliance\nAuditor", 1.5, 2.5, '#059669', '#d1fae5'),
        ("DPO / Legal\nCounsel", 8.5, 2.5, '#dc2626', '#fee2e2'),
    ]

    for name, x, y, edge_color, face_color in stakeholders:
        circle = patches.Circle((x, y), 0.8, edgecolor=edge_color,
                                facecolor=face_color, linewidth=3)
        ax.add_patch(circle)
        ax.text(x, y, name, ha='center', va='center', fontsize=9, fontweight='bold')

    # Conflicts (connecting lines with labels)
    conflicts = [
        (1.5, 2.5, 8.5, 2.5, "CONFLICT-01\n41-day audit retention vs\nzero direct PII exposure", 5, 1.8, '#dc2626'),
        (1.5, 7.5, 8.5, 7.5, "CONFLICT-02\n20-hour SLA vs\n302 concurrent load", 5, 8.2, '#ea580c'),
        (1.5, 7.5, 1.5, 2.5, "CONFLICT-03\nInstant revocation vs\naudit logging latency", 0.2, 5, '#7c3aed'),
    ]

    for x1, y1, x2, y2, label, lx, ly, color in conflicts:
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=2.5, linestyle='--', alpha=0.7)
        ax.text(lx, ly, label, ha='center', va='center', fontsize=8,
                bbox=dict(boxstyle='round', facecolor='white', edgecolor=color, linewidth=1.5))

    # Outcomes (center)
    outcomes_box = patches.FancyBboxPatch((3.5, 4.2), 3, 1.6,
                                           boxstyle="round,pad=0.1",
                                           edgecolor='#64748b', facecolor='#f1f5f9', linewidth=2)
    ax.add_patch(outcomes_box)
    ax.text(5, 5.5, 'Measurable Outcomes', ha='center', va='top',
            fontsize=10, fontweight='bold')
    ax.text(5, 5.1, 'OUTCOME-01: 100% requests ≤ 20h', ha='center', va='top', fontsize=7)
    ax.text(5, 4.8, 'OUTCOME-02: 100% compliance, 41-day, 0% PII', ha='center', va='top', fontsize=7)
    ax.text(5, 4.5, 'OUTCOME-03: Error rate < 0.1% @ 302 users', ha='center', va='top', fontsize=7)

    # Variant parameters
    ax.text(5, 0.8, 'Variant Parameters: 302 concurrent users | 41-day retention | 20-hour response window',
            ha='center', va='center', fontsize=8,
            bbox=dict(boxstyle='round', facecolor='#e5e7eb', alpha=0.9))

    plt.tight_layout()
    plt.savefig(ASSETS_DIR / 'diagram_conflicts.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ diagram_conflicts.png generated")


if __name__ == '__main__':
    print("Generating fallback diagrams for Variant RE-027...")
    create_process_diagram()
    create_architecture_diagram()
    create_sequence_diagram()
    create_conflicts_diagram()
    print("\n✓ All 4 fallback diagrams generated successfully in assets/")
