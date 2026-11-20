---
name: image_to_image_lora_sampler_clip_108
type: Image To Image
frequency: 4
level: strong
coverage: 0.8115
common_nodes: [BatchCount+, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Muter (rgthree), Image Comparer (rgthree), ImageFromBatch, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, PreviewImage, PrimitiveInt, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy mathInt, easy rangeInt]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux_klein_+_SeedVR2.5.1_搭载高清放大lora_图像编辑法_细节修复_2087437139972808706.json, 平台全量/flux klein + SeedVR2.5.1  搭载高清放大lora_图像编辑法  细节修复_2048574895830863873.json, 平台全量/flux klein + SeedVR2.5.1 + 4宫格自动分块_2048989705114488834.json, 平台全量/小邵的究极klein高清修复_2039513970217852929.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_108

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux_klein_+_SeedVR2.5.1_搭载高清放大lora_图像编辑法_细节修复_2087437139972808706.json、平台全量/flux klein + SeedVR2.5.1  搭载高清放大lora_图像编辑法  细节修复_2048574895830863873.json、平台全量/flux klein + SeedVR2.5.1 + 4宫格自动分块_2048989705114488834.json、平台全量/小邵的究极klein高清修复_2039513970217852929.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `BatchCount+`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `PrimitiveInt`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy mathInt`
- `easy rangeInt`

**可变部分**（部分 workflow 才有）：
- `ImageTile+` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `easy imageSizeBySide` —— 3/4 个有
- `HAIGC_LoadImagesFromZip` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.6 - 1 | 4 | 81% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.1 - 1 | 4 | 50% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.6 - 1，4 个样本，取值集中（一致性 81%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，4 个样本，取值分散，一致性仅 50%
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
