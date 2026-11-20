---
name: unknown_workflow_sampler_clip_unet_189
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.89075
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/三图参考加强版-Flux2-Klein_9B_2115621365150740482.json, 图片生成/图生图/三图参考加强版-Flux2-Klein_9B_2115668590069374977.json, 图片生成/图生图/常用_图片_flux2_单图_2037742922816299009.json, 图片生成/图生图/生产力-flux2_klein单图+多图参考_2013052924347289602.json, 图片生成/图生图/自拍照+服装参考图一键生成证件照_2020047100834226178.json, 图片生成/文生图/danotebook-flux2-klein-9b_2062427994236481537.json, 平台全量/三图参考加强版-Flux2-Klein_9B_2114520255337943041.json, 视频生成/图生视频/三图参考加强版-Flux2-Klein_9B_2115291153124909057.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_189

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/三图参考加强版-Flux2-Klein_9B_2115621365150740482.json、图片生成/图生图/三图参考加强版-Flux2-Klein_9B_2115668590069374977.json、图片生成/图生图/常用_图片_flux2_单图_2037742922816299009.json、图片生成/图生图/生产力-flux2_klein单图+多图参考_2013052924347289602.json、图片生成/图生图/自拍照+服装参考图一键生成证件照_2020047100834226178.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
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
- `GetImageSize` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `ComfySwitchNode` —— 5/8 个有
- `BatchImagesNode` —— 4/8 个有
- `CreateBoundingBoxes` —— 4/8 个有
- `Flux3LayoutPrompt` —— 4/8 个有
- `ImageCASharpening+` —— 4/8 个有
- `PreviewAny` —— 4/8 个有
- `TextGenerate` —— 4/8 个有
- `PrimitiveString` —— 2/8 个有
- `PrimitiveInt` —— 1/8 个有
- `StringCompare` —— 1/8 个有
- `StringReplace` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
