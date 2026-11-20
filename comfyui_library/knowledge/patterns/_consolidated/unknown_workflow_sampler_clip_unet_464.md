---
name: unknown_workflow_sampler_clip_unet_464
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.804
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, ImageResizeKJv2, KSampler, LucyConditionConcatNode, ModelSamplingSD3, PrimitiveFloat, PrimitiveInt, SaveVideo, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideoFFmpeg]
problems: []
missing: []
members: [平台全量/lucy-edit-视频换装_1970482333650460674.json, 平台全量/lucy-edit视频编辑官方工作流_1970108321355210754.json, 平台全量/【老金驿站】LucyEdit纳米香蕉式极速魔改视频工作流_1970023643017322498.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_464

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/lucy-edit-视频换装_1970482333650460674.json、平台全量/lucy-edit视频编辑官方工作流_1970108321355210754.json、平台全量/【老金驿站】LucyEdit纳米香蕉式极速魔改视频工作流_1970023643017322498.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `ImageResizeKJv2`
- `KSampler`
- `LucyConditionConcatNode`
- `ModelSamplingSD3`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideoFFmpeg`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 40 - 50 | 3 | 90% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 40 - 50，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
