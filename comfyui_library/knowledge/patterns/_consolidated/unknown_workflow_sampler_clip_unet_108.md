---
name: unknown_workflow_sampler_clip_unet_108
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_通用导演台_图生配音视频_2086025061747748866.json, 视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_108

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_通用导演台_图生配音视频_2086025061747748866.json、视频生成/文生视频/Flux.2 Klein 9B文生图_2066059765985406977.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

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
- `CompressImages` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `Int Literal` —— 1/2 个有
- `MiniMaxH3Director` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
