---
name: unknown_workflow_sampler_clip_unet_206
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.88375
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/电商产品场景图生成_2065142735723646978.json, 图片生成/文生图/节点系列05-Seed (rgthree)_2034898646168248322.json, 平台全量/单图编辑 + 1张参考图（替换产品、服装、材质、背景）Flux2 Klein_2044764770087215105.json, 平台全量/单图编辑 + 2 张参考图（替换产品、服装、材质、背景）Flux2 Klein_2044767420467912705.json, 平台全量/单图编辑+ 局部重绘｜Flux2 Klein_2044714257614381058.json, 平台全量/单图编辑（去水印、产品精修、换材质、局部修改、人物美颜、替换背景）Flux2 Klein_2044763056986656770.json, 平台全量/图片-局部重绘_2022511882833235970.json, 平台全量/扩图 Flux2 Klein_2044771728571768833.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_206

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/电商产品场景图生成_2065142735723646978.json、图片生成/文生图/节点系列05-Seed (rgthree)_2034898646168248322.json、平台全量/单图编辑 + 1张参考图（替换产品、服装、材质、背景）Flux2 Klein_2044764770087215105.json、平台全量/单图编辑 + 2 张参考图（替换产品、服装、材质、背景）Flux2 Klein_2044767420467912705.json、平台全量/单图编辑+ 局部重绘｜Flux2 Klein_2044714257614381058.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `EmptyFlux2LatentImage` —— 5/8 个有
- `DifferentialDiffusion` —— 3/8 个有
- `InpaintModelConditioning` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `GetImageSize` —— 2/8 个有
- `AddLabel` —— 1/8 个有
- `ImagePadForOutpaint` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `MaskFillHoles` —— 1/8 个有
- `Qwen2.5` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `Text` —— 1/8 个有
- `easy convertAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
