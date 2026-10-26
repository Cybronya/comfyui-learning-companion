---
name: unknown_workflow_sampler_unet_vae_55
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.668923
common_nodes: [CLIPLoader, CR Text, GrowMaskWithBlur, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PainterFluxImageEdit, RH_LLMAPI_Pro_Node, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageDetailTransfer, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX2+Klein自动更换背景_2082542629203566593.json, 图片生成/图生图/FLUX2+Klein自动更换背景_2084534648163618817.json, 图片生成/图生图/FLUX2+Klein自动更换背景_2084648676047278081.json, 图片生成/图生图/FLUX2+Klein自动更换背景_2087355589092536322.json, 图片生成/图生图/FLUX2+Klein自动更换背景_2092611518163668994.json, 图片生成/图生图/Flux2-Klein_产品换背景（融入自然 高一致性）_2015989981126336514.json, 图片生成/图生图/Flux2-Klein电商产品更换背景 效果一般  林瑶_2016171845766094849.json, 图片生成/图生图/Flux2-Klein电商产品更换背景_2015763026812608514.json, 图片生成/图生图/单图编辑_2016421973278068737.json, 图片生成/图生图/自动更换背景（人物+电商产品）- FLUX2+Klein_2015610719189868545.json, 图片生成/图生图/自动更换背景（人物+电商产品）-FLUX2+Klein_2014525020197883905.json, 图片生成/图生图/🦄Klein更换背景~适合人物电商产品等🦄_2013874760345722882.json, 图片生成/图生图/🦄Klein更换背景~适合人物电商产品等🦄_2015981122013896705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_55

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/FLUX2+Klein自动更换背景_2082542629203566593.json、图片生成/图生图/FLUX2+Klein自动更换背景_2084534648163618817.json、图片生成/图生图/FLUX2+Klein自动更换背景_2084648676047278081.json、图片生成/图生图/FLUX2+Klein自动更换背景_2087355589092536322.json、图片生成/图生图/FLUX2+Klein自动更换背景_2092611518163668994.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `GrowMaskWithBlur`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PainterFluxImageEdit`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageDetailTransfer`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 12/13 个有
- `PreviewImage` —— 10/13 个有
- `GetNode` —— 9/13 个有
- `SetNode` —— 9/13 个有
- `ShowText|pysssss` —— 9/13 个有
- `孤海图像缩放按像素` —— 7/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/13 个有
- `MaskPreview+` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `Note Plus (mtb)` —— 3/13 个有
- `DapaoImageAspectRatioResizeNode` —— 2/13 个有
- `LayerMask: MaskPreview` —— 1/13 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
