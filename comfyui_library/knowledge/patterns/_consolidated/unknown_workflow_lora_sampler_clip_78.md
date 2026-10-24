---
name: unknown_workflow_lora_sampler_clip_78
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.856833
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Rebalance写实洗图工作流_1990797714432667650.json, 图片生成/图生图/Qwen写实洗图工作流单张（防侵权）_1991315465637310465.json, 图片生成/图生图/Qwen洗图工作流单张（防侵权）_1995445153374593026.json, 图片生成/图生图/高级感服装模特展示图+全节点注释_2039663460946022401.json, 图片生成/文生图/Qwen Rebalance 写实洗图工作流_1991492700780371970.json, 图片生成/文生图/Qwen Rebalance超强写实质感出图_1990940694510514177.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_78

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Rebalance写实洗图工作流_1990797714432667650.json、图片生成/图生图/Qwen写实洗图工作流单张（防侵权）_1991315465637310465.json、图片生成/图生图/Qwen洗图工作流单张（防侵权）_1995445153374593026.json、图片生成/图生图/高级感服装模特展示图+全节点注释_2039663460946022401.json、图片生成/文生图/Qwen Rebalance 写实洗图工作流_1991492700780371970.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 5/6 个有
- `CheckpointLoaderSimple` —— 5/6 个有
- `ConditioningZeroOut` —— 5/6 个有
- `EmptySD3LatentImage` —— 5/6 个有
- `LayerUtility: ImageReel` —— 5/6 个有
- `LayerUtility: ImageReelComposit` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `LayerUtility: PurgeVRAM V2` —— 4/6 个有
- `PreviewImage` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 26 | 6 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 44% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 26，6 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（10/6 个样本）：Steps较低可能导致细节不足
