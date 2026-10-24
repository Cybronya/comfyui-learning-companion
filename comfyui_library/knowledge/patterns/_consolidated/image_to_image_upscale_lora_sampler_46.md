---
name: image_to_image_upscale_lora_sampler_46
type: Image To Image
frequency: 4
level: moderate
coverage: 0.90575
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/产品融图-kontext_1948722789718077441.json, 图片生成/图生图/产品融图-kontext_1953038923623821313.json, 图片生成/图生图/线稿生成效果图（建筑）线稿，概念建筑生成_1982702923677351938.json, 图片生成/图生图/高清修复测试版v1_1955086321104687106.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/产品融图-kontext_1948722789718077441.json、图片生成/图生图/产品融图-kontext_1953038923623821313.json、图片生成/图生图/线稿生成效果图（建筑）线稿，概念建筑生成_1982702923677351938.json、图片生成/图生图/高清修复测试版v1_1955086321104687106.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `ConstrainImage|pysssss` —— 3/4 个有
- `LayerMask: LoadFlorence2Model` —— 3/4 个有
- `LayerUtility: Florence2Image2Prompt` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `ChinesePrompt_Mix` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Float` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `Text` —— 2/4 个有
- `ImageScale` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `Int` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `Text _O` —— 1/4 个有
- `TextInput_` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 4 | 0% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.5 - 1 | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，4 个样本
