---
name: unknown_workflow_sampler_clip_vae_35
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.917667
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2单图编辑_1993878843299741698.json, 图片生成/图生图/Flux2单图编辑flux最新图片编辑模型（支持中文））_1993552295038222338.json, 图片生成/图生图/Flux2双图编辑_1993864960981794817.json, 图片生成/图生图/WF28-Flux2DEV测试_1993560263798571009.json, 图片生成/图生图/flux2.0-去水印_1995432261795426305.json, 图片生成/图生图/flux2.0-去水印_1995756422661025793.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_35

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2单图编辑_1993878843299741698.json、图片生成/图生图/Flux2单图编辑flux最新图片编辑模型（支持中文））_1993552295038222338.json、图片生成/图生图/Flux2双图编辑_1993864960981794817.json、图片生成/图生图/WF28-Flux2DEV测试_1993560263798571009.json、图片生成/图生图/flux2.0-去水印_1995432261795426305.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `UnetLoaderGGUF` —— 5/6 个有
- `UNETLoader` —— 4/6 个有
- `ImageConcanate` —— 3/6 个有
- `load_GGUF` —— 3/6 个有
- `CR SDXL Aspect Ratio` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `easy imageSize` —— 1/6 个有
- `easy promptList` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
