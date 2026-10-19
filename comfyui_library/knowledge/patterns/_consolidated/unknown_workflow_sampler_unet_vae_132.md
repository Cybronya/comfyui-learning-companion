---
name: unknown_workflow_sampler_unet_vae_132
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9834
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1942182398836764674.json, 图片生成/文生图/1942817552894464001.json, 图片生成/文生图/1943252121083146241.json, 图片生成/文生图/1944714736133132290.json, 图片生成/文生图/1952603918469672962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_132

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1942182398836764674.json、图片生成/文生图/1942817552894464001.json、图片生成/文生图/1943252121083146241.json、图片生成/文生图/1944714736133132290.json、图片生成/文生图/1952603918469672962.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateCLIPTextEncodeNode` —— 2/5 个有
- `CLIPTextEncodeFlux` —— 2/5 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `TeaCache` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1200 | 5 | 83% |
| 高度 | 1024 | 768 - 1600 | 5 | 75% |
| 采样步数 | 20 | 4 - 38 | 5 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 0.35 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1200，5 个样本，取值集中（一致性 83%）
- 高度 中位数 1024，观测区间 768 - 1600，5 个样本
- 采样步数 中位数 20，观测区间 4 - 38，5 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
