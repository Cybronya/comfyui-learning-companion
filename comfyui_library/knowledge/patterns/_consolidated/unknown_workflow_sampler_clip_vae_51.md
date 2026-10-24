---
name: unknown_workflow_sampler_clip_vae_51
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.98675
common_nodes: [CLIPLoader, CLIPTextEncode, FluxGuidance, Load pi-Flow Model, LoadImage, ModelSamplingPiFlow, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, pi-Flow Sampler]
problems: []
missing: []
members: [图片生成/图生图/Flux 2-Pi 4步超级加速图像编辑V1_2006071587203715073.json, 图片生成/图生图/Flux2-单图编辑（4步出图）_2007029117383876609.json, 图片生成/文生图/FLUX2-PIFLOW-4步加速_2008106083335802881.json, 图片生成/文生图/pi-Flux2 4步文生图_2073296324719632386.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_51

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux 2-Pi 4步超级加速图像编辑V1_2006071587203715073.json、图片生成/图生图/Flux2-单图编辑（4步出图）_2007029117383876609.json、图片生成/文生图/FLUX2-PIFLOW-4步加速_2008106083335802881.json、图片生成/文生图/pi-Flux2 4步文生图_2073296324719632386.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `FluxGuidance`
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
- `EmptyFlux2LatentImage` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
