---
name: unknown_workflow_sampler_unet_vae_184
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9415
common_nodes: [CFGGuider, CLIPLoader, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json, 图片生成/图生图/参考风格生成效果图_2030619395935965186.json, 图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json, 图片生成/图生图/双模放大_2076211416096399362.json, 图片生成/图生图/发型迁移与更换_2051141221707468801.json, 图片生成/图生图/渲染级产品精修V5 +自动白底 +细节增强_2084924306483666945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_184

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json、图片生成/图生图/参考风格生成效果图_2030619395935965186.json、图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json、图片生成/图生图/双模放大_2076211416096399362.json、图片生成/图生图/发型迁移与更换_2051141221707468801.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `CLIPTextEncode` —— 4/6 个有
- `ReferenceLatent` —— 4/6 个有
- `VAEEncode` —— 4/6 个有
- `EmptyFlux2LatentImage` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `GetImageSize` —— 2/6 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CR Text Input Switch (4 way)` —— 1/6 个有
- `DapaoImageAspectRatioResizeNode` —— 1/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `ImageInvert` —— 1/6 个有
- `JoinImageWithAlpha` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SAM3Segment` —— 1/6 个有
- `TEEDPreprocessor` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
