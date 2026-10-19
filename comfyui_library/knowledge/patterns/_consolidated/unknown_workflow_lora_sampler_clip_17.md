---
name: unknown_workflow_lora_sampler_clip_17
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.838333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, FluxGuidance, KSamplerSelect, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [Text Concatenate, Text Multiline, CR SDXL Aspect Ratio, easy cleanGpuUsed, Upscale Model Loader]
members: [图片生成/文生图/1913094526456557570.json, 图片生成/文生图/1914304383847231490.json, 图片生成/文生图/1915672810759589889.json, 图片生成/文生图/1915753087057723394.json, 图片生成/文生图/1920069563512459265.json, 图片生成/文生图/1923351389630885890.json, 图片生成/文生图/1927931879364935681.json, 图片生成/文生图/1929809956793434113.json, 图片生成/文生图/1947113386972327938.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1913094526456557570.json、图片生成/文生图/1914304383847231490.json、图片生成/文生图/1915672810759589889.json、图片生成/文生图/1915753087057723394.json、图片生成/文生图/1920069563512459265.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `CR SDXL Aspect Ratio` —— 1/9 个有
- `ImageUpscaleWithModel` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_Captioner` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `Text Concatenate` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `Upscale Model Loader` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Text Concatenate、Text Multiline、CR SDXL Aspect Ratio、easy cleanGpuUsed、Upscale Model Loader
