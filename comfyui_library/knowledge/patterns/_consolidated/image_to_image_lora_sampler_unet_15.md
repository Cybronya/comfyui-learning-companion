---
name: image_to_image_lora_sampler_unet_15
type: Image To Image
frequency: 21
level: strong
coverage: 0.851286
common_nodes: [CLIPLoader, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/[🛫书墨]小红书FireRed-Image-edit1.1_一至三图任意切换_2029240103347949569.json, 图片生成/图生图/[🛬书墨]FireRed-Image-edit1.0全能1-3图自由切换编辑_2023016122932531202.json, 图片生成/图生图/小红书FireRed Image Edit 1.1 多图编辑加速版｜模特换装｜换场景｜换颜色_2049307280159547394.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029246391024881666.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029367604804067329.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511 单图_2029491702288879617.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511(化妆)_2029500931573817345.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 VS aio 2511（文字排版）_2029499925364482049.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 单图双图三图编辑_2029911022823280641.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑（文字排版参考）_2029575105692573697.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑（文字排版参考）_2030166401742282754.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 文字排版_2029759015185551362.json, 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致性）_2029575084368728065.json, 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致性）_2029727437268979713.json, 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致）_2029741910889336833.json, 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑（换装）_2029575073815863298.json, 图片生成/图生图/小红书FireRed-Image-edit1.1图像编辑（妆容迁移）_2029575093277433858.json, 图片生成/图生图/小红书FireRed-Image-edit1.1妆容迁移_2029746671227248641.json, 图片生成/图生图/小红书FireRed批量换装_2046756130541539330.json, 图片生成/图生图/（好用）小红书FireRed-Image-edit1.1双图编辑（情趣换装）_2030162350132695041.json, 图片生成/文生图/2029537706899935234.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_15

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/[🛫书墨]小红书FireRed-Image-edit1.1_一至三图任意切换_2029240103347949569.json、图片生成/图生图/[🛬书墨]FireRed-Image-edit1.0全能1-3图自由切换编辑_2023016122932531202.json、图片生成/图生图/小红书FireRed Image Edit 1.1 多图编辑加速版｜模特换装｜换场景｜换颜色_2049307280159547394.json、图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029246391024881666.json、图片生成/图生图/小红书FireRed-Image-edit1.1 8步加速版图像编辑V1_2029367604804067329.json…）

- **类型**：Image To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 20/21 个有
- `CFGNorm` —— 20/21 个有
- `ModelSamplingAuraFlow` —— 20/21 个有
- `PreviewImage` —— 20/21 个有
- `CR Prompt Text` —— 19/21 个有
- `easy cleanGpuUsed` —— 16/21 个有
- `Fast Groups Muter (rgthree)` —— 15/21 个有
- `AddLabel` —— 7/21 个有
- `CR Image Grid Panel` —— 7/21 个有
- `Image Batch` —— 7/21 个有
- `KOOK_SaveJPGImage` —— 7/21 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 7/21 个有
- `CheckpointLoaderSimple` —— 4/21 个有
- `CR SDXL Aspect Ratio` —— 2/21 个有
- `PrimitiveStringMultiline` —— 2/21 个有
- `HAIGC_LoadImagesFromZip` —— 1/21 个有
- `RH_BatchImages` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 21 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 21 | 100% |
| 采样算法 | euler | - | 21 | 81% |
| 调度器 | simple | - | 21 | 76% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，21 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，21 个样本，一致性 81%
- 调度器 最常用 simple，21 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（21/21 个样本）：Steps较低可能导致细节不足
