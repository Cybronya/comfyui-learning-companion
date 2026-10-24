---
name: unknown_workflow_lora_sampler_clip_63
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.769429
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2017779060331515905.json, 图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084812529720713218.json, 图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084815948225273857.json, 图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084827676447170561.json, 图片生成/文生图/▶WAN2.2高低噪文生图流（另一种）_1956245195178344449.json, 图片生成/文生图/万相2.2 高质量文生图工作流_1960368358069776385.json, 图片生成/文生图/文生图 ZImage（Base Vs Turbo Vs Art）_2017768633228857346.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2017779060331515905.json、图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084812529720713218.json、图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084815948225273857.json、图片生成/文生图/ZImage 文生图 多种模式（Base+Turbo+Art）_2084827676447170561.json、图片生成/文生图/▶WAN2.2高低噪文生图流（另一种）_1956245195178344449.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `LayerUtility: PurgeVRAM` —— 6/7 个有
- `CR Prompt Text` —— 5/7 个有
- `ModelSamplingAuraFlow` —— 5/7 个有
- `QwenImageLatentAspectRatio` —— 5/7 个有
- `EmptyHunyuanLatentVideo` —— 2/7 个有
- `ModelSamplingSD3` —— 2/7 个有
- `CR Image Size` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | res_multistep | - | 7 | 71% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 0.3 - 1 | 7 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，7 个样本
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足
