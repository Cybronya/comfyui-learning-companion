---
name: unknown_workflow_controlnet_lora_sampler_13
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.93975
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ConditioningCombine, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, GetImageSize+, ImageResize+, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Flux_高清放大-Upscaler-jasperai_1955616753901453314.json, 图片生成/图生图/【图片超分】Flux.1.0_洗图超分_1981202730742087681.json, 图片生成/图生图/修复+高清放大-flux_1955249718633775105.json, 数字人/数字人/目前最强全局修复+高清放大-许老师专用_1981563194785316866.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux_高清放大-Upscaler-jasperai_1955616753901453314.json、图片生成/图生图/【图片超分】Flux.1.0_洗图超分_1981202730742087681.json、图片生成/图生图/修复+高清放大-flux_1955249718633775105.json、数字人/数字人/目前最强全局修复+高清放大-许老师专用_1981563194785316866.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningCombine`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `GetImageSize+`
- `ImageResize+`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImpactInt` —— 3/4 个有
- `ResizeLongestToNode` —— 3/4 个有
- `FloatSlider` —— 2/4 个有
- `Joy_caption` —— 2/4 个有
- `Joy_caption_load` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `CR Latent Batch Size` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `easy float` —— 1/4 个有
- `easy getNode` —— 1/4 个有
- `easy setNode` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.7 - 0.9 | 4 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.7 - 0.9，4 个样本，取值集中（一致性 91%）
