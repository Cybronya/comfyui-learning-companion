---
name: image_to_image_lora_sampler_vae_16
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9154
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ygd生图-多图生成多角度-QwenEdit_1988117156808269826.json, 图片生成/图生图/一键转绘-Qwen-Image-Edit图像编辑_2031200944762916865.json, 图片生成/图生图/人物多角度一键生成《Next Scene》_1984265817120522242.json, 图片生成/图生图/按尺寸扩图_2054365264153718786.json, 图片生成/图生图/生图-动漫转真人-qwen-Edit-anything2real-2511-8步_2008107492974272513.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_16

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ygd生图-多图生成多角度-QwenEdit_1988117156808269826.json、图片生成/图生图/一键转绘-Qwen-Image-Edit图像编辑_2031200944762916865.json、图片生成/图生图/人物多角度一键生成《Next Scene》_1984265817120522242.json、图片生成/图生图/按尺寸扩图_2054365264153718786.json、图片生成/图生图/生图-动漫转真人-qwen-Edit-anything2real-2511-8步_2008107492974272513.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `Int` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `GetImageSizeAndCount` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/5 个有
- `easy promptLine` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `DifferentialDiffusion` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImagePadKJ` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
