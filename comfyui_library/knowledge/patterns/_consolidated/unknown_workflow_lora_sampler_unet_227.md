---
name: unknown_workflow_lora_sampler_unet_227
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.919
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageConcatMulti, ImageFromBatch, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MmuuaiGroupBypass, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人物资产-4视图_2095374881834758145.json, 图片生成/图生图/人物资产4视图_2092428551445368834.json, 数字人/数字人/10Eros-miniMax 8步极速生成人物资产四视图v2.0_2087065573468495873.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_227

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人物资产-4视图_2095374881834758145.json、图片生成/图生图/人物资产4视图_2092428551445368834.json、数字人/数字人/10Eros-miniMax 8步极速生成人物资产四视图v2.0_2087065573468495873.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageConcatMulti`
- `ImageFromBatch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MmuuaiGroupBypass`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
