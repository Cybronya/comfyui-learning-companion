---
name: unknown_workflow_sampler_clip_vae_49
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9735
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, FluxGuidance, ImageScaleToTotalPixels, Load pi-Flow Model, LoadImage, ModelSamplingPiFlow, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, pi-Flow Sampler]
problems: []
missing: []
members: [图片生成/文生图/FLUX2-PIFLOW-4步加速_2008106083335802881.json, 图片生成/文生图/pi-Flux2 4步文生图_2073296324719632386.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_49

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/FLUX2-PIFLOW-4步加速_2008106083335802881.json、图片生成/文生图/pi-Flux2 4步文生图_2073296324719632386.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `Load pi-Flow Model`
- `LoadImage`
- `ModelSamplingPiFlow`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `pi-Flow Sampler`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
