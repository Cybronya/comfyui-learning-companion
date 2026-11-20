---
name: unknown_workflow_upscale_sampler_clip_33
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8165
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader_Any, CLIPTextEncode, ImageScaleBy, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImageJPG_GH, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/图片批量放大 上传压缩包 TTP分块放大   轻量版 zip-for循环批量_2083725440543449090.json, 图片生成/图生图/图片高清放大+全节点注释_2084521419387531266.json, 图片生成/图生图/高清放大 修复 TTP分块放大 轻量版_2091683311738515457.json, 平台全量/flux2-klein-TTP分块放大 _ 轻量版 不匹配颜色【zip-for循环批量】_1938368846430408706.json, 平台全量/flux2-klein-TTP分块放大 _ 轻量版【zip-for循环批量】_1890329820201623553.json, 平台全量/消除水印+放大+zip批量_2090790263458455554.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/图片批量放大 上传压缩包 TTP分块放大   轻量版 zip-for循环批量_2083725440543449090.json、图片生成/图生图/图片高清放大+全节点注释_2084521419387531266.json、图片生成/图生图/高清放大 修复 TTP分块放大 轻量版_2091683311738515457.json、平台全量/flux2-klein-TTP分块放大 _ 轻量版 不匹配颜色【zip-for循环批量】_1938368846430408706.json、平台全量/flux2-klein-TTP分块放大 _ 轻量版【zip-for循环批量】_1890329820201623553.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
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
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `easy imageColorMatch` —— 5/6 个有
- `Bjornulf_ShowInt` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `RHBatchImages:` —— 4/6 个有
- `RHExtractImage` —— 4/6 个有
- `RHUploadZip` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `easy forLoopEnd` —— 4/6 个有
- `easy forLoopStart` —— 4/6 个有
- `easy imageCount` —— 4/6 个有
- `LoadImage` —— 3/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `ConstrainImage|pysssss` —— 1/6 个有
- `DualCLIPLoader` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `KSampler` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `UNETLoader` —— 1/6 个有
- `VAELoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
