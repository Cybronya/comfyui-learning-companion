---
name: unknown_workflow_sampler_clip_unet_140
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.964
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen2512-qwen-水彩画-文生图工作流_2011342788499087361.json, 图片生成/文生图/qwen_image2512+lora8步_2009428030506143746.json, 图片生成/文生图/qwen_image文生图+lora8步_1955214645163278337.json, 图片生成/文生图/zimage-base文生图_2039943203540967425.json, 图片生成/文生图/zimage-turbo-文生图工作流-lora人像_2048255863974010881.json, 图片生成/文生图/亚秒级生成！Zimage超快图片生成器官方工作流_2035604076301393921.json, 图片生成/文生图/文生图-Qwen2512-6步-模板_2023584055270313986.json, 图片生成/文生图/自己用小i文生图：Qwen+Lora_2021825579867185154.json, 数字人/数字人/文生图-Qwen2512-6步-模板_2026856696487878658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_140

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/qwen2512-qwen-水彩画-文生图工作流_2011342788499087361.json、图片生成/文生图/qwen_image2512+lora8步_2009428030506143746.json、图片生成/文生图/qwen_image文生图+lora8步_1955214645163278337.json、图片生成/文生图/zimage-base文生图_2039943203540967425.json、图片生成/文生图/zimage-turbo-文生图工作流-lora人像_2048255863974010881.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 7/9 个有
- `ModelSamplingAuraFlow` —— 7/9 个有
- `ConditioningZeroOut` —— 3/9 个有
- `RH_LLMAPI_NODE` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `TextConcat` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 50 | 9 | 9% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 37% |
| 采样算法 | dpmpp_2m | - | 9 | 33% |
| 调度器 | simple | - | 9 | 44% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | 0.95 - 1 | 7 | 98% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 50，9 个样本，取值分散，一致性仅 9%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 dpmpp_2m，9 个样本，一致性 33%
- 调度器 最常用 simple，9 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.95 - 1，7 个样本，取值集中（一致性 98%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
