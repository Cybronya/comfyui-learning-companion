---
name: unknown_workflow_lora_sampler_unet_92
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.926714
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511 3图编辑_2004437958134562817.json, 图片生成/图生图/Qwen edit 千问编辑_1958364031461572610.json, 图片生成/图生图/Qwen 编辑 生成 三视图_1962408297523449858.json, 图片生成/图生图/Qwen+编辑+表情包_1964221766015045634.json, 图片生成/图生图/QwenImageEdit-8Steps_1958006497307504641.json, 图片生成/图生图/b-光影溶图融图qwen edit 2509_2005252378804842497.json, 图片生成/文生图/QwenImageEdit-8step基础版_1960161305468547074.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_92

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511 3图编辑_2004437958134562817.json、图片生成/图生图/Qwen edit 千问编辑_1958364031461572610.json、图片生成/图生图/Qwen 编辑 生成 三视图_1962408297523449858.json、图片生成/图生图/Qwen+编辑+表情包_1964221766015045634.json、图片生成/图生图/QwenImageEdit-8Steps_1958006497307504641.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/7 个有
- `TextEncodeQwenImageEdit` —— 5/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `GetImageSize` —— 4/7 个有
- `TextEncodeQwenImageEditPlus` —— 4/7 个有
- `CFGNorm` —— 3/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 2/7 个有
- `PrimitiveString` —— 2/7 个有
- `CR Simple Image Compare` —— 1/7 个有
- `ImageTile+` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1536 | 7 | 55% |
| 高度 | 1024 | 512 - 2064 | 7 | 47% |
| 采样步数 | 8 | 8 - 20 | 7 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 7 | 84% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1536，7 个样本
- 高度 中位数 1024，观测区间 512 - 2064，7 个样本，取值分散，一致性仅 47%
- 采样步数 中位数 8，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，7 个样本，取值集中（一致性 84%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
