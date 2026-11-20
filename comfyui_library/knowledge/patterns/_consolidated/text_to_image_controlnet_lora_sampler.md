---
name: text_to_image_controlnet_lora_sampler
type: Text To Image
frequency: 8
level: moderate
coverage: 0.863
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图像一键编程90年代日漫风格_1923634243497619457.json, 图片生成/图生图/图生图 单视觉参考+构图参考_1986614589536272386.json, 图片生成/图生图/复古动漫风格_1909619588206686210.json, 图片生成/图生图/情侣婚纱照片转手绘豆豆眼风格_1935914145080668162.json, 图片生成/图生图/高清照片转手绘豆豆眼风格_2026918149987241985.json, 图片生成/图生图/高清照片转手绘豆豆眼风格_2030526642736599042.json, 图片生成/文生图/FLUX人物模特智能反推图生图Controlnet可控生成统一风格_1919597654442184705.json, 图片生成/文生图/照片风格_1938147090012749826.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/图像一键编程90年代日漫风格_1923634243497619457.json、图片生成/图生图/图生图 单视觉参考+构图参考_1986614589536272386.json、图片生成/图生图/复古动漫风格_1909619588206686210.json、图片生成/图生图/情侣婚纱照片转手绘豆豆眼风格_1935914145080668162.json、图片生成/图生图/高清照片转手绘豆豆眼风格_2026918149987241985.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `UpscaleModelLoader` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `ImageUpscaleWithModel` —— 4/8 个有
- `InspyrenetRembg` —— 4/8 个有
- `LayerUtility: ImageBlendAdvance V3` —— 4/8 个有
- `Preview from image [Crystools]` —— 4/8 个有
- `RHHiddenNodes` —— 4/8 个有
- `DifferentialDiffusion` —— 3/8 个有
- `UltimateSDUpscale` —— 2/8 个有
- `ConditioningCombine` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `InstructPixToPixConditioning` —— 1/8 个有
- `WD14Tagger|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 8 | 71% |
| 高度 | 512 | 512 - 1448 | 8 | 51% |
| 采样步数 | 25 | 20 - 28 | 8 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | normal | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| ControlNet 权重 | 0.6 | 0.6 - 1.5 | 8 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，8 个样本
- 高度 中位数 512，观测区间 512 - 1448，8 个样本
- 采样步数 中位数 25，观测区间 20 - 28，8 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 normal，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，观测区间 0.6 - 1.5，8 个样本
