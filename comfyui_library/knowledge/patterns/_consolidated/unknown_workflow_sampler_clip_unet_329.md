---
name: unknown_workflow_sampler_clip_unet_329
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/flux.2-klein文生图_2077238073297031169.json, 图片生成/文生图/flux2-Klein-自动文生图（4B）_2012021202050617346.json, 图片生成/文生图/flux2.0_1995304483615858689.json, 图片生成/文生图/【文生图】Flux.2.0_Klein9B_2030309405933182978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_329

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/flux.2-klein文生图_2077238073297031169.json、图片生成/文生图/flux2-Klein-自动文生图（4B）_2012021202050617346.json、图片生成/文生图/flux2.0_1995304483615858689.json、图片生成/文生图/【文生图】Flux.2.0_Klein9B_2030309405933182978.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `JDCN_StringToList` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 6 - 22 | 4 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 6 - 22，4 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
