---
name: unknown_workflow_sampler_clip_unet_275
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.76775
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, Image Comparer (rgthree), KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/FLUX-图生图-TTP4K、8K放大_1905644946848944129.json, 图片生成/图生图/FLUX超大图分块优化_2005076783177367554.json, 图片生成/图生图/【 Banan美甲定制】香蕉图像编辑-TTP高清放大_1967708079838158849.json, 图片生成/图生图/小图变2k、4k、6k、8k无限放大_1916024025137479681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_275

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX-图生图-TTP4K、8K放大_1905644946848944129.json、图片生成/图生图/FLUX超大图分块优化_2005076783177367554.json、图片生成/图生图/【 Banan美甲定制】香蕉图像编辑-TTP高清放大_1967708079838158849.json、图片生成/图生图/小图变2k、4k、6k、8k无限放大_1916024025137479681.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `easy imageListToImageBatch` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `ImageListToBatch+` —— 1/4 个有
- `Load Image Batch` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `RH_Nano_Banana_Image2Image` —— 1/4 个有
- `RH_Translator` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
