---
name: unknown_workflow_lora_sampler_clip_302
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9115
common_nodes: [CLIPLoaderGGUF, CLIPTextEncode, CR Text, ConditioningZeroOut, DapaoImageRatioLimitNode, Dapao_LlamaChat, EmptyLatentImage, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Seed (rgthree), StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader, easy int, easy showAnything, 孤海注释]
problems: []
missing: []
members: [图片生成/文生图/绝望少妇 POV第一视角 网红图 专属lora_2060626394132082690.json, 图片生成/文生图/绝望少妇 POV第一视角 网红图 专属lora_2061363103056621569.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_302

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/绝望少妇 POV第一视角 网红图 专属lora_2060626394132082690.json、图片生成/文生图/绝望少妇 POV第一视角 网红图 专属lora_2061363103056621569.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DapaoImageRatioLimitNode`
- `Dapao_LlamaChat`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Seed (rgthree)`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`
- `easy showAnything`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 864 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 864，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
