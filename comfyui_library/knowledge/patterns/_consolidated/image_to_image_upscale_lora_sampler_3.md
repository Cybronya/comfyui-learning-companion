---
name: image_to_image_upscale_lora_sampler_3
type: Image To Image
frequency: 26
level: moderate
coverage: 0.909923
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2026人像高清放大_2111016233243078658.json, 图片生成/图生图/4k细节高清修复放大 Krea2  4K High-Definition Restoratio_2093175048554237954.json, 图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2076831204363558913.json, 图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2077204887024263169.json, 图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2077214375592681474.json, 图片生成/图生图/Flux2‑Klein 画质修复｜控油 + 超分放大 + 细节增强_2089341242424516609.json, 图片生成/图生图/GM全能放大_2081984953218330626.json, 图片生成/图生图/GM场景放大_2079047148741681153.json, 图片生成/图生图/GM角色放大2_2079076481115971586.json, 图片生成/图生图/Klein 9B 渲染级产品精修V5版 自动白底+自动对齐_2072518037533712385.json, 图片生成/图生图/Krea2 最新工作流｜一键 4K 极致细节修复_2089365154176782337.json, 图片生成/图生图/Krea2+klein 双采样高清放大 工作流_2107666827190030337.json, 图片生成/图生图/Krea2高清修复+4k细节 去除AI塑料感-_2090250245597908993.json, 图片生成/图生图/Krea2高清修复+4k细节 去除AI塑料感-最新工作流_2079391952835006466.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-_2090617473048604674.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-_2090632524371423233.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-最新工作流_2081980031391322114.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-最新工作流_2095796380165033985.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-最新工作流_2096152026144133121.json, 图片生成/图生图/Krea2高清修复4k细节最新工作流_2079017345418354689.json, 图片生成/图生图/Krea2高清修复4k细节最新工作流_2079876925773926402.json, 图片生成/图生图/Krea2高清修复_4k细节最新工作流_2075388724048912386.json, 图片生成/图生图/Krea2高清修复_4k细节最新工作流_2075398450363064322.json, 图片生成/图生图/flux-2-klein 9b高清修复_4k细节-Krea2最新工作流_2081987882591547393.json, 图片生成/图生图/krea2高清修复工作流_2089631544880230401.json, 图片生成/图生图/人物皮肤质感+克莱因高清_1914251049425694721.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/图生图/2026人像高清放大_2111016233243078658.json、图片生成/图生图/4k细节高清修复放大 Krea2  4K High-Definition Restoratio_2093175048554237954.json、图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2076831204363558913.json、图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2077204887024263169.json、图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2077214375592681474.json…）

- **类型**：Image To Image
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 26 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `EditTextEncode_EditUtils` —— 25/26 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 25/26 个有
- `Flux2KleinModelConfig_EditUtils` —— 25/26 个有
- `FluxKVCache` —— 25/26 个有
- `Image Comparer (rgthree)` —— 25/26 个有
- `PrimitiveFloat` —— 25/26 个有
- `VAEEncodeTiled` —— 25/26 个有
- `easy cleanGpuUsed` —— 25/26 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 23/26 个有
- `Anything Everywhere3` —— 18/26 个有
- `LatentColorMatchSimple` —— 15/26 个有
- `PreviewImage` —— 6/26 个有
- `TTP_Image_Assy` —— 5/26 个有
- `TTP_Image_Tile_Batch` —— 5/26 个有
- `TTP_Tile_image_size` —— 5/26 个有
- `ImageListToImageBatch` —— 4/26 个有
- `easy imageBatchToImageList` —— 4/26 个有
- `PrimitiveStringMultiline` —— 3/26 个有
- `CheckpointLoaderSimple` —— 1/26 个有
- `ColorMatchPro` —— 1/26 个有
- `DualCLIPLoader` —— 1/26 个有
- `EmptyFlux2LatentImage` —— 1/26 个有
- `Fast Groups Bypasser (rgthree)` —— 1/26 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 1/26 个有
- `FluxGuidance` —— 1/26 个有
- `INTConstant` —— 1/26 个有
- `ImpactImageBatchToImageList` —— 1/26 个有
- `LCSColorAnchor` —— 1/26 个有
- `LCSLoadData` —— 1/26 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/26 个有
- `MemoryCleaner` —— 1/26 个有
- `PathchSageAttentionKJ` —— 1/26 个有
- `RHHiddenNodes` —— 1/26 个有
- `SeedVR2Conditioning` —— 1/26 个有
- `SeedVR2Preprocess` —— 1/26 个有
- `SimpleMath+` —— 1/26 个有
- `easy imageListToImageBatch` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 1 - 6 | 26 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 26 | 100% |
| 采样算法 | euler_ancestral | - | 26 | 92% |
| 调度器 | kl_optimal | - | 26 | 96% |
| 重绘幅度 | 0.4 | 0.4 - 1 | 26 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 1 - 6，26 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，26 个样本，一致性 92%
- 调度器 最常用 kl_optimal，26 个样本，一致性 96%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 1，26 个样本
- 高发问题（29/26 个样本）：Steps较低可能导致细节不足
