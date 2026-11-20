---
name: image_to_image_sampler_clip_unet_122
type: Image To Image
frequency: 4
level: weak
coverage: 0.83775
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingSD3, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万相TTP_1964856835423485953.json, 图片生成/图生图/推荐提示词： 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一_1985251520163758082.json, 图片生成/图生图/放大-通用_1980921341337583617.json, 图片生成/图生图/👾怪獸-wan2.2高清修复-去AI感_添加细节👾_2014548216443834370.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_122

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/万相TTP_1964856835423485953.json、图片生成/图生图/推荐提示词： 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一_1985251520163758082.json、图片生成/图生图/放大-通用_1980921341337583617.json、图片生成/图生图/👾怪獸-wan2.2高清修复-去AI感_添加细节👾_2014548216443834370.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `Anything Everywhere3` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `FluxGuidance` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 20 | 4 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.065 | 0.02 - 0.5 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 20，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.065，观测区间 0.02 - 0.5，4 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 0.02，低于常用下限 0.1（）
