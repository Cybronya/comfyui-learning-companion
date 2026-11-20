---
name: image_to_image_upscale_lora_sampler_33
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8664
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Joy3反推提示词+Wan2.2TTP细节增强放大_1951297958203609090.json, 图片生成/图生图/LH-DMT-019.wan-NMKD人像高清放大-NF_2016194808208957442.json, 图片生成/图生图/Wan2.2TTP图像细节增强放大_1951193407014248449.json, 图片生成/图生图/高清修复(wan2.2)-去AI感_添加细节_1953713018205032450.json, 数字人/数字人/高清修复(wan2.2)-去AI感_添加细节_2103481336999800834.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Joy3反推提示词+Wan2.2TTP细节增强放大_1951297958203609090.json、图片生成/图生图/LH-DMT-019.wan-NMKD人像高清放大-NF_2016194808208957442.json、图片生成/图生图/Wan2.2TTP图像细节增强放大_1951193407014248449.json、图片生成/图生图/高清修复(wan2.2)-去AI感_添加细节_1953713018205032450.json、数字人/数字人/高清修复(wan2.2)-去AI感_添加细节_2103481336999800834.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `Florence2ModelLoader` —— 3/5 个有
- `Florence2Run` —— 3/5 个有
- `FluxGuidance` —— 3/5 个有
- `ImageFromBatch` —— 3/5 个有
- `InjectLatentNoise+` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/5 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/5 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | beta | - | 5 | 40% |
| 重绘幅度 | 0.05 | 0.05 - 0.1 | 5 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 40%
- 重绘幅度 中位数 0.05，观测区间 0.05 - 0.1，5 个样本
- 风险：重绘幅度 观测到 0.05，低于常用下限 0.1（）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
