---
name: unknown_workflow_sampler_clip_vae_35
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.897429
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/hunyuan-image gguf 8步加速版_1966037699108966402.json, 图片生成/文生图/写实加强版Wan2.2文生图工作流_1956995525369323522.json, 图片生成/文生图/千问-qwen2512-image-文生图工作流_2008014250991685634.json, 图片生成/文生图/千问工作流_2083184424287563777.json, 图片生成/文生图/千问文生图_1985931273690591234.json, 图片生成/文生图/千问文生图_1985959773130633217.json, 图片生成/文生图/千问文生图_1987591657719836673.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_35

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/hunyuan-image gguf 8步加速版_1966037699108966402.json、图片生成/文生图/写实加强版Wan2.2文生图工作流_1956995525369323522.json、图片生成/文生图/千问-qwen2512-image-文生图工作流_2008014250991685634.json、图片生成/文生图/千问工作流_2083184424287563777.json、图片生成/文生图/千问文生图_1985931273690591234.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 4/7 个有
- `ModelSamplingSD3` —— 2/7 个有
- `TextInput_` —— 2/7 个有
- `CR Simple Prompt List` —— 1/7 个有
- `EmptyHunyuanImageLatent` —— 1/7 个有
- `GlobalSeed //Inspire` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 20 | 7 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 7 | 42% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
