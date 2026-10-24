---
name: unknown_workflow_generic_273
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.77525
common_nodes: [LoadImage, LoadOmniGen2Model, OmniGen2, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/OmniGen2--一键手办生成_1937084348833370113.json, 图片生成/图生图/OmniGen2--图像编辑和motion控制_1937080503122169858.json, 图片生成/图生图/OmniGen2--换装(测试不稳定)_1937080466665279490.json, 图片生成/图生图/Omnigen2电商美女拿包_1936684455555928065.json, 图片生成/图生图/Omnigen2角色一致性同框_1936636241985310722.json, 图片生成/图生图/【遇见AI】OmniGen2多模态模型_2041819478459162626.json, 图片生成/图生图/最新Omnigen2 多图融合｜电商海报_1936708941567135745.json, 图片生成/文生图/OmniGen2--线稿(测试)_1937073804357062657.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_273

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/OmniGen2--一键手办生成_1937084348833370113.json、图片生成/图生图/OmniGen2--图像编辑和motion控制_1937080503122169858.json、图片生成/图生图/OmniGen2--换装(测试不稳定)_1937080466665279490.json、图片生成/图生图/Omnigen2电商美女拿包_1936684455555928065.json、图片生成/图生图/Omnigen2角色一致性同框_1936636241985310722.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `LoadImage`
- `LoadOmniGen2Model`
- `OmniGen2`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/8 个有
- `ImageConcanate` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `Text` —— 4/8 个有
- `PrimitiveString` —— 3/8 个有
- `BiRefNet_Hugo` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
