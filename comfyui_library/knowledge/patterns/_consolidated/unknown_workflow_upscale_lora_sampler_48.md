---
name: unknown_workflow_upscale_lora_sampler_48
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.82375
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, GetImageSize+, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoader, ModelSamplingFlux, PreviewImage, RandomNoise, SDXLPromptStyler, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Flux Krea 图生图洗图放大（SD Upscale）_1847689348954329089.json, 图片生成/图生图/Flux多重控制参考图片风格转绘（EasyControl Canny）_1909451347215659009.json, 图片生成/图生图/haiilo-Flux洗图放大_1947757479541227522.json, 图片生成/图生图/多场景融合生成（基于UNO 多图版） ）_1910578932431712257.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux Krea 图生图洗图放大（SD Upscale）_1847689348954329089.json、图片生成/图生图/Flux多重控制参考图片风格转绘（EasyControl Canny）_1909451347215659009.json、图片生成/图生图/haiilo-Flux洗图放大_1947757479541227522.json、图片生成/图生图/多场景融合生成（基于UNO 多图版） ）_1910578932431712257.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SDXLPromptStyler`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `MirroredImage` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `JjkShowText` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `EasyControlGenerate` —— 1/4 个有
- `EasyControlLoadFlux` —— 1/4 个有
- `EasyControlLoadLora` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageResize` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `RunningHub_UNO_Loadmodel` —— 1/4 个有
- `RunningHub_UNO_Sampler` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | 0.3 - 0.4 | 4 | 88% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.4，观测区间 0.3 - 0.4，4 个样本，取值集中（一致性 88%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
