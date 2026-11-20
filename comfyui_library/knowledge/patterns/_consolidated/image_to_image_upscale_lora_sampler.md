---
name: image_to_image_upscale_lora_sampler
type: Image To Image
frequency: 40
level: strong
coverage: 0.911775
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2026人像高清放大_2111016233243078658.json, 图片生成/图生图/4k细节高清修复放大 Krea2  4K High-Definition Restoratio_2093175048554237954.json, 图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2076831204363558913.json, 图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2077204887024263169.json, 图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2077214375592681474.json, 图片生成/图生图/4k细节高清修复放大_Krea2_4K_High-Definition_Restoratio_2116666165421498370.json, 图片生成/图生图/Flux2‑Klein 画质修复｜控油 + 超分放大 + 细节增强_2089341242424516609.json, 图片生成/图生图/GM全能放大_2081984953218330626.json, 图片生成/图生图/GM场景放大_2079047148741681153.json, 图片生成/图生图/GM角色放大2_2079076481115971586.json, 图片生成/图生图/Klein 9B 渲染级产品精修V5版 自动白底+自动对齐_2072518037533712385.json, 图片生成/图生图/Krea2 最新工作流｜一键 4K 极致细节修复_2089365154176782337.json, 图片生成/图生图/Krea2+klein 双采样高清放大 工作流_2107666827190030337.json, 图片生成/图生图/Krea2高清修复+4k细节 去除AI塑料感-_2090250245597908993.json, 图片生成/图生图/Krea2高清修复+4k细节 去除AI塑料感-最新工作流_2079391952835006466.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-_2090617473048604674.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-_2090632524371423233.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-最新工作流_2081980031391322114.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-最新工作流_2095796380165033985.json, 图片生成/图生图/Krea2高清修复+4k细节_去除AI塑料感-最新工作流_2096152026144133121.json, 图片生成/图生图/Krea2高清修复4k细节最新工作流_2079017345418354689.json, 图片生成/图生图/Krea2高清修复4k细节最新工作流_2079876925773926402.json, 图片生成/图生图/Krea2高清修复_4k细节最新工作流_2075388724048912386.json, 图片生成/图生图/Krea2高清修复_4k细节最新工作流_2075398450363064322.json, 图片生成/图生图/flux-2-klein 9b高清修复_4k细节-Krea2最新工作流_2081987882591547393.json, 图片生成/图生图/krea2高清修复工作流_2089631544880230401.json, 图片生成/图生图/人像精修皮肤质感后再SeedVR2二段超分，高清放大纹理自然真实不假面_2115605126567256066.json, 图片生成/图生图/人像精修皮肤质感后再SeedVR2二段超分，高清放大纹理自然真实不假面_2115941665654530049.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2074820750917328897.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2077028032933613569.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2077343497681727490.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2077826236499456001.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2078025500471160834.json, 图片生成/图生图/高清修复 4k细节-Krea2最新工作流_2078073501503811585.json, 图片生成/图生图/高清修复+4k细节-Krea2 自然真实 修复细节 最新工作流 极致美学_2076542796521099266.json, 图片生成/图生图/高清修复4k细节_2076124143707312129.json, 图片生成/图生图/高清修复_4k细节-Krea2最新工作流_2092621636909486081.json, 图片生成/图生图/高清细节修复 去除AI感_2087433012127555586.json, 平台全量/Krea2最新 4K 细节高清修复拉满_2086072873881526274.json, 平台全量/洗图修复2.0_2077086906856337409.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler

> 由 `engine/knowledge_consolidation` 从 40 个 workflow 归纳得出（图片生成/图生图/2026人像高清放大_2111016233243078658.json、图片生成/图生图/4k细节高清修复放大 Krea2  4K High-Definition Restoratio_2093175048554237954.json、图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2076831204363558913.json、图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2077204887024263169.json、图片生成/图生图/4k细节高清修复放大+-Krea2最新工作流_2077214375592681474.json…）

- **类型**：Image To Image
- **样本数**：40
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 40 个 workflow 都包含：
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
- `EditTextEncode_EditUtils` —— 39/40 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 39/40 个有
- `Flux2KleinModelConfig_EditUtils` —— 39/40 个有
- `FluxKVCache` —— 39/40 个有
- `PrimitiveFloat` —— 39/40 个有
- `VAEEncodeTiled` —— 39/40 个有
- `easy cleanGpuUsed` —— 39/40 个有
- `Image Comparer (rgthree)` —— 38/40 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 37/40 个有
- `Anything Everywhere3` —— 30/40 个有
- `LatentColorMatchSimple` —— 28/40 个有
- `PreviewImage` —— 8/40 个有
- `ImageListToImageBatch` —— 5/40 个有
- `TTP_Image_Assy` —— 5/40 个有
- `TTP_Image_Tile_Batch` —— 5/40 个有
- `TTP_Tile_image_size` —— 5/40 个有
- `easy imageBatchToImageList` —— 4/40 个有
- `PrimitiveStringMultiline` —— 3/40 个有
- `SeedVR2LoadDiTModel` —— 3/40 个有
- `SeedVR2LoadVAEModel` —— 3/40 个有
- `SeedVR2VideoUpscaler` —— 3/40 个有
- `DualCLIPLoader` —— 2/40 个有
- `EmptyFlux2LatentImage` —— 1/40 个有
- `Float` —— 1/40 个有
- `FluxGuidance` —— 1/40 个有
- `ImageResize+` —— 1/40 个有
- `ImageScaleBy` —— 1/40 个有
- `ImpactImageBatchToImageList` —— 1/40 个有
- `ImpactInt` —— 1/40 个有
- `ImpactMinMax` —— 1/40 个有
- `Joy_caption_two` —— 1/40 个有
- `Joy_caption_two_load` —— 1/40 个有
- `PreviewAny` —— 1/40 个有
- `ResizeImagesByLongerEdge` —— 1/40 个有
- `SDVN Load Image Url` —— 1/40 个有
- `SimpleMath+` —— 1/40 个有
- `easy imageSize` —— 1/40 个有
- `easy int` —— 1/40 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 3 - 6 | 40 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 40 | 100% |
| 采样算法 | euler_ancestral | - | 40 | 98% |
| 调度器 | kl_optimal | - | 40 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.6 | 40 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 41/40 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 3 - 6，40 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，40 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，40 个样本，一致性 98%
- 调度器 最常用 kl_optimal，40 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.6，40 个样本，取值集中（一致性 87%）
- 高发问题（41/40 个样本）：Steps较低可能导致细节不足
