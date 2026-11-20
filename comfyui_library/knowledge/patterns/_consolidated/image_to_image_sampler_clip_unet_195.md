---
name: image_to_image_sampler_clip_unet_195
type: Image To Image
frequency: 3
level: strong
coverage: 0.891667
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, ImageResizeKJ, InstructPixToPixConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: TextJoin, LoadImage, SaveImage, SetLatentNoiseMask, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/WildboarA6 丨抽象艺术手机壳_1881067974433075202.json, 平台全量/创意水果服装_1892850607370506242.json, 平台全量/更换抱枕风格_1876484740135243777.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_195

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/WildboarA6 丨抽象艺术手机壳_1881067974433075202.json、平台全量/创意水果服装_1892850607370506242.json、平台全量/更换抱枕风格_1876484740135243777.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `ImageResizeKJ`
- `InstructPixToPixConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: TextJoin`
- `LoadImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `ApplyIPAdapterFlux` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `FloatSlider` —— 1/3 个有
- `IPAdapterFluxLoader` —— 1/3 个有
- `ImageToMask` —— 1/3 个有
- `JWImageResizeByLongerSide` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerMask: BiRefNetUltraV2` —— 1/3 个有
- `LayerMask: LoadBiRefNetModel` —— 1/3 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/3 个有
- `LayerUtility: ColorPicker` —— 1/3 个有
- `LayerUtility: ImageHub` —— 1/3 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 25 - 30 | 3 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 25 - 30，3 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
