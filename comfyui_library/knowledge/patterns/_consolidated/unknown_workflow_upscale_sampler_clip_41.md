---
name: unknown_workflow_upscale_sampler_clip_41
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.775
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader_Any, CLIPTextEncode, ImageScaleBy, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImageJPG_GH, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/图片批量放大 上传压缩包 TTP分块放大   轻量版 zip-for循环批量_2083725440543449090.json, 图片生成/图生图/图片高清放大+全节点注释_2084521419387531266.json, 图片生成/图生图/高清放大 修复 TTP分块放大 轻量版_2091683311738515457.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图片批量放大 上传压缩包 TTP分块放大   轻量版 zip-for循环批量_2083725440543449090.json、图片生成/图生图/图片高清放大+全节点注释_2084521419387531266.json、图片生成/图生图/高清放大 修复 TTP分块放大 轻量版_2091683311738515457.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
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
- `LoadImage` —— 2/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RHBatchImages:` —— 1/3 个有
- `RHExtractImage` —— 1/3 个有
- `RHUploadZip` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy imageCount` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
