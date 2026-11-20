---
name: unknown_workflow_lora_sampler_unet_398
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.717
common_nodes: [ACE_TextGoogleTranslate, BlockifyMask, CFGNorm, CLIPLoader, ConditioningZeroOut, DrawMaskOnImage, Florence2ModelLoader, Florence2Run, Image Comparer (rgthree), KSampler, LayerUtility: ImageBlend, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingAuraFlow, PointsEditor, PreviewImage, RMBG, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, SeCModelLoader, SeCVideoSegmentation, Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, UnetLoaderGGUF, VAEDecode, VAELoader, YOLOModelLoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/多角色换人遮罩_2007655913640955905.json, 数字人/数字人/小白换人遮罩_2003396750369038337.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_398

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/多角色换人遮罩_2007655913640955905.json、数字人/数字人/小白换人遮罩_2003396750369038337.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `ACE_TextGoogleTranslate`
- `BlockifyMask`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `PointsEditor`
- `PreviewImage`
- `RMBG`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `YOLOModelLoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
