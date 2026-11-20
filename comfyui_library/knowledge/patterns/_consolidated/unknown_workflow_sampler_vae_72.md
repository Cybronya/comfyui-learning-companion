---
name: unknown_workflow_sampler_vae_72
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5075
common_nodes: [Any Switch (rgthree), Bookmark (rgthree), CFGNorm, CLIPLoader, ConditioningZeroOut, DWPreprocessor, DepthAnythingV2Preprocessor, EmptySD3LatentImage, Fast Groups Muter (rgthree), GetNode, ImageScaleToTotalPixels, KSampler, Label (rgthree), LoadImage, ModelSamplingAuraFlow, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), NunchakuQwenImageDiTLoader, PrimitiveString, PrimitiveStringMultiline, RH_Translator, SaveImage, SetNode, StringConcatenate, TextEncodeQwenImageEditPlus_lrzjason, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/图片秒变手办-阿浩_2026842986700611585.json, 数字人/数字人/手办自由 Qwen新版 图片编辑V1 不偏移！_1972352052158459906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_72

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/图片秒变手办-阿浩_2026842986700611585.json、数字人/数字人/手办自由 Qwen新版 图片编辑V1 不偏移！_1972352052158459906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bookmark (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `EmptySD3LatentImage`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `NunchakuQwenImageDiTLoader`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RH_Translator`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAEDecode`
- `VAELoader`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
