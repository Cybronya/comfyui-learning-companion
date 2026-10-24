---
name: unknown_workflow_generic_633
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.904
common_nodes: [InspyrenetRembgAdvanced, JoinImageWithAlpha, LayerMask: BenUltra, LayerMask: BiRefNetUltraV2, LayerMask: LoadBenModel, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview+, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/5种主流抠图工具联用（1次5图选1）_1952199306679930881.json, 图片生成/图生图/6种主流抠图工具联用V2（1次6图选1，含SDmatte）_1956211154316132354.json, 图片生成/图生图/多种抠图工具_1952572230473584641.json, 图片生成/图生图/🦖最新多合一抠图工具_1893862736365813762.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_633

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/5种主流抠图工具联用（1次5图选1）_1952199306679930881.json、图片生成/图生图/6种主流抠图工具联用V2（1次6图选1，含SDmatte）_1956211154316132354.json、图片生成/图生图/多种抠图工具_1952572230473584641.json、图片生成/图生图/🦖最新多合一抠图工具_1893862736365813762.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `InspyrenetRembgAdvanced`
- `JoinImageWithAlpha`
- `LayerMask: BenUltra`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBenModel`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview+`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `InvertMask` —— 3/4 个有
- `Mask Batch` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ResizeMask` —— 3/4 个有
- `easy imageSize` —— 3/4 个有
- `BackgroundEraseNetwork` —— 2/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/4 个有
- `Mask Invert` —— 2/4 个有
- `SDMatteApply` —— 2/4 个有
- `ImageConcanate` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
