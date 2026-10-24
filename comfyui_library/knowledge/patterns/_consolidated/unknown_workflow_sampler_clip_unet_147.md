---
name: unknown_workflow_sampler_clip_unet_147
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9445
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein-9B-产品迁移完美细节多图编辑+放大_2012088188105400322.json, 图片生成/图生图/Flux2 Klein-多图编辑-4B加速版_2012124773035286530.json, 图片生成/图生图/Flux2 Klein去除水印9B版_2012705879501574145.json, 图片生成/图生图/Flux2 Klein图像编辑-9B版官方版（单图编辑）_2012123953627668482.json, 图片生成/图生图/Flux2-Klein+一键扩图_2013231626309869570.json, 图片生成/图生图/Flux2-klein 【扩图&局部重绘】_2013840320462594049.json, 图片生成/图生图/Flux2-klein 扩图&局部重绘_2013122024448729089.json, 图片生成/图生图/Flux2-klein 扩图_局部重绘_2013083035629002753.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_147

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein-9B-产品迁移完美细节多图编辑+放大_2012088188105400322.json、图片生成/图生图/Flux2 Klein-多图编辑-4B加速版_2012124773035286530.json、图片生成/图生图/Flux2 Klein去除水印9B版_2012705879501574145.json、图片生成/图生图/Flux2 Klein图像编辑-9B版官方版（单图编辑）_2012123953627668482.json、图片生成/图生图/Flux2-Klein+一键扩图_2013231626309869570.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `EmptyFlux2LatentImage` —— 7/8 个有
- `GetImageSize` —— 6/8 个有
- `ImageConcanate` —— 6/8 个有
- `ColorMatch` —— 4/8 个有
- `ImagePadForOutpaint` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `DrawMaskOnImage` —— 3/8 个有
- `easy seed` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `JWFloat` —— 2/8 个有
- `easy imageSize` —— 2/8 个有
- `BasicScheduler` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ImageSharpen` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LayerFilter: Sharp & Soft` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `MaskColorize` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有
- `图像缩放V2_孤海` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
