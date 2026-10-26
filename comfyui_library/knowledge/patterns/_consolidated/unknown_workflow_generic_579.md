---
name: unknown_workflow_generic_579
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8196
common_nodes: [LoadImage, SaveImage, TransparentImage]
problems: []
missing: []
members: [图片生成/图生图/一键抠图获取透明图像_2003072026501873666.json, 图片生成/图生图/一键抠图获取透明图像_2006620350502674434.json, 图片生成/图生图/一键抠图获取透明图像（Segment+anything语义分割）_1990626347234070530.json, 图片生成/图生图/语义分割任何元素+黑白背景SegmentAnything+全节点注释_2056026873137778690.json, 图片生成/图生图/透明_2068898137724514305.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_579

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键抠图获取透明图像_2003072026501873666.json、图片生成/图生图/一键抠图获取透明图像_2006620350502674434.json、图片生成/图生图/一键抠图获取透明图像（Segment+anything语义分割）_1990626347234070530.json、图片生成/图生图/语义分割任何元素+黑白背景SegmentAnything+全节点注释_2056026873137778690.json、图片生成/图生图/透明_2068898137724514305.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `TransparentImage`

**可变部分**（部分 workflow 才有）：
- `GroundingDinoModelLoader (segment anything)` —— 4/5 个有
- `GroundingDinoSAMSegment (segment anything)` —— 4/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 4/5 个有
- `MaskToImage` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `SAMLoader` —— 4/5 个有
- `RHHiddenNodes` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
