---
name: unknown_workflow_sampler_vae_60
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.562
common_nodes: [Any Switch (rgthree), Bookmark (rgthree), CFGNorm, CLIPLoader, ConditioningZeroOut, DWPreprocessor, DrawMaskOnImage, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageResizeKJv2, KSampler, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, Mask Fill Holes, ModelSamplingAuraFlow, PreviewImage, PrimitiveString, PrimitiveStringMultiline, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, RHHiddenNodes, RMBG, SaveImage, SetNode, StringConcatenate, Switch any [Crystools], TextEncodeQwenImageEditPlusCustom_lrzjason, ToBinaryMask, VAEDecode, VAELoader, easy imagePixelPerfect, easy int, easy isMaskEmpty, easy promptReplace]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物替换 图片编辑 简单上手 效果炸裂_2028472465067872257.json, 图片生成/图生图/角色替换_图片编辑V3 (影视恶搞必备）_2026919896113745922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_60

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人物替换 图片编辑 简单上手 效果炸裂_2028472465067872257.json、图片生成/图生图/角色替换_图片编辑V3 (影视恶搞必备）_2026919896113745922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bookmark (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `Mask Fill Holes`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `RHHiddenNodes`
- `RMBG`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `Switch any [Crystools]`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ToBinaryMask`
- `VAEDecode`
- `VAELoader`
- `easy imagePixelPerfect`
- `easy int`
- `easy isMaskEmpty`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
