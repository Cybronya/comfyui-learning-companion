---
name: image_to_image_upscale_sampler_clip_13
type: Image To Image
frequency: 9
level: moderate
coverage: 0.896556
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein-4k-8k高清放大_2012143815259332609.json, 图片生成/图生图/LH-DMT-018.wan2.2 ttp图像放大_2016184333878435842.json, 图片生成/图生图/QT106-TTP放大（Wan2.2）高清放大+细节修复，超真实_1956348858932580353.json, 图片生成/图生图/TTP-无损超清放大（优化版）_1952695000993828865.json, 图片生成/图生图/WAN 2.2  Upscaler_1965097044522188801.json, 图片生成/图生图/Wan2.2 - 14B  - TTP 图片放大 - 加速版_1991867139686723585.json, 图片生成/图生图/Wan2.2 - 14B -图片变清晰-效果好-速度快_1978337190512058369.json, 图片生成/图生图/Wan2.2 TTP高阶放大_1951113456193875969.json, 图片生成/图生图/Wan2.2+TTP放大_零变形不油腻_1950480608784994306.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein-4k-8k高清放大_2012143815259332609.json、图片生成/图生图/LH-DMT-018.wan2.2 ttp图像放大_2016184333878435842.json、图片生成/图生图/QT106-TTP放大（Wan2.2）高清放大+细节修复，超真实_1956348858932580353.json、图片生成/图生图/TTP-无损超清放大（优化版）_1952695000993828865.json、图片生成/图生图/WAN 2.2  Upscaler_1965097044522188801.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
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
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `ModelSamplingSD3` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `PreviewImage` —— 5/9 个有
- `easy cleanGpuUsed` —— 5/9 个有
- `Anything Everywhere3` —— 3/9 个有
- `Float` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `Anything Everywhere` —— 1/9 个有
- `BaiduTranslateNode` —— 1/9 个有
- `CFGZeroStar` —— 1/9 个有
- `ConstrainImage|pysssss` —— 1/9 个有
- `EasyCache` —— 1/9 个有
- `GLM_Vision_ImageToPrompt` —— 1/9 个有
- `ImageScaleDownToSize` —— 1/9 个有
- `Int` —— 1/9 个有
- `ModelPatchTorchSettings` —— 1/9 个有
- `PlaySound|pysssss` —— 1/9 个有
- `easy bookmark` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 10 | 9 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | heun | - | 9 | 67% |
| 调度器 | beta | - | 9 | 67% |
| 重绘幅度 | 0.1 | 0.08 - 0.3 | 9 | 49% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 10，9 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，9 个样本，一致性 67%
- 调度器 最常用 beta，9 个样本，一致性 67%
- 重绘幅度 中位数 0.1，观测区间 0.08 - 0.3，9 个样本，取值分散，一致性仅 49%
- 风险：重绘幅度 观测到 0.08，低于常用下限 0.1（）
