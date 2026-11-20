---
name: unknown_workflow_lora_sampler_clip_281
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9745
common_nodes: [BiRefNetRMBG, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, DetailerForEach, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, KSampler, LayerMask: PersonMaskUltra V2, LayerMask: SegformerB2ClothesUltra, LayerUtility: ExtendCanvas, LayerUtility: ImageScaleByAspectRatio, LoadImage, LoraLoaderModelOnly, MaskToSEGS, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, SaveImage, Seed (rgthree), SubtractMask, TextEncodeQwenImageEditPlusAdvance_lrzjason, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/换头换场景比例1_1_1981549238716907521.json, 图片生成/文生图/FLUX换脸+比例控制_1992126721765822465.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_281

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/换头换场景比例1_1_1981549238716907521.json、图片生成/文生图/FLUX换脸+比例控制_1992126721765822465.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `BiRefNetRMBG`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DetailerForEach`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToSEGS`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `SaveImage`
- `Seed (rgthree)`
- `SubtractMask`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageMaskScaleAs` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
