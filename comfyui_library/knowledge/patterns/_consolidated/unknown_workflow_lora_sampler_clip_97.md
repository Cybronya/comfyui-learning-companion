---
name: unknown_workflow_lora_sampler_clip_97
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.847
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [MathExpression|pysssss, CR Prompt Text]
members: [视频生成/文生视频/1972558589065949185.json, 视频生成/文生视频/1972639381158862850.json, 视频生成/文生视频/1974800997673512961.json, 视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_97

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1972558589065949185.json、视频生成/文生视频/1972639381158862850.json、视频生成/文生视频/1974800997673512961.json、视频生成/文生视频/UnifiedReward-Flex LoRA-Wan2.2-动作优化-文生视频_2031576870059249666.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CustomAddLabel` —— 1/4 个有
- `DF_Int_to_Float` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 4 | 81% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，4 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、CR Prompt Text
