---
name: image_to_image_lora_sampler_unet_153
type: Image To Image
frequency: 4
level: moderate
coverage: 0.8925
common_nodes: [CLIPLoader, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit模型，手办风格-4K直出_1961646663603568641.json, 图片生成/图生图/Qwen-Image-Edit模型，精准编辑图片文字_1957821483923992578.json, 图片生成/图生图/QwenEdit官方流改优图片编辑4步加速Lora 6步出图效果更佳_1958102515072061442.json, 图片生成/图生图/qwen编辑 人物转手办_1959056979866103809.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit模型，手办风格-4K直出_1961646663603568641.json、图片生成/图生图/Qwen-Image-Edit模型，精准编辑图片文字_1957821483923992578.json、图片生成/图生图/QwenEdit官方流改优图片编辑4步加速Lora 6步出图效果更佳_1958102515072061442.json、图片生成/图生图/qwen编辑 人物转手办_1959056979866103809.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `PreviewImage` —— 3/4 个有
- `easy imageConcat` —— 3/4 个有
- `CFGNorm` —— 2/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `Int` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `ColorMatch` —— 1/4 个有
- `Image Remove Background Rembg (mtb)` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 6 - 20 | 4 | 52% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 4 | 57% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 6 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
