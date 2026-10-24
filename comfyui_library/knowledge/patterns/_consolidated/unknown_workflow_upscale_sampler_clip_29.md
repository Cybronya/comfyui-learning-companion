---
name: unknown_workflow_upscale_sampler_clip_29
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8506
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader_Any, CLIPTextEncode, ImageScaleBy, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImageJPG_GH, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/图片批量放大 上传压缩包 TTP分块放大   轻量版 zip-for循环批量_2083725440543449090.json, 图片生成/图生图/图片高清放大+全节点注释_2084521419387531266.json, 图片生成/图生图/高清放大 修复 TTP分块放大 轻量版_2091683311738515457.json, 视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088069964401041409.json, 视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088143314515226625.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图片批量放大 上传压缩包 TTP分块放大   轻量版 zip-for循环批量_2083725440543449090.json、图片生成/图生图/图片高清放大+全节点注释_2084521419387531266.json、图片生成/图生图/高清放大 修复 TTP分块放大 轻量版_2091683311738515457.json、视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088069964401041409.json、视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088143314515226625.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImageJPG_GH`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader_Any`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `Bjornulf_ShowInt` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RHBatchImages:` —— 1/5 个有
- `RHExtractImage` —— 1/5 个有
- `RHUploadZip` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有
- `easy imageCount` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
