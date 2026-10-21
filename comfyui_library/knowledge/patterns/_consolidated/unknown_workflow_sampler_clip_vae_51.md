---
name: unknown_workflow_sampler_clip_vae_51
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2-klein-9B 肢体修复+高清放大_2012497939876290562.json, 图片生成/文生图/z1.tonnie-klein文生图正确的方式_2012496046194171905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_51

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/flux2-klein-9B 肢体修复+高清放大_2012497939876290562.json、图片生成/文生图/z1.tonnie-klein文生图正确的方式_2012496046194171905.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
