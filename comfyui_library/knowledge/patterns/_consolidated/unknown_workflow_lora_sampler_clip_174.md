---
name: unknown_workflow_lora_sampler_clip_174
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.92
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Amazon写实类人物场景 外贸跨境电商产品主图详情页场景_2012697618173923329.json, 图片生成/文生图/人猫合影_1891781898589384705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_174

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Amazon写实类人物场景 外贸跨境电商产品主图详情页场景_2012697618173923329.json、图片生成/文生图/人猫合影_1891781898589384705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
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
- `CR Text` —— 1/2 个有
- `ChinesePrompt_Mix` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `Int` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
