---
name: image_to_image_lora_sampler_clip_12
type: Image To Image
frequency: 12
level: strong
coverage: 0.915333
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, GoogleTranslateTextNode, ImageConcanate, ImageStitch, KSampler, LoadImage, LoadImageOutput, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/20250711教程-多种注意力方式及遮罩对比工作流_1943266766070181890.json, 图片生成/图生图/20250712教程-Kontext多种加速对比工作流1_1943718782529339393.json, 图片生成/图生图/20250712教程-Kontext多种加速对比工作流2_1943661657971363841.json, 图片生成/图生图/FLUX真人照片转粘土风格_1948981078938791938.json, 图片生成/图生图/Flux Kontext Dev 3D玩具风格加速版v1_1941886932706291713.json, 图片生成/图生图/Flux Kontext Dev 90S香港电影胶片风加速版v1_1943629738063921153.json, 图片生成/图生图/Flux Kontext Dev IP三视图特化稳定版加速版v1_1941734024627044353.json, 图片生成/图生图/Flux Kontext Dev gmic icon颜色转换加速版v1_1942622828363452418.json, 图片生成/图生图/Flux Kontext Dev 极端模糊图片3阶段差异修复V2_1940683049312956417.json, 图片生成/图生图/Flux Kontext Dev万物3D建模加速版v1_1944428611233304578.json, 图片生成/图生图/Flux Kontext Dev二阶段修复万物马克笔风格化加速版v1_1941724018607341569.json, 图片生成/图生图/二阶段极限修复Deblur+SeedVR_1975919737614020610.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/20250711教程-多种注意力方式及遮罩对比工作流_1943266766070181890.json、图片生成/图生图/20250712教程-Kontext多种加速对比工作流1_1943718782529339393.json、图片生成/图生图/20250712教程-Kontext多种加速对比工作流2_1943661657971363841.json、图片生成/图生图/FLUX真人照片转粘土风格_1948981078938791938.json、图片生成/图生图/Flux Kontext Dev 3D玩具风格加速版v1_1941886932706291713.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GoogleTranslateTextNode`
- `ImageConcanate`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoadImageOutput`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MagCache` —— 9/12 个有
- `TeaCache` —— 5/12 个有
- `LayerUtility: PurgeVRAM` —— 4/12 个有
- `PDIMAGE_LongerSize` —— 3/12 个有
- `EmptySD3LatentImage` —— 2/12 个有
- `InvSRSampler` —— 2/12 个有
- `LoadInvSRModels` —— 2/12 个有
- `NunchakuFluxDiTLoader` —— 2/12 个有
- `NunchakuFluxLoraLoader` —— 2/12 个有
- `PMRF` —— 2/12 个有
- `CLIPVisionLoader` —— 1/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `ImageAndMaskPreview` —— 1/12 个有
- `Kontext Inpainting Conditioning` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `LucidFlux_SM_Cond` —— 1/12 个有
- `LucidFlux_SM_Encode` —— 1/12 个有
- `LucidFlux_SM_KSampler` —— 1/12 个有
- `LucidFlux_SM_Model` —— 1/12 个有
- `SeedVR2BlockSwap` —— 1/12 个有
- `SeedVR2ExtraArgs` —— 1/12 个有
- `SeedVR2GGUF` —— 1/12 个有
- `SetLatentNoiseMask` —— 1/12 个有
- `ShowText` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 12 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，12 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
