---
name: unknown_workflow_lora_sampler_unet_273
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.931
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, ImpactSwitch, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text, TextCombinerTwo, TextEncodeQwenImageEditPlus, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/专属个性签名 - 支持各种笔锋_2038454093030629378.json, 图片生成/文生图/qwen_image_2512三步打造专属签名：商务稳重、艺术个性、草书飘逸_2011277108491849729.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_273

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/专属个性签名 - 支持各种笔锋_2038454093030629378.json、图片生成/文生图/qwen_image_2512三步打造专属签名：商务稳重、艺术个性、草书飘逸_2011277108491849729.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactSwitch`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text`
- `TextCombinerTwo`
- `TextEncodeQwenImageEditPlus`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 1352 | - | 2 | 86% |
| 高度 | 1296 | - | 2 | 79% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 1352，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1296，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
