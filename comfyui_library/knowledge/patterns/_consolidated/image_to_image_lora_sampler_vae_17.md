---
name: image_to_image_lora_sampler_vae_17
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9508
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen换装_1972259814439055362.json, 图片生成/图生图/qwen真人转网红手办_3D_盲盒手办_效果堪比Naon 全能图片V1_1989295548085751810.json, 图片生成/图生图/☯️千问QUYI-DIY换装流_1978128358280159234.json, 图片生成/图生图/【乐导】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1992133522697809922.json, 图片生成/图生图/【阡陌】Qwen-Image-Edit-2509升级Plus版人物姿态控制_1971193309135851522.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_17

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/qwen换装_1972259814439055362.json、图片生成/图生图/qwen真人转网红手办_3D_盲盒手办_效果堪比Naon 全能图片V1_1989295548085751810.json、图片生成/图生图/☯️千问QUYI-DIY换装流_1978128358280159234.json、图片生成/图生图/【乐导】Qwen-Image-Edit-2509升级Plus版nunchaku加速_1992133522697809922.json、图片生成/图生图/【阡陌】Qwen-Image-Edit-2509升级Plus版人物姿态控制_1971193309135851522.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 4/5 个有
- `CFGNorm` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `TextEncodeQwenImageEdit` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `EmptyLatentImage` —— 2/5 个有
- `NunchakuQwenImageDiTLoader` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `DWPreprocessor` —— 1/5 个有
- `GLM_Vision_ImageToPrompt` —— 1/5 个有
- `JWImageResizeByLongerSide` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 5 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
