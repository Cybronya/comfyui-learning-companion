---
name: image_to_image_sampler_clip_unet_72
type: Image To Image
frequency: 8
level: moderate
coverage: 0.958125
common_nodes: [CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/上传图片 2K 高清放大（zimage turbo）_2057112481067261953.json, 图片生成/图生图/图生图工作流77_2114259153182089217.json, 图片生成/图生图/图生图工作流77号｜通用图片再创作的高性价比之选_2114775665710026753.json, 平台全量/Qwen-Image-2k 高清放大_1955596688053321730.json, 平台全量/Qwen-Image-4k-8k高清放大_1955598061718441986.json, 平台全量/TTP分块高清放大细节修复，皮肤真实，保留细节，不失真 4 8k_2027979336116080641.json, 平台全量/TTP高清放大细节修复 精修 图像修复放大 真实细节增强 皮肤去AI_2034799841607421953.json, 平台全量/TTP高清放大细节修复_1963128953097662465.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/上传图片 2K 高清放大（zimage turbo）_2057112481067261953.json、图片生成/图生图/图生图工作流77_2114259153182089217.json、图片生成/图生图/图生图工作流77号｜通用图片再创作的高性价比之选_2114775665710026753.json、平台全量/Qwen-Image-2k 高清放大_1955596688053321730.json、平台全量/Qwen-Image-4k-8k高清放大_1955598061718441986.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 6/8 个有
- `UpscaleModelLoader` —— 6/8 个有
- `CLIPLoader` —— 5/8 个有
- `ImageScaleDownToSize` —— 5/8 个有
- `VAEDecode` —— 5/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `ImageListToImageBatch` —— 4/8 个有
- `ImageScaleBy` —— 4/8 个有
- `TTP_Image_Assy` —— 4/8 个有
- `TTP_Image_Tile_Batch` —— 4/8 个有
- `TTP_Tile_image_size` —— 4/8 个有
- `DualCLIPLoader` —— 3/8 个有
- `ImpactImageBatchToImageList` —— 3/8 个有
- `ModelSamplingAuraFlow` —— 3/8 个有
- `VAEDecodeTiled` —— 3/8 个有
- `BiRefNet_Loader_LG` —— 2/8 个有
- `CR Simple Image Compare` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `ImageCompare` —— 1/8 个有
- `easy imageBatchToImageList` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 20 | 8 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 0.895 | 0.1 - 1 | 8 | 41% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 20，8 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 0.895，观测区间 0.1 - 1，8 个样本，取值分散，一致性仅 41%
