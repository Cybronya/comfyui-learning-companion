---
name: image_to_image_sampler_unet_vae_25
type: Image To Image
frequency: 9
level: strong
coverage: 0.821556
common_nodes: [CLIPLoader, CR Text, GetImageSize, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview+, PainterFluxImageEdit, ReferenceLatent, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2产品换背景_自由调整位置_2089149943289307137.json, 图片生成/图生图/产品背景合成+融图打光（自动版）_2022663606793408513.json, 图片生成/图生图/合成打光-场景融合-flux2 klein产品场景合成_2020204898721206274.json, 图片生成/图生图/溶图合成打光-flux2最新全流程_2021815536040026114.json, 图片生成/图生图/溶图合成打光-flux2最新全流程_2096807788579213314.json, 图片生成/图生图/溶图合成打光-flux2最新全流程_2097153012191031297.json, 图片生成/图生图/电商产品溶图合成打光-flux2最新全流程_2029363862591512577.json, 图片生成/图生图/电商换背景_flux2最新溶图工作流_2031610323630825473.json, 平台全量/电商产品换背景-加重打光-flux klein-可参考指定的背景_2029520688947662850.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_25

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2产品换背景_自由调整位置_2089149943289307137.json、图片生成/图生图/产品背景合成+融图打光（自动版）_2022663606793408513.json、图片生成/图生图/合成打光-场景融合-flux2 klein产品场景合成_2020204898721206274.json、图片生成/图生图/溶图合成打光-flux2最新全流程_2021815536040026114.json、图片生成/图生图/溶图合成打光-flux2最新全流程_2096807788579213314.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `GetImageSize`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview+`
- `PainterFluxImageEdit`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `RH_Captioner` —— 8/9 个有
- `孤海-遮罩混合运算` —— 8/9 个有
- `CR Color Panel` —— 7/9 个有
- `FastCanvas` —— 7/9 个有
- `FastCanvasTool` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `SolidMask` —— 7/9 个有
- `easy imageDetailTransfer` —— 7/9 个有
- `easy imageRemBg` —— 7/9 个有
- `LayerColor: ColorAdapter` —— 1/9 个有
- `LayerMask: MaskPreview` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（18/9 个样本）：Steps较低可能导致细节不足
