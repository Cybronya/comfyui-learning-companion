---
name: unknown_workflow_sampler_clip_unet_129
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9664
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux.2-Klein-文生图_2057389434856886274.json, 图片生成/文生图/Flux.2-Klein-文生图_2060250377894846466.json, 图片生成/文生图/Flux2 Klein 9B 文生图_2012015496945737730.json, 图片生成/文生图/Flux2 Klein 文生图_2020763009353785346.json, 图片生成/文生图/RH-PSAPI插件用-文生图_2068260936263233538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_129

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Flux.2-Klein-文生图_2057389434856886274.json、图片生成/文生图/Flux.2-Klein-文生图_2060250377894846466.json、图片生成/文生图/Flux2 Klein 9B 文生图_2012015496945737730.json、图片生成/文生图/Flux2 Klein 文生图_2020763009353785346.json、图片生成/文生图/RH-PSAPI插件用-文生图_2068260936263233538.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `JWInteger` —— 1/5 个有
- `MuyeSizeSelector` —— 1/5 个有
- `QwenImageLatentAspectRatio` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 5 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 0.4 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
