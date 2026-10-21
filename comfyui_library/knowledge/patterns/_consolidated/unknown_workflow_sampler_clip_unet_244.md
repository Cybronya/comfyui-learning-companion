---
name: unknown_workflow_sampler_clip_unet_244
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6985
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, ImpactInt, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/开源参数猛兽FLUX2系列 —— 文字生图片_1993607069964107777.json, 图片生成/文生图/🍕最强开源 FLUX2系列之文生图【题词自动优化】_1993551504671965186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_244

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/开源参数猛兽FLUX2系列 —— 文字生图片_1993607069964107777.json、图片生成/文生图/🍕最强开源 FLUX2系列之文生图【题词自动优化】_1993551504671965186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `ImpactInt`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
