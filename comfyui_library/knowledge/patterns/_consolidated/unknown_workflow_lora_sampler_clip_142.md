---
name: unknown_workflow_lora_sampler_clip_142
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6015
common_nodes: [AddLabel, CR Image Grid Panel, CR Math Operation, ConditioningZeroOut, EmptyLatentImage, Float, GoogleTranslateCLIPTextEncodeNode, JoinStringMulti, KSampler, LoraLoaderModelOnly, MuyeTextEditOutput, PreviewImage, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAELoader, easy batchAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart]
problems: []
missing: [CR Image Grid Panel, CR Math Operation, SimpleMath+, easy batchAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy promptLine]
members: [图片生成/文生图/(Qc_Lora)Z-ImageLora_text_1996391726472380417.json, 图片生成/文生图/1987396378466955266.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_142

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/(Qc_Lora)Z-ImageLora_text_1996391726472380417.json、图片生成/文生图/1987396378466955266.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Image Grid Panel、CR Math Operation、SimpleMath+、easy batchAnything、easy convertAnything
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
