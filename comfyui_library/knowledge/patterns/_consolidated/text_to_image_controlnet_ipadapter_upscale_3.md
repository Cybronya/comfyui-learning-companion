---
name: text_to_image_controlnet_ipadapter_upscale_3
type: Text To Image
frequency: 3
level: strong
coverage: 0.86
common_nodes: [AIO_Preprocessor, Anything Everywhere, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSize, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, LoraLoaderModelOnly, ModelSamplingFlux, PixelPerfectResolution, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, SetUnionControlNetType, ShowText|pysssss, String, Text Concatenate, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, Zoe_DepthAnythingPreprocessor]
problems: []
missing: []
members: [图片生成/图生图/Flux转绘+XL线稿+depth+IPA毛坯房生效果图_1935282658937339906.json, 平台全量/zmj毛坯房转室内效果图_2016474847748038658.json, 平台全量/毛坯房转室内效果图_1882062091547705346.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_upscale_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux转绘+XL线稿+depth+IPA毛坯房生效果图_1935282658937339906.json、平台全量/zmj毛坯房转室内效果图_2016474847748038658.json、平台全量/毛坯房转室内效果图_1882062091547705346.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PixelPerfectResolution`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `String`
- `Text Concatenate`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `Zoe_DepthAnythingPreprocessor`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| 采样步数 | 32 | 32 - 32 | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 32，观测区间 32 - 32，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
