---
name: unknown_workflow_lora_sampler_clip_203
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.753
common_nodes: [AddLabel, CR Image Grid Panel, CR Math Operation, ConditioningZeroOut, EmptyLatentImage, Float, GoogleTranslateCLIPTextEncodeNode, JoinStringMulti, KSampler, LoraLoaderModelOnly, MuyeTextEditOutput, PreviewImage, SaveImage, SimpleMath+, VAEDecode, VAELoader, easy batchAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/(Qc_Lora)Z-ImageLora_text_1996391726472380417.json, 图片生成/文生图/2029887943283843073.json, 图片生成/文生图/lora测试xy图表工作流_1987396378466955266.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_203

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/(Qc_Lora)Z-ImageLora_text_1996391726472380417.json、图片生成/文生图/2029887943283843073.json、图片生成/文生图/lora测试xy图表工作流_1987396378466955266.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CR Image Grid Panel`
- `CR Math Operation`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Float`
- `GoogleTranslateCLIPTextEncodeNode`
- `JoinStringMulti`
- `KSampler`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `PreviewImage`
- `SaveImage`
- `SimpleMath+`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `EnhancedLoadDiffusionModel` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 3 | 87% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 20 | 9 - 20 | 3 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 3 | 33% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 9 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，3 个样本，一致性 33%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
