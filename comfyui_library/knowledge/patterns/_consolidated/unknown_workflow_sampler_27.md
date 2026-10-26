---
name: unknown_workflow_sampler_27
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6912
common_nodes: [ACE_ImageFaceCrop, BiRefNetRMBG, CR Prompt Text, ImageConcanate, LoadImage, PDIMAGE_LongerSize, PMRF, RunningHub XVerse Pipeline Loader, RunningHub XVerse Sampler, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Xverse一句话双图融合_1944016705532100610.json, 图片生成/图生图/Xverse单人一致性250714_1944539618484080642.json, 图片生成/图生图/Xverse单人物品强一致性互动V1_1943889529516462082.json, 图片生成/图生图/Xverse双人一致性_1944286736124088321.json, 图片生成/图生图/最强双人一致性互动编辑Xverse（T8优化版）V1_1943887486902763522.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_27

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Xverse一句话双图融合_1944016705532100610.json、图片生成/图生图/Xverse单人一致性250714_1944539618484080642.json、图片生成/图生图/Xverse单人物品强一致性互动V1_1943889529516462082.json、图片生成/图生图/Xverse双人一致性_1944286736124088321.json、图片生成/图生图/最强双人一致性互动编辑Xverse（T8优化版）V1_1943887486902763522.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `ACE_ImageFaceCrop`
- `BiRefNetRMBG`
- `CR Prompt Text`
- `ImageConcanate`
- `LoadImage`
- `PDIMAGE_LongerSize`
- `PMRF`
- `RunningHub XVerse Pipeline Loader`
- `RunningHub XVerse Sampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `SetNode` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
