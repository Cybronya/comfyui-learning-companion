---
name: unknown_workflow_generic_1576
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7205
common_nodes: [DF_Integer, Image Comparer (rgthree), ImageCASharpening+, ImageListToImageBatch, ImpactMinMax, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RHHiddenNodes, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy cleanGpuUsed, easy clearCacheAll, easy imageBatchToImageList, easy imageSize, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/迄今商用级极速8K高清放大！万物低像素图去AI感，保持肌肤质感输出画质（2K_4K_6K_8K可选）_1965312373458391041.json, 图片生成/图生图/迄今图修复画质SeedVR2+Tile分块万物图像完美修复放大，完美人物一致性，复现原图中文等细节✨_1960509771155763201.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1576

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/迄今商用级极速8K高清放大！万物低像素图去AI感，保持肌肤质感输出画质（2K_4K_6K_8K可选）_1965312373458391041.json、图片生成/图生图/迄今图修复画质SeedVR2+Tile分块万物图像完美修复放大，完美人物一致性，复现原图中文等细节✨_1960509771155763201.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `DF_Integer`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageListToImageBatch`
- `ImpactMinMax`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
