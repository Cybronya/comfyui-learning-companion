---
name: image_to_image_upscale_sampler_unet_3
type: Image To Image
frequency: 4
level: strong
coverage: 0.85475
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/场景多角度_1991721072194318337.json, 图片生成/图生图/多角度一致性Qwen-Edit-Angles【高清】_1986611456689008642.json, 图片生成/图生图/胸部增强模型-丰胸自动流程-qwen2511新模型_2014336544496164865.json, 图片生成/图生图/（电商流）最强服装平铺加速放大ultra版-qwenedit2509_1990668776490360834.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_unet_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/场景多角度_1991721072194318337.json、图片生成/图生图/多角度一致性Qwen-Edit-Angles【高清】_1986611456689008642.json、图片生成/图生图/胸部增强模型-丰胸自动流程-qwen2511新模型_2014336544496164865.json、图片生成/图生图/（电商流）最强服装平铺加速放大ultra版-qwenedit2509_1990668776490360834.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `Anything Everywhere3` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `VAEEncodeTiled` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `Upscale Model Loader` —— 1/4 个有
- `easy ifElse` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
