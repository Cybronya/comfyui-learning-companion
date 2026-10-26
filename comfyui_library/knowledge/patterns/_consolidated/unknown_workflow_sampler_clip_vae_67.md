---
name: unknown_workflow_sampler_clip_vae_67
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.952333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2-Klein-文生图（9B）_2012016556003303426.json, 图片生成/文生图/flux2-klein-9B 肢体修复+高清放大_2012497939876290562.json, 图片生成/文生图/z1.tonnie-klein文生图正确的方式_2012496046194171905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/flux2-Klein-文生图（9B）_2012016556003303426.json、图片生成/文生图/flux2-klein-9B 肢体修复+高清放大_2012497939876290562.json、图片生成/文生图/z1.tonnie-klein文生图正确的方式_2012496046194171905.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `easy int` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
