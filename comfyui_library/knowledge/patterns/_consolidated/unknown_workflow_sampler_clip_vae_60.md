---
name: unknown_workflow_sampler_clip_vae_60
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/双节棍加速千问 image工作流_1965043199712612353.json, 图片生成/文生图/在线-Z-T2I-1128_1994378488129986561.json, 图片生成/文生图/基础文生图 Z-Image-Turbo（带LoRA加载节点）_2007330137645260802.json, 图片生成/文生图/基础案例basic_switch_node+全节点注释_2055478851081383937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/双节棍加速千问 image工作流_1965043199712612353.json、图片生成/文生图/在线-Z-T2I-1128_1994378488129986561.json、图片生成/文生图/基础文生图 Z-Image-Turbo（带LoRA加载节点）_2007330137645260802.json、图片生成/文生图/基础案例basic_switch_node+全节点注释_2055478851081383937.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `NunchakuQwenImageDiTLoader` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 10 | 4 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | res_multistep | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 res_multistep，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
