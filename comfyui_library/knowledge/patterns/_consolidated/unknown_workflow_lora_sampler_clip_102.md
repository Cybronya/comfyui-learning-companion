---
name: unknown_workflow_lora_sampler_clip_102
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.807667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, FluxGuidance, KSamplerSelect, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [Text Concatenate, Text Multiline, CR SDXL Aspect Ratio, easy cleanGpuUsed, Upscale Model Loader]
members: [图片生成/文生图/1913094526456557570.json, 图片生成/文生图/1920069563512459265.json, 图片生成/文生图/1923351389630885890.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1913094526456557570.json、图片生成/文生图/1920069563512459265.json、图片生成/文生图/1923351389630885890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
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
- `EmptySD3LatentImage` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `Upscale Model Loader` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Text Concatenate、Text Multiline、CR SDXL Aspect Ratio、easy cleanGpuUsed、Upscale Model Loader
