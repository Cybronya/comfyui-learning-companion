---
name: unknown_workflow_lora_sampler_unet_92
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9285
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511 3图编辑_2004437958134562817.json, 图片生成/图生图/Qwen edit 千问编辑_1958364031461572610.json, 图片生成/图生图/Qwen 编辑 生成 三视图_1962408297523449858.json, 图片生成/图生图/Qwen+编辑+表情包_1964221766015045634.json, 图片生成/图生图/QwenImageEdit-8Steps_1958006497307504641.json, 图片生成/图生图/b-光影溶图融图qwen edit 2509_2005252378804842497.json, 图片生成/图生图/ktv公主_1991635135160336386.json, 图片生成/文生图/QwenImageEdit-8step基础版_1960161305468547074.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_92

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511 3图编辑_2004437958134562817.json、图片生成/图生图/Qwen edit 千问编辑_1958364031461572610.json、图片生成/图生图/Qwen 编辑 生成 三视图_1962408297523449858.json、图片生成/图生图/Qwen+编辑+表情包_1964221766015045634.json、图片生成/图生图/QwenImageEdit-8Steps_1958006497307504641.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
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
- `ModelSamplingAuraFlow` —— 6/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `TextEncodeQwenImageEdit` —— 5/8 个有
- `TextEncodeQwenImageEditPlus` —— 5/8 个有
- `CFGNorm` —— 4/8 个有
- `GetImageSize` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 3/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `JjkText` —— 2/8 个有
- `PrimitiveString` —— 2/8 个有
- `CR Simple Image Compare` —— 1/8 个有
- `ImageTile+` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 976 | 512 - 1536 | 8 | 57% |
| 高度 | 1084 | 512 - 2064 | 8 | 50% |
| 采样步数 | 8 | 8 - 20 | 8 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 8 | 84% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 976，观测区间 512 - 1536，8 个样本
- 高度 中位数 1084，观测区间 512 - 2064，8 个样本
- 采样步数 中位数 8，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，8 个样本，取值集中（一致性 84%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
