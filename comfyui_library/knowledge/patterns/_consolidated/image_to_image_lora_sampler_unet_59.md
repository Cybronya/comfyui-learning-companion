---
name: image_to_image_lora_sampler_unet_59
type: Image To Image
frequency: 10
level: moderate
coverage: 0.788
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA单个镜头_2009066368041226242.json, "图片生成/图生图/Qwen-Image-Edit图像编辑,超强精准控制_1958442372495523841.json", 图片生成/图生图/Qwen-Image-Edit工作流_1953817263986147329.json, 图片生成/图生图/Qwen-Image海报生成工作流_1982450271907389441.json, 图片生成/图生图/Qwen-edit 超自然重打光_2054846333298724865.json, 图片生成/图生图/Qwen-edit_万物重打光_2099321308822724609.json, 图片生成/图生图/Qwen-edit_万物重打光_2099665295848861698.json, 图片生成/图生图/人像写真重打光_2076370520215474177.json, 图片生成/图生图/人像写真重打光_2077926058837504001.json, 图片生成/图生图/人像写真重打光_2077938985393020930.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_59

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA单个镜头_2009066368041226242.json、图片生成/图生图/Qwen-Image-Edit图像编辑,超强精准控制_1958442372495523841.json、图片生成/图生图/Qwen-Image-Edit工作流_1953817263986147329.json、图片生成/图生图/Qwen-Image海报生成工作流_1982450271907389441.json、图片生成/图生图/Qwen-edit 超自然重打光_2054846333298724865.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 9/10 个有
- `ConditioningZeroOut` —— 8/10 个有
- `PreviewImage` —— 7/10 个有
- `ColorMatch` —— 6/10 个有
- `JjkText` —— 6/10 个有
- `LayerUtility: PurgeVRAM V2` —— 6/10 个有
- `Canny` —— 3/10 个有
- `ModelPatchLoader` —— 3/10 个有
- `QwenImageDiffsynthControlnet` —— 3/10 个有
- `Anything Everywhere3` —— 1/10 个有
- `CLIPTextEncode` —— 1/10 个有
- `EmptySD3LatentImage` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 10 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 10 | 61% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，10 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（6/10 个样本）：Steps较低可能导致细节不足
