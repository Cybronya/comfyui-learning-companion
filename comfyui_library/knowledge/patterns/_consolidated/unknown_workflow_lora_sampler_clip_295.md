---
name: unknown_workflow_lora_sampler_clip_295
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8575
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DeepTranslatorTextNode, DualCLIPLoader, FluxGuidance, JJC_JoyCaption, KSampler (Efficient), LayerFilter: HDREffects, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewImage, ReduxAdvanced, SaveImage, ShowText|pysssss, StringFunction|pysssss, StyleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/一键运行：Nunchaku 一键换背景、刷图、洗图_1937035535103741953.json, 图片生成/文生图/一键运行：Nunchaku 视觉参考 极速洗图出图_1936968718520061954.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_295

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/一键运行：Nunchaku 一键换背景、刷图、洗图_1937035535103741953.json、图片生成/文生图/一键运行：Nunchaku 视觉参考 极速洗图出图_1936968718520061954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `FluxGuidance`
- `JJC_JoyCaption`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `StyleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `BRIA_RMBG_ModelLoader_Zho` —— 1/2 个有
- `BRIA_RMBG_Zho` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
