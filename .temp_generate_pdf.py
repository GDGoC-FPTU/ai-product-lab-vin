from pathlib import Path

lines = [
    'Bước 1: Cư dân gửi ticket lên App',
    'Bước 2: Nhân sự BQL nhận ticket  (🔄 Handoff: App -> Nhân sự)',
    'Bước 3: Nhân sự đọc nội dung text/hình ảnh  (🔴 Bottleneck)',
    'Bước 4: Nhân sự gắn tag phân loại sự cố  (🔴 Bottleneck)',
    'Bước 5: Nhân sự xác định tòa nhà, vị trí, mức độ ưu tiên  (🔴 Bottleneck)',
    'Bước 6: Nhân sự tạo lệnh điều phối trên hệ thống  (🔄 Handoff: Nhân sự -> Hệ thống)',
    'Bước 7: Kỹ thuật viên thực địa nhận việc  (🔄 Handoff: Hệ thống -> Kỹ thuật viên)',
    'Tổng cộng = 15 phút/lượt'
]

content = 'BT\n/F1 12 Tf\n72 760 Td\n'
for i, line in enumerate(lines):
    escaped = line.replace('(', '\(').replace(')', '\)')
    content += f'({escaped}) Tj\n'
    if i < len(lines) - 1:
        content += '0 -16 Td\n'
content += 'ET\n'

obj = []
obj.append(b'%PDF-1.1\n')
obj.append(b'1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n')
obj.append(b'2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n')
stream = content.encode('latin1')
obj.append(b'3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n')
obj.append(f'4 0 obj\n<< /Length {len(stream)} >>\nstream\n'.encode('latin1') + stream + b'endstream\nendobj\n')
obj.append(b'5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n')

byte_pos = 0
xref = b'xref\n0 6\n0000000000 65535 f \n'
for o in obj:
    xref += f'{byte_pos:010d} 00000 n \n'.encode('latin1')
    byte_pos += len(o)

trailer = b'trailer << /Root 1 0 R /Size 6 >>\nstartxref\n' + str(byte_pos).encode('latin1') + b'\n%%EOF\n'

path = Path('04-workflow-diagram.pdf')
with path.open('wb') as f:
    for o in obj:
        f.write(o)
    f.write(xref)
    f.write(trailer)
print(f'Created {path.resolve()}')
