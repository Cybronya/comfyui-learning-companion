---
name: unknown_workflow_lora_sampler_checkpoint_3
type: Unknown Workflow
frequency: 8
level: strong
coverage: 1
common_nodes: [CR Text, CheckpointLoaderSimple, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Rapid-AIO_2047923784266555393.json, 图片生成/图生图/图生图一键工作_2001323637812625410.json, 图片生成/图生图/图生图一键工作_2045091323006427138.json, 图片生成/图生图/图生图工作流_2037530314460893185.json, 图片生成/文生图/Qwen-Rapid-AIO_2054565798374584322.json, 图片生成/文生图/YYEMOJI 图生图一键工作_2056537190146076674.json, 图片生成/文生图/图生图一键工作_2049476537925242881.json, 图片生成/文生图/通义千问文生图_2064587610374361089.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen-Rapid-AIO_2047923784266555393.json、图片生成/图生图/图生图一键工作_2001323637812625410.json、图片生成/图生图/图生图一键工作_2045091323006427138.json、图片生成/图生图/图生图工作流_2037530314460893185.json、图片生成/文生图/Qwen-Rapid-AIO_2054565798374584322.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 6/8 个有
- `SaveLatent` —— 5/8 个有
- `SaveImage` —— 4/8 个有
- `TT_img_enc` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 8 | 71% |
| 采样算法 | euler_ancestral | - | 8 | 50% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，8 个样本
- 采样算法 最常用 euler_ancestral，8 个样本，一致性 50%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
