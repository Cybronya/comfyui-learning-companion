---
name: image_to_image_inpaint_upscale_lora_5
type: Image To Image
frequency: 3
level: strong
coverage: 0.933333
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_NearestSDXLResolution, CR Color Bars, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, ETN_CropImage, EmptySD3LatentImage, FluxGuidance, GlobalSeed //Inspire, Image To Mask, ImageBlur, ImageInvert, ImagePaste, ImageRemoveAlpha+, ImageScale, InpaintModelConditioning, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, Paste By Mask, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext360VR出图_1941851490090905601.json, 图片生成/图生图/一张图生成360全景（Kontext）_1949749378559950850.json, 图片生成/图生图/室内全景图_1922505451131342850.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/kontext360VR出图_1941851490090905601.json、图片生成/图生图/一张图生成360全景（Kontext）_1949749378559950850.json、图片生成/图生图/室内全景图_1922505451131342850.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_NearestSDXLResolution`
- `CR Color Bars`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `ETN_CropImage`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `GlobalSeed //Inspire`
- `Image To Mask`
- `ImageBlur`
- `ImageInvert`
- `ImagePaste`
- `ImageRemoveAlpha+`
- `ImageScale`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `Paste By Mask`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FL_SDUltimate_Slices` —— 2/3 个有
- `FluxEmptyLatentSizePicker` —— 2/3 个有
- `LoadImageOutput` —— 2/3 个有
- `LyingSigmaSampler` —— 2/3 个有
- `MagCache` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `MultiplySigmas` —— 2/3 个有
- `TeaCache` —— 2/3 个有
- `UltimateSDUpscaleCustomSample` —— 2/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `HDRCreate` —— 1/3 个有
- `PanoramaViewerNode` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Width/Height Literal (Image Saver)` —— 1/3 个有
- `workflow>3` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1344x768 (1.03MP) - 16:9 | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.58 | 0.58 - 0.58 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 最常用 1344x768 (1.03MP) - 16:9，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.58，观测区间 0.58 - 0.58，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
