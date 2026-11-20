---
name: unknown_workflow_generic_285
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.826556
common_nodes: [InspyrenetRembgAdvanced, JoinImageWithAlpha, LayerMask: BenUltra, LayerMask: BiRefNetUltraV2, LayerMask: LoadBenModel, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/5种主流抠图工具联用（1次5图选1）_1952199306679930881.json, 图片生成/图生图/6种主流抠图工具联用V2（1次6图选1，含SDmatte）_1956211154316132354.json, 图片生成/图生图/多种抠图工具_1952572230473584641.json, 图片生成/图生图/🦖最新多合一抠图工具_1893862736365813762.json, 平台全量/6种主流抠图工具联用V2（1次6图选1，含SDmatte）_1963496972009312257.json, 平台全量/6种主流抠图工具联用V2（1次6图选1，含SDmatte）林耀_2016188185075785729.json, 平台全量/抠图V1-快速（5in1）_1956566773728464897.json, 平台全量/抠图集合_1958817515990364161.json, 平台全量/抠图集合_1960719025955385346.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_285

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/5种主流抠图工具联用（1次5图选1）_1952199306679930881.json、图片生成/图生图/6种主流抠图工具联用V2（1次6图选1，含SDmatte）_1956211154316132354.json、图片生成/图生图/多种抠图工具_1952572230473584641.json、图片生成/图生图/🦖最新多合一抠图工具_1893862736365813762.json、平台全量/6种主流抠图工具联用V2（1次6图选1，含SDmatte）_1963496972009312257.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `InspyrenetRembgAdvanced`
- `JoinImageWithAlpha`
- `LayerMask: BenUltra`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBenModel`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `InvertMask` —— 8/9 个有
- `MaskPreview+` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `ResizeMask` —— 8/9 个有
- `easy imageSize` —— 8/9 个有
- `BackgroundEraseNetwork` —— 7/9 个有
- `ImageConcanate` —— 6/9 个有
- `LayerMask: SegmentAnythingUltra V2` —— 6/9 个有
- `Mask Invert` —— 6/9 个有
- `SDMatteApply` —— 6/9 个有
- `Mask Batch` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `GetNode` —— 2/9 个有
- `Image Comparer (rgthree)` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `Manual XY Entry Info` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
