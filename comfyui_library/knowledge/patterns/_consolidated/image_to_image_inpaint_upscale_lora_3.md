---
name: image_to_image_inpaint_upscale_lora_3
type: Image To Image
frequency: 5
level: strong
coverage: 0.9282
common_nodes: [Anything Everywhere3, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Get Image Size, GrowMaskWithBlur, Image Comparer (rgthree), Image Overlay, ImageScale, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键专业写真（拯救废片）_1979219311166394370.json, 图片生成/图生图/废片更换背景加高清修复_2039601149367558145.json, 平台全量/【一键换背景】AI摄影 背景自由 一键专业写真_1977290655506538497.json, 平台全量/一键专业写真_1936612870782357505.json, 平台全量/拯救废片 一键优化光影并增强清晰度 一键专业摄影人物模特写真_2000383004008644609.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键专业写真（拯救废片）_1979219311166394370.json、图片生成/图生图/废片更换背景加高清修复_2039601149367558145.json、平台全量/【一键换背景】AI摄影 背景自由 一键专业写真_1977290655506538497.json、平台全量/一键专业写真_1936612870782357505.json、平台全量/拯救废片 一键优化光影并增强清晰度 一键专业摄影人物模特写真_2000383004008644609.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `Get Image Size`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `ImageScale`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 2/5 个有
- `Joy_caption_two` —— 2/5 个有
- `Joy_caption_two_load` —— 2/5 个有
- `LayerMask: BiRefNetUltraV2` —— 2/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LibLibSeedreamV4Node` —— 2/5 个有
- `MaskPreview+` —— 2/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RH_Nano_Banana_Image2Image` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
