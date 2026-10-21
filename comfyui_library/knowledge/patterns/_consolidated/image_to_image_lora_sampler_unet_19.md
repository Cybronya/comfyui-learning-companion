---
name: image_to_image_lora_sampler_unet_19
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8156
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline]
members: [图片生成/文生图/1986720327151595522.json, 图片生成/文生图/1986721390671949825.json, 图片生成/文生图/Gemini3.5 笔记本手账生成+全节点注释_2058861210543673345.json, 图片生成/文生图/Qwen-Edit-2509-多角度切换_1991129925849579521.json, 视频生成/图生视频/1987730871912435714.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_19

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1986720327151595522.json、图片生成/文生图/1986721390671949825.json、图片生成/文生图/Gemini3.5 笔记本手账生成+全节点注释_2058861210543673345.json、图片生成/文生图/Qwen-Edit-2509-多角度切换_1991129925849579521.json、视频生成/图生视频/1987730871912435714.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 4/5 个有
- `ConditioningZeroOut` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `ImageStitch` —— 2/5 个有
- `Text` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `easy imageSize` —— 2/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `TT_img_enc` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 20 | 5 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 20，5 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline
