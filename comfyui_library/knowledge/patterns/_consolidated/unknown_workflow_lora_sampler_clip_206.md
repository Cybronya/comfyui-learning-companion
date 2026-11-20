---
name: unknown_workflow_lora_sampler_clip_206
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.912
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Amazon写实类人物场景 外贸跨境电商产品主图详情页场景_2012697618173923329.json, 图片生成/文生图/FLUX 2-文生图_1993499987302612994.json, 图片生成/文生图/FLUX2 文生图-text to image_1993525496059281410.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_206

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Amazon写实类人物场景 外贸跨境电商产品主图详情页场景_2012697618173923329.json、图片生成/文生图/FLUX 2-文生图_1993499987302612994.json、图片生成/文生图/FLUX2 文生图-text to image_1993525496059281410.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `ChinesePrompt_Mix` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `Int` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
