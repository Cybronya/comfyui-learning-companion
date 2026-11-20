---
name: unknown_workflow_sampler_clip_unet_149
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.904125
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImagePadForOutpaint, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/图生图/Flux2-klein 扩图_局部重绘_2013083035629002753.json, 图片生成/图生图/flux 2 klein 无缝扩图+局部重绘_2017924280838791170.json, 图片生成/图生图/klein 扩图_2018209439236493313.json, 图片生成/图生图/klein 扩图_局部重绘_2012965333056888833.json, 图片生成/图生图/klein 扩图_局部重绘_2016153153808371714.json, 图片生成/图生图/klein单图编辑_2014331376341880834.json, 图片生成/图生图/klein单图编辑_2026469050368397313.json, 图片生成/图生图/klein扩图工作流_2013942199481798658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_149

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux2-klein 扩图_局部重绘_2013083035629002753.json、图片生成/图生图/flux 2 klein 无缝扩图+局部重绘_2017924280838791170.json、图片生成/图生图/klein 扩图_2018209439236493313.json、图片生成/图生图/klein 扩图_局部重绘_2012965333056888833.json、图片生成/图生图/klein 扩图_局部重绘_2016153153808371714.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
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
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 7/8 个有
- `ColorMatch` —— 6/8 个有
- `DrawMaskOnImage` —— 5/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `BasicScheduler` —— 1/8 个有
- `CustomAddLabel` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ImageSharpen` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LayerFilter: Sharp & Soft` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `图像缩放V2_孤海` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
