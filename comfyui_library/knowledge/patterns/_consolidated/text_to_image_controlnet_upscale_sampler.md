---
name: text_to_image_controlnet_upscale_sampler
type: Text To Image
frequency: 3
level: moderate
coverage: 0.584333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, EmptyLatentImage, Fast Groups Muter (rgthree), FluxGuidance, GetImageSize, JWImageResizeByLongerSide, KSampler, KSamplerSelect, LineArtPreprocessor, LoadImage, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【基础入门】 毛坯房转效果图_1916410335840894977.json, 平台全量/基于参考图室内装修_多选+放大v2_pro_1836286479432663042.json, 平台全量/基于参考图的室内装修风格可视化_多选+高清放大_1833857834357321730.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【基础入门】 毛坯房转效果图_1916410335840894977.json、平台全量/基于参考图室内装修_多选+放大v2_pro_1836286479432663042.json、平台全量/基于参考图的室内装修风格可视化_多选+高清放大_1833857834357321730.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `GetImageSize`
- `JWImageResizeByLongerSide`
- `KSampler`
- `KSamplerSelect`
- `LineArtPreprocessor`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `CLIPTextEncodeHunyuanDiT` —— 2/3 个有
- `DownloadAndLoadFlorence2Model` —— 2/3 个有
- `Florence2Run` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `Multi Text Merge` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `TextInput_` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `Int` —— 1/3 个有
- `Joy_caption` —— 1/3 个有
- `Joy_caption_load` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `PreviewTextNode` —— 1/3 个有
- `Save image with extra metadata [Crystools]` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| ControlNet 权重 | 0.8 | 0.6 - 0.8 | 3 | 87% |
| 采样步数 | 50 | 10 - 50 | 3 | 49% |
| Prompt 约束强度(CFG) | 5 | 3.5 - 5 | 3 | 84% |
| 采样算法 | ddpm | - | 3 | 67% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 75% |
| LoRA 文本强度 | 3 | - | 2 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.6 - 0.8，3 个样本，取值集中（一致性 87%）
- 采样步数 中位数 50，观测区间 10 - 50，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 5，观测区间 3.5 - 5，3 个样本，取值集中（一致性 84%）
- 采样算法 最常用 ddpm，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
