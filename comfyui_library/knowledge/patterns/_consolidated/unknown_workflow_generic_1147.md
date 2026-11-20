---
name: unknown_workflow_generic_1147
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.847333
common_nodes: [EmptyImage, GetImageSize, ImageCompositeMasked, LoadImage, LongCatImageEdit, LongCatImageModelLoader, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/longcat-image-advanced-edit-图像编辑_2000840598707990530.json, 图片生成/文生图/longcat-image-advanced-edit_1998416916836442114.json, 平台全量/一圈即没：Longcat 智能物体移除工作流_2002054007961055234.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1147

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/longcat-image-advanced-edit-图像编辑_2000840598707990530.json、图片生成/文生图/longcat-image-advanced-edit_1998416916836442114.json、平台全量/一圈即没：Longcat 智能物体移除工作流_2002054007961055234.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `EmptyImage`
- `GetImageSize`
- `ImageCompositeMasked`
- `LoadImage`
- `LongCatImageEdit`
- `LongCatImageModelLoader`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
