---
name: image_to_image_upscale_sampler_clip_32
type: Image To Image
frequency: 5
level: weak
coverage: 0.8958
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan2.2图生图高质量_1987726436859621378.json, "图片生成/图生图/wan2.2高清放大修复高质量,4K_1983123878350352386.json", 图片生成/图生图/（高清放大）Wan2.2 - 14B - 加速版 -  图片高清放大_1977811440935600129.json, 平台全量/Z-image生图洗图线稿控制_1982391899568906241.json, 平台全量/图片高清修复wan2.2_1986341262846558209.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/wan2.2图生图高质量_1987726436859621378.json、图片生成/图生图/wan2.2高清放大修复高质量,4K_1983123878350352386.json、图片生成/图生图/（高清放大）Wan2.2 - 14B - 加速版 -  图片高清放大_1977811440935600129.json、平台全量/Z-image生图洗图线稿控制_1982391899568906241.json、平台全量/图片高清修复wan2.2_1986341262846558209.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
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
- `LoraLoaderModelOnly` —— 4/5 个有
- `ModelSamplingSD3` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `SaveImagePlus` —— 3/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `Text Concatenate` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `workflow>wan2.2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 5 - 10 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 12 | 5 | 0% |
| 采样算法 | heun | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 0.1 | 0.01 - 0.1 | 4 | 50% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 5 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 12，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 heun，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 0.1，观测区间 0.01 - 0.1，4 个样本，取值分散，一致性仅 50%
- 风险：重绘幅度 观测到 0.01，低于常用下限 0.1（）
