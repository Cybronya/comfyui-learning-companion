---
name: image_to_image_upscale_sampler_clip_44
type: Image To Image
frequency: 3
level: strong
coverage: 0.886
common_nodes: [CLIPTextEncode, ConditioningZeroOut, GetImageSize, INTConstant, Image Comparer (rgthree), ImageListToBatch+, ImageUpscaleWithModel, KSampler, LoadImage, MathExpression|pysssss, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, VAEDecode, VAEEncode, easy imageBatchToImageList, easy imageScaleDownToSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Anima-琉璃4K动漫洗图工作流（带模型和节点下载链接）_2100872011168964610.json, 图片生成/图生图/动漫_二次元_cartoon 放大 upscale_2101669053529149442.json, 平台全量/豹豹喵呜制作：动漫图专门超分放大_2099696926848540673.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Anima-琉璃4K动漫洗图工作流（带模型和节点下载链接）_2100872011168964610.json、图片生成/图生图/动漫_二次元_cartoon 放大 upscale_2101669053529149442.json、平台全量/豹豹喵呜制作：动漫图专门超分放大_2099696926848540673.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageListToBatch+`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `MathExpression|pysssss`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `easy imageBatchToImageList`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `AnimaBoosterCheckpointLoader` —— 2/3 个有
- `AnimaTeaCache` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `JoinStrings` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | kl_optimal | - | 3 | 100% |
| 重绘幅度 | 0.45 | 0.45 - 0.45 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 kl_optimal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 0.45，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
