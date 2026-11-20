---
name: unknown_workflow_sampler_clip_unet_343
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.896333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX 图生图学习基础工作流（用于学习）_2054901883512336386.json, 图片生成/图生图/FLUX.小红书网红生成机_1891789004021379074.json, 图片生成/图生图/FLUX网红推流版_1901477758571290625.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_343

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX 图生图学习基础工作流（用于学习）_2054901883512336386.json、图片生成/图生图/FLUX.小红书网红生成机_1891789004021379074.json、图片生成/图生图/FLUX网红推流版_1901477758571290625.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `TextInput_` —— 2/3 个有
- `easy promptConcat` —— 2/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Molmo7BDbnb` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
