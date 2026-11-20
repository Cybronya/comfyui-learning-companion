---
name: unknown_workflow_generic_466
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.747833
common_nodes: [ImageScale, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide]
problems: []
missing: []
members: [图片生成/图生图/seedVR2 GGUF版本（低显存且放大参数高于6k时使用）——适用于高清的增加细节+全节点注释_2054878600821788673.json, 图片生成/图生图/seedVR2 原模分块版本（放大参数高于4k时使用）——适用于不清晰的+全节点注释_2054878680249315330.json, 图片生成/图生图/seedVR2_原模分块版本放大参数高于4k时使用-适用于不清晰的_2055544526051266562.json, 图片生成/图生图/seedvr2 超高清无损放大_1967443133325828098.json, 图片生成/图生图/seedvr2放大_1986367857825087490.json, 图片生成/图生图/啊癫 SeedVR2图像高清放大流_1971202743803297794.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_466

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/seedVR2 GGUF版本（低显存且放大参数高于6k时使用）——适用于高清的增加细节+全节点注释_2054878600821788673.json、图片生成/图生图/seedVR2 原模分块版本（放大参数高于4k时使用）——适用于不清晰的+全节点注释_2054878680249315330.json、图片生成/图生图/seedVR2_原模分块版本放大参数高于4k时使用-适用于不清晰的_2055544526051266562.json、图片生成/图生图/seedvr2 超高清无损放大_1967443133325828098.json、图片生成/图生图/seedvr2放大_1986367857825087490.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 5/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `PlaySound|pysssss` —— 3/6 个有
- `SeedVR2` —— 3/6 个有
- `SeedVR2GGUF` —— 3/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
