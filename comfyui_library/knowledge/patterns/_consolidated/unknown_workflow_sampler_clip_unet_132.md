---
name: unknown_workflow_sampler_clip_unet_132
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8656
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/WH-AI-Studio（Flux2-Klein完美文生图）_2026681586271391745.json, 图片生成/文生图/flux-2-klein-9b（文生图）_2012052794068443137.json, 图片生成/文生图/【阡陌】FLUX-2-Klein 9B base版文生图工作流_2016491648590553089.json, 图片生成/文生图/【阡陌】FLUX-2-Klein 9B 蒸馏版4步极速文生图工作流_2016500518138421250.json, 图片生成/文生图/工作流系列00-klein的文生图工作流-基础向讲解此工作流_2012049130310340610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_132

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/WH-AI-Studio（Flux2-Klein完美文生图）_2026681586271391745.json、图片生成/文生图/flux-2-klein-9b（文生图）_2012052794068443137.json、图片生成/文生图/【阡陌】FLUX-2-Klein 9B base版文生图工作流_2016491648590553089.json、图片生成/文生图/【阡陌】FLUX-2-Klein 9B 蒸馏版4步极速文生图工作流_2016500518138421250.json、图片生成/文生图/工作流系列00-klein的文生图工作流-基础向讲解此工作流_2012049130310340610.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `Int` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `KSampler` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
