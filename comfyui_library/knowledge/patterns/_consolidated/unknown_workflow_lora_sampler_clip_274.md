---
name: unknown_workflow_lora_sampler_clip_274
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [AdvancedLyingSigmaSampler, ApplyTeaCachePatch, BasicScheduler, CLIPTextEncode, DeepTranslatorTextNode, DualCLIPLoader, FluxForwardOverrider, KSamplerSelect, LoadImage, LoraLoader, SamplerCustom, SaveImage, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, workflow>1]
problems: []
missing: []
members: [图片生成/图生图/merge二合_1943609839673372673.json, 数字人/数字人/merge新_1939529700354007042.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_274

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/merge二合_1943609839673372673.json、数字人/数字人/merge新_1939529700354007042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `AdvancedLyingSigmaSampler`
- `ApplyTeaCachePatch`
- `BasicScheduler`
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `FluxForwardOverrider`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `SamplerCustom`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `workflow>1`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.315 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.315，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
