---
name: image_to_image_lora_sampler_unet_185
type: Image To Image
frequency: 3
level: strong
coverage: 0.873667
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511-多视角_2004491947710578690.json, 图片生成/图生图/laoA 单姿态控制_2083568675835174913.json, 图片生成/图生图/qwen image edit 2509-图像编辑_1971041918497001474.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_185

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen2511-多视角_2004491947710578690.json、图片生成/图生图/laoA 单姿态控制_2083568675835174913.json、图片生成/图生图/qwen image edit 2509-图像编辑_1971041918497001474.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 2/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（12/3 个样本）：Steps较低可能导致细节不足
