---
name: text_to_image_lora_sampler_clip_202
type: Text To Image
frequency: 9
level: strong
coverage: 0.851333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Get Image Size, ImageMergeTileList, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PrimitiveInt, SaveImage, SeedVR2, SplitImageToTileList, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/907一阶段放大不缩尺寸｜透明背景高清输出_2097151874083414018.json, 图片生成/图生图/913-VO+SE不透明版图生图｜913当天调试成品，参数锁定即取即用_2099529599943270402.json, 图片生成/图生图/913-VO+SE透明板版本｜透明通道保留完整，图生图后期好接手_2099531547643830273.json, 图片生成/图生图/999-vo+se不透明版图生图｜参数调好的成品流，导入即用不折腾_2099507003130466305.json, 图片生成/图生图/VO+SE不透明版图生图 视频叠加不透明效果处理_2099206060946051073.json, 图片生成/图生图/VO+SE透明版图生图 视频叠加透明效果处理工具_2099207580798251009.json, 图片生成/图生图/一阶段放大不缩小透明处理｜907图生图高清增强_2097095626621280258.json, 图片生成/图生图/图生图｜1.5到4倍无损放大，海分专用画质增强_2099889777045753857.json, 图片生成/图生图/透明背景放大3倍处理｜ESR高清画质增强图生图_2096706574864703489.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_202

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/907一阶段放大不缩尺寸｜透明背景高清输出_2097151874083414018.json、图片生成/图生图/913-VO+SE不透明版图生图｜913当天调试成品，参数锁定即取即用_2099529599943270402.json、图片生成/图生图/913-VO+SE透明板版本｜透明通道保留完整，图生图后期好接手_2099531547643830273.json、图片生成/图生图/999-vo+se不透明版图生图｜参数调好的成品流，导入即用不折腾_2099507003130466305.json、图片生成/图生图/VO+SE不透明版图生图 视频叠加不透明效果处理_2099206060946051073.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Get Image Size`
- `ImageMergeTileList`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2`
- `SplitImageToTileList`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImpactMinMax` —— 7/9 个有
- `Int` —— 7/9 个有
- `LayerUtility: BooleanOperatorV2` —— 7/9 个有
- `easy ifElse` —— 7/9 个有
- `JoinImageWithAlpha` —— 6/9 个有
- `VOSR2ModelLoader` —— 5/9 个有
- `VOSR2Upscale` —— 5/9 个有
- `孤海-图像添加水印` —— 4/9 个有
- `ImageResize+` —— 3/9 个有
- `ImageUpscaleWithModel` —— 3/9 个有
- `LayerUtility: PurgeVRAM` —— 3/9 个有
- `UpscaleModelLoader` —— 3/9 个有
- `easy boolean` —— 3/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
