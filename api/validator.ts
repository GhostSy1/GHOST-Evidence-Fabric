export interface EvidenceRecord {
    id: string;
    asset: string;
    findingType: string;
    riskScore: number;
    riskLevel: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
    integrityHash: string;
    timestamp: string;
}

export function validateRecord(record: any): boolean {
    return typeof record.asset === 'string' &&
           typeof record.riskScore === 'number' &&
           ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW'].includes(record.riskLevel);
}
