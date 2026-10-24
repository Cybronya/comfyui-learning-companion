---
name: text_to_image_controlnet_upscale_lora
type: Text To Image
frequency: 10
level: strong
coverage: 0.7963
common_nodes: [BasicGuider, BasicScheduler, Bjornulf_ShowText, CLIPTextEncode, CR Text Replace, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, EmptyLatentImage, FluxGuidance, Image Comparer (rgthree), ImageBlend, ImageResizeKJ, JjkText, KSampler, KSamplerSelect, LeReS-DepthMapPreprocessor, LoadImage, LoraLoader, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, RH_Captioner, RH_Prompter, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, TextCombinerTwo, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/WH-AI-Studio毛坯房到装修效果图（装修专用）_2022501173428752386.json, 图片生成/图生图/一键实现毛坯房到装修效果图_1943509704708681730.json, 图片生成/图生图/一键实现毛坯房到装修效果图_2052939319219896321.json, 图片生成/图生图/一键毛坯房到精装修效果图-细节可独立调整_2054741290750881793.json, 图片生成/图生图/一键毛坯房到精装修效果图-细节可独立调整_2060241573308358658.json, 图片生成/图生图/一键装修毛坯房（高效率神器）_2044610308148301825.json, 图片生成/图生图/家装_1960161910832443393.json, 图片生成/图生图/毛坯房转换装修效果图（完美匹配房型）_1958803174297591809.json, 图片生成/图生图/超好用🔥一键毛坯房到精装修效果图-细节可独立调整_2053655000986992641.json, 图片生成/文生图/一键实现毛坯房到装修效果图_1948432612133076993.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/WH-AI-Studio毛坯房到装修效果图（装修专用）_2022501173428752386.json、图片生成/图生图/一键实现毛坯房到装修效果图_1943509704708681730.json、图片生成/图生图/一键实现毛坯房到装修效果图_2052939319219896321.json、图片生成/图生图/一键毛坯房到精装修效果图-细节可独立调整_2054741290750881793.json、图片生成/图生图/一键毛坯房到精装修效果图-细节可独立调整_2060241573308358658.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `Bjornulf_ShowText`
- `CLIPTextEncode`
- `CR Text Replace`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageBlend`
- `ImageResizeKJ`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LeReS-DepthMapPreprocessor`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `RH_Captioner`
- `RH_Prompter`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `TextCombinerTwo`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 9/10 个有
- `easy cleanGpuUsed` —— 9/10 个有
- `Label (rgthree)` —— 8/10 个有
- `GetNode` —— 1/10 个有
- `ImageUpscaleWithModel` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `easy seed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 512 | 512 - 512 | 10 | 100% |
| 高度 | 512 | 512 - 512 | 10 | 100% |
| 采样步数 | 30 | 30 - 30 | 10 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 10 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 10 | 90% |
| 调度器 | karras | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| ControlNet 权重 | 0.6 | 0.4 - 0.6 | 10 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，10 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，10 个样本，一致性 90%
- 调度器 最常用 karras，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，观测区间 0.4 - 0.6，10 个样本，取值集中（一致性 90%）
