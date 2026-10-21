---
name: unknown_workflow_lora_sampler_clip_57
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.753
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, QwenImageLatentAspectRatio, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2017779060331515905.json, 图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084812529720713218.json, 图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084815948225273857.json, 图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084827676447170561.json, 图片生成/文生图/【KKAI】开班课生图工作流_2037521440781639682.json, 图片生成/文生图/文生图 ZImage（Base Vs Turbo Vs Art）_2017768633228857346.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2017779060331515905.json、图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084812529720713218.json、图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084815948225273857.json、图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084827676447170561.json、图片生成/文生图/【KKAI】开班课生图工作流_2037521440781639682.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageLatentAspectRatio`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 5/6 个有
- `CR Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 12 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_multistep | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 12，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（10/6 个样本）：Steps较低可能导致细节不足
