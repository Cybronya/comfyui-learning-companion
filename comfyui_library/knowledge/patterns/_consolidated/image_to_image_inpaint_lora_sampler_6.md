---
name: image_to_image_inpaint_lora_sampler_6
type: Image To Image
frequency: 4
level: strong
coverage: 0.86775
common_nodes: [AIO_Preprocessor, CFGNorm, CLIPLoader, ConditioningZeroOut, GetImageSize, GrowMaskWithBlur, ImageConcanate, ImageResizeKJ, ImageResizeKJv2, ImageScaleToTotalPixels, InpaintPreprocessor, KSampler, LayerMask: LoadSegmentAnythingModels, LayerMask: ObjectDetectorMask, LayerMask: SAM2Ultra, LayerMask: SegmentAnythingUltra V3, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, SaveImage, Text, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN2509完美姿势迁移工作流_1984507565964935170.json, 图片生成/图生图/Qwen-Edit 2509：姿势迁移终极解决方案，一键摆拍，动作完美复刻！_1984471217027629058.json, 图片生成/图生图/Qwen-Image-Edit 2509姿势迁移_1988082283074793474.json, 图片生成/图生图/Qwen2509姿势迁移_1995445193992232961.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QWEN2509完美姿势迁移工作流_1984507565964935170.json、图片生成/图生图/Qwen-Edit 2509：姿势迁移终极解决方案，一键摆拍，动作完美复刻！_1984471217027629058.json、图片生成/图生图/Qwen-Image-Edit 2509姿势迁移_1988082283074793474.json、图片生成/图生图/Qwen2509姿势迁移_1995445193992232961.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetImageSize`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `InpaintPreprocessor`
- `KSampler`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: ObjectDetectorMask`
- `LayerMask: SAM2Ultra`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `easy imageColorMatch` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
