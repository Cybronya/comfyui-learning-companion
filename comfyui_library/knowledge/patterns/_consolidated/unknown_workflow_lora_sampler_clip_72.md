---
name: unknown_workflow_lora_sampler_clip_72
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.868875
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-Pruning版本更低显存质量一致_1968866874069065729.json, 图片生成/文生图/QwenImage 4K高清大图DyPE直出_2000788947687141378.json, 图片生成/文生图/Z-Image-Turbo 4K高清大图DyPE直出_2000758971898134529.json, 图片生成/文生图/Z-image-base文生图8部加速版_2033075055076319234.json, 图片生成/文生图/zimage base 加速高质量lora最高20倍提速_2021771055412547585.json, 图片生成/文生图/小说推文古风小说推文抖音超火_1991148887255920641.json, 图片生成/文生图/沙雕动漫修仙玄幻人物三视图（加速版）_1988478076659130370.json, 图片生成/文生图/沙雕动漫怪兽神兽多视图三视图（加速版）_2002568995201007617.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-Pruning版本更低显存质量一致_1968866874069065729.json、图片生成/文生图/QwenImage 4K高清大图DyPE直出_2000788947687141378.json、图片生成/文生图/Z-Image-Turbo 4K高清大图DyPE直出_2000758971898134529.json、图片生成/文生图/Z-image-base文生图8部加速版_2033075055076319234.json、图片生成/文生图/zimage base 加速高质量lora最高20倍提速_2021771055412547585.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 6/8 个有
- `SDXLEmptyLatentSizePicker+` —— 5/8 个有
- `RMBG` —— 4/8 个有
- `EmptySD3LatentImage` —— 3/8 个有
- `CR Text Concatenate` —— 2/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `DyPE_FLUX` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `easy promptConcat` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832x1152 (0.72) | - | 5 | 40% |
| 高度 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 6 | 4 - 20 | 8 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 58% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 最常用 832x1152 (0.72)，5 个样本，一致性 40%
- 高度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，观测区间 4 - 20，8 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
