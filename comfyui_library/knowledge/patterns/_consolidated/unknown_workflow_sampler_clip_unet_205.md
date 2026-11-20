---
name: unknown_workflow_sampler_clip_unet_205
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.977875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen2512-qwen-水彩画-文生图工作流_2011342788499087361.json, 图片生成/文生图/qwen_image2512+lora8步_2009428030506143746.json, 图片生成/文生图/qwen_image文生图+lora8步_1955214645163278337.json, 图片生成/文生图/zimage-base文生图_2039943203540967425.json, 图片生成/文生图/zimage-turbo-文生图工作流-lora人像_2048255863974010881.json, 图片生成/文生图/小红书风格加黑丝_2003393169008041986.json, 图片生成/文生图/自己用小i文生图：Qwen+Lora_2021825579867185154.json, 视频生成/图生视频/自己用：Qwen-Image +Lora_1955581722751483906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_205

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/qwen2512-qwen-水彩画-文生图工作流_2011342788499087361.json、图片生成/文生图/qwen_image2512+lora8步_2009428030506143746.json、图片生成/文生图/qwen_image文生图+lora8步_1955214645163278337.json、图片生成/文生图/zimage-base文生图_2039943203540967425.json、图片生成/文生图/zimage-turbo-文生图工作流-lora人像_2048255863974010881.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 6/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `RH_LLMAPI_NODE` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `FluxResolutionNode` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `TextConcat` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14.5 | 8 - 50 | 8 | 28% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 4 | 8 | 42% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 1 | 0.95 - 1 | 7 | 98% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14.5，观测区间 8 - 50，8 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 4，8 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.95 - 1，7 个样本，取值集中（一致性 98%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
