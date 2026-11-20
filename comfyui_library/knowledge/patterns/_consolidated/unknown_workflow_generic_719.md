---
name: unknown_workflow_generic_719
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7688
common_nodes: [CompressImages, ImageListToBatch_, PreviewImage, RHUploadZip_V2, RMBG]
problems: []
missing: []
members: [图片生成/图生图/批量移除背景 （Zip解压包批量）_1997837693189033985.json, 平台全量/Zip V2 批量移除背景_1996552604920455169.json, 平台全量/zip-大批量抠图_2001650164072869889.json, 平台全量/批量抠图-全部打包zip_2001179255985799169.json, 平台全量/批量抠图-全部打包zip_2092457115368644610.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_719

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/批量移除背景 （Zip解压包批量）_1997837693189033985.json、平台全量/Zip V2 批量移除背景_1996552604920455169.json、平台全量/zip-大批量抠图_2001650164072869889.json、平台全量/批量抠图-全部打包zip_2001179255985799169.json、平台全量/批量抠图-全部打包zip_2092457115368644610.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CompressImages`
- `ImageListToBatch_`
- `PreviewImage`
- `RHUploadZip_V2`
- `RMBG`

**可变部分**（部分 workflow 才有）：
- `MaskToImage` —— 2/5 个有
- `LoadImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
