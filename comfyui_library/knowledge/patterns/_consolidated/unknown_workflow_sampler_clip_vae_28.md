---
name: unknown_workflow_sampler_clip_vae_28
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.929429
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2单图编辑_1993878843299741698.json, 图片生成/图生图/Flux2单图编辑flux最新图片编辑模型（支持中文））_1993552295038222338.json, 图片生成/图生图/Flux2双图编辑_1993864960981794817.json, 图片生成/图生图/WF28-Flux2DEV测试_1993560263798571009.json, 图片生成/图生图/flux2.0-去水印_1995432261795426305.json, 图片生成/图生图/flux2.0-去水印_1995756422661025793.json, 图片生成/文生图/最新Flux 2.0文生图工作流（支持直接输入中文提示词）_1993538099806404610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_28

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux2单图编辑_1993878843299741698.json、图片生成/图生图/Flux2单图编辑flux最新图片编辑模型（支持中文））_1993552295038222338.json、图片生成/图生图/Flux2双图编辑_1993864960981794817.json、图片生成/图生图/WF28-Flux2DEV测试_1993560263798571009.json、图片生成/图生图/flux2.0-去水印_1995432261795426305.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
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
- `EmptyFlux2LatentImage` —— 6/7 个有
- `PreviewImage` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `UnetLoaderGGUF` —— 5/7 个有
- `ImageConcanate` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `load_GGUF` —— 3/7 个有
- `CR SDXL Aspect Ratio` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `easy promptList` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageStitch` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `easy imageSize` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
