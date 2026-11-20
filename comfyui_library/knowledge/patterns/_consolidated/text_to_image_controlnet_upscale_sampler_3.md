---
name: text_to_image_controlnet_upscale_sampler_3
type: Text To Image
frequency: 3
level: strong
coverage: 0.648667
common_nodes: [AIO_Preprocessor, CLIPSetLastLayer, CLIPTextEncode, CLIPTextEncodeSDXL, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, GetNode, ImageResize+, ImageUpscaleWithModel, KSampler, KSamplerAdvanced, LoadImage, PreviewImage, RepeatLatentBatch, SaveImage, SetNode, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/气泡酒商业摄影与油画风格转换_1805497356858155009.json, 平台全量/黄玫瑰_1805851834558377985.json, 平台全量/黄玫瑰_1807626610060275713.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/气泡酒商业摄影与油画风格转换_1805497356858155009.json、平台全量/黄玫瑰_1805851834558377985.json、平台全量/黄玫瑰_1807626610060275713.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CLIPTextEncodeSDXL`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `GetNode`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CropFace` —— 2/3 个有
- `DF_Integer` —— 2/3 个有
- `DF_Text_Box` —— 2/3 个有
- `IPAdapterFaceID` —— 2/3 个有
- `IPAdapterUnifiedLoaderFaceID` —— 2/3 个有
- `Mask Gaussian Region` —— 2/3 个有
- `CLIPTextEncodeSDXLRefiner` —— 1/3 个有
- `IPAdapter` —— 1/3 个有
- `IPAdapterUnifiedLoader` —— 1/3 个有
- `Integer` —— 1/3 个有
- `Text box` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 0.25 | 0.25 - 0.46 | 3 | 69% |
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 0.25，观测区间 0.25 - 0.46，3 个样本
- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
