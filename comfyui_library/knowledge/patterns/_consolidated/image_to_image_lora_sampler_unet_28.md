---
name: image_to_image_lora_sampler_unet_28
type: Image To Image
frequency: 15
level: strong
coverage: 0.949133
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片编辑 改图_2112431618567794689.json, 图片生成/图生图/图片编辑姿势完美迁移_1970415639292747778.json, 图片生成/图生图/图生图 _ 场景角度切换_1996085406431166466.json, 图片生成/图生图/室内设计 建筑设计   效果图 渲染图_2060281824609390593.json, 图片生成/图生图/少儿_迁移_换装_抠图_runninghub简化版本_2077676821130338306.json, 图片生成/图生图/少儿_迁移_换装_抠图_runninghub简化版本_2079437242732474369.json, 图片生成/图生图/换背景Qwen+Image+Edit+2511-支持单图多图编辑加速版_2007308029473071105.json, 图片生成/图生图/换装千问Qwen2511最新图像编辑换装工作流_2084112989686427649.json, 图片生成/图生图/换装千问Qwen2511最新图像编辑换装工作流_2084124102578753538.json, 图片生成/图生图/换装千问qwen2511最新图像编辑_2008133174475366401.json, 图片生成/图生图/换装千问qwen2511最新图像编辑换装千问2511_2003636475113684993.json, 图片生成/图生图/换装千问qwen2511最新图像编辑换装千问2511_2100047371999735810.json, 图片生成/图生图/换装千问qwen2511最新图像编辑换装千问2511_2100125361475506178.json, 图片生成/图生图/生图-图换装手动遮罩-qwen-Edit-2509-8步_1983500012187492353.json, 图片生成/图生图/生图-图换装自动遮罩-qwen-Edit-2509-8步_1983510280296669186.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_28

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/图片编辑 改图_2112431618567794689.json、图片生成/图生图/图片编辑姿势完美迁移_1970415639292747778.json、图片生成/图生图/图生图 _ 场景角度切换_1996085406431166466.json、图片生成/图生图/室内设计 建筑设计   效果图 渲染图_2060281824609390593.json、图片生成/图生图/少儿_迁移_换装_抠图_runninghub简化版本_2077676821130338306.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 13/15 个有
- `CR Text` —— 13/15 个有
- `ModelSamplingAuraFlow` —— 13/15 个有
- `ImageConcanate` —— 12/15 个有
- `FluxKontextMultiReferenceLatentMethod` —— 9/15 个有
- `PreviewImage` —— 5/15 个有
- `TextEncodeQwenImageEdit` —— 5/15 个有
- `easy showAnything` —— 4/15 个有
- `AIO_Preprocessor` —— 3/15 个有
- `BackgroundEraseNetwork` —— 2/15 个有
- `ETN_LoadImageBase64` —— 2/15 个有
- `GetImageSizeAndCount` —— 2/15 个有
- `ImageAndMaskPreview` —— 2/15 个有
- `ImageResizeKJ` —— 2/15 个有
- `Int` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `StringFunction|pysssss` —— 2/15 个有
- `WD14Tagger|pysssss` —— 2/15 个有
- `easy seed` —— 2/15 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/15 个有
- `MaskPreview+` —— 1/15 个有
- `Qwen3_VQA_Plus` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 15 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 87% |
| 调度器 | simple | - | 15 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 87%
- 调度器 最常用 simple，15 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
