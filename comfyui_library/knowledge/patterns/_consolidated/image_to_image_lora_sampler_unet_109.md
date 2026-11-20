---
name: image_to_image_lora_sampler_unet_109
type: Image To Image
frequency: 6
level: moderate
coverage: 0.834333
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_EditV1.0_2001542701378093057.json, 图片生成/图生图/Qwen_一键双人合影工作流_1994794472980537346.json, 图片生成/图生图/Qwen光线迁移_1998591999689261058.json, 图片生成/图生图/WH-AI-Studio换装Qwen版_2022569512205295617.json, 图片生成/图生图/WH-AI-Studio电商模特换姿势-动作迁移完美版（保持人物服装细节一致）_2022561416414240770.json, 图片生成/图生图/（网页）千问换姿势工作流_2037509543676088321.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_109

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen_EditV1.0_2001542701378093057.json、图片生成/图生图/Qwen_一键双人合影工作流_1994794472980537346.json、图片生成/图生图/Qwen光线迁移_1998591999689261058.json、图片生成/图生图/WH-AI-Studio换装Qwen版_2022569512205295617.json、图片生成/图生图/WH-AI-Studio电商模特换姿势-动作迁移完美版（保持人物服装细节一致）_2022561416414240770.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
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
- `Image Comparer (rgthree)` —— 4/6 个有
- `Anything Everywhere3` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `LatentUpscaleBy` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `easy imageConcat` —— 3/6 个有
- `DWPreprocessor` —— 2/6 个有
- `GetImageSize` —— 2/6 个有
- `TextEncodeQwenImageEdit` —— 2/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 3 - 8 | 6 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 0.5 - 1 | 6 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 3 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，6 个样本
- 高发问题（9/6 个样本）：Steps较低可能导致细节不足
