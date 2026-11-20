---
name: unknown_workflow_sampler_clip_unet_543
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/🍕最强开源 FLUX2系列之文生图【题词自动优化】_1993551504671965186.json, 视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_543

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/🍕最强开源 FLUX2系列之文生图【题词自动优化】_1993551504671965186.json、视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CompressImages` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int Literal` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
