---
name: unknown_workflow_inpaint_sampler_clip_3
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.677571
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), ImagePadForOutpaint, InpaintModelConditioning, KSamplerSelect, LanPaint_MaskBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 多图万能编辑工作流（局部重绘、扩图、单图、双图、三图编辑）_2012017503123283970.json, 图片生成/图生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2058397027016466433.json, 图片生成/图生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2100023809893031937.json, 图片生成/图生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2101484677134635010.json, 图片生成/图生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2102214802272776194.json, 图片生成/图生图/krea 2 and flux klein__文生图_2100026938537627650.json, 图片生成/图生图/krea 2 and flux klein__文生图_2100263128801038337.json, 图片生成/图生图/星绘-Flux2+Klein整合_2013197385870090242.json, 图片生成/文生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2014259943414697985.json, 图片生成/文生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图自用_2012776375110868994.json, 图片生成/文生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2098909534654914562.json, 图片生成/文生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2098971198804807681.json, 图片生成/文生图/YZ金鱼-Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2012136788260823041.json, 图片生成/文生图/krea_2_and_flux_klein_文生图_2_2101081616683716610.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 多图万能编辑工作流（局部重绘、扩图、单图、双图、三图编辑）_2012017503123283970.json、图片生成/图生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2058397027016466433.json、图片生成/图生图/Flux2 Klein 超级多合一_文生图、单图多图编辑、重绘、完美扩图_2100023809893031937.json、图片生成/图生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2101484677134635010.json、图片生成/图生图/Flux2_Klein_超级多合一_文生图、单图多图编辑、重绘、完美扩图_2102214802272776194.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSamplerSelect`
- `LanPaint_MaskBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 13/14 个有
- `Fast Groups Bypasser (rgthree)` —— 13/14 个有
- `ImageScaleToTotalPixels` —— 13/14 个有
- `SeedVR2LoadDiTModel` —— 13/14 个有
- `SeedVR2LoadVAEModel` —— 13/14 个有
- `SeedVR2VideoUpscaler` —— 13/14 个有
- `easy cleanGpuUsed` —— 13/14 个有
- `GetNode` —— 12/14 个有
- `PlaySound|pysssss` —— 12/14 个有
- `SetNode` —— 12/14 个有
- `EmptyImage` —— 2/14 个有
- `CR Text Input Switch (4 way)` —— 1/14 个有
- `MuyeSizeSelector` —— 1/14 个有
- `TextInput_` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
