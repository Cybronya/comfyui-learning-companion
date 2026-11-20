---
name: image_to_image_inpaint_lora_sampler
type: Image To Image
frequency: 8
level: strong
coverage: 0.813375
common_nodes: [CLIPLoader, ConditioningZeroOut, CreateShapeMask, GrowMaskWithBlur, ImageBlend, ImageConcanate, ImagePadForOutpaint, ImageResizeKJv2, ImageScaleToTotalPixels, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/360_2031667084123443202.json, 图片生成/图生图/360全景图生成+TTP放大+全自动接缝_2018589222394929154.json, 图片生成/图生图/一键 图片 转 360全景图_2059073213757485058.json, 图片生成/图生图/一键+图片+转+360全景图_2096562014134030337.json, 图片生成/图生图/一键+图片+转+360全景图_2104866199501893634.json, 图片生成/图生图/一键+图片+转+360全景图_2110206285751869442.json, 图片生成/图生图/图片转360全景图，效果完美，无瑕疵_2052271703472001026.json, 图片生成/图生图/图生图 一键 图片 转 360全景图_2063870262696824833.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/360_2031667084123443202.json、图片生成/图生图/360全景图生成+TTP放大+全自动接缝_2018589222394929154.json、图片生成/图生图/一键 图片 转 360全景图_2059073213757485058.json、图片生成/图生图/一键+图片+转+360全景图_2096562014134030337.json、图片生成/图生图/一键+图片+转+360全景图_2104866199501893634.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CreateShapeMask`
- `GrowMaskWithBlur`
- `ImageBlend`
- `ImageConcanate`
- `ImagePadForOutpaint`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/8 个有
- `LayerUtility: If ` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `SeedVR2LoadDiTModel` —— 5/8 个有
- `SeedVR2LoadVAEModel` —— 5/8 个有
- `SeedVR2VideoUpscaler` —— 5/8 个有
- `SimpleComparison+` —— 5/8 个有
- `CLIPTextEncode` —— 3/8 个有
- `ConstrainImage|pysssss` —— 3/8 个有
- `EmptySD3LatentImage` —— 3/8 个有
- `ImageUpscaleWithModel` —— 3/8 个有
- `PanoramaViewerNode` —— 3/8 个有
- `PrimitiveFloat` —— 3/8 个有
- `PrimitiveInt` —— 3/8 个有
- `UpscaleModelLoader` —— 3/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（22/8 个样本）：Steps较低可能导致细节不足
