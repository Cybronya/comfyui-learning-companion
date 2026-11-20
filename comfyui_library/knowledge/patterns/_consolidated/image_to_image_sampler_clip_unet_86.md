---
name: image_to_image_sampler_clip_unet_86
type: Image To Image
frequency: 7
level: weak
coverage: 0.826
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万相TTP_1964856835423485953.json, 图片生成/图生图/推荐提示词： 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一_1985251520163758082.json, 图片生成/图生图/放大-通用_1980921341337583617.json, 图片生成/图生图/👾怪獸-wan2.2高清修复-去AI感_添加细节👾_2014548216443834370.json, 平台全量/Qwen2511+wan2.2皮肤质感完美修复_2007377921459097602.json, 平台全量/WAN2.2人像超清放大工作流_1995064381052530689.json, 平台全量/Z-IMAGE毛孔级人像超清放大工作流_1995064294268133377.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_86

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/万相TTP_1964856835423485953.json、图片生成/图生图/推荐提示词： 【Wan2.2图像放大】 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像一_1985251520163758082.json、图片生成/图生图/放大-通用_1980921341337583617.json、图片生成/图生图/👾怪獸-wan2.2高清修复-去AI感_添加细节👾_2014548216443834370.json、平台全量/Qwen2511+wan2.2皮肤质感完美修复_2007377921459097602.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageUpscaleWithModel` —— 6/7 个有
- `ModelSamplingSD3` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `UpscaleModelLoader` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `GetNode` —— 4/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `CheckpointLoaderSimple` —— 3/7 个有
- `FluxGuidance` —— 3/7 个有
- `ImageFromBatch` —— 3/7 个有
- `PrimitiveFloat` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `ColorMatch` —— 2/7 个有
- `ImageBlend` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `SUPIR_conditioner` —— 2/7 个有
- `SUPIR_decode` —— 2/7 个有
- `SUPIR_encode` —— 2/7 个有
- `SUPIR_first_stage` —— 2/7 个有
- `SUPIR_model_loader_v2` —— 2/7 个有
- `SUPIR_sample` —— 2/7 个有
- `SeedVR2LoadDiTModel` —— 2/7 个有
- `SeedVR2LoadVAEModel` —— 2/7 个有
- `SeedVR2VideoUpscaler` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `QwenImageIntegratedKSampler` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 20 | 7 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 0.03 | 0.02 - 0.9 | 7 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 20，7 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 0.03，观测区间 0.02 - 0.9，7 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 0.02，低于常用下限 0.1（）
