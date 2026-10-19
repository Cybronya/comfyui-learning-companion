---
name: unknown_workflow_inpaint_sampler_clip_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.735667
common_nodes: [CLIPTextEncode, ColorCorrect, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, ImpactInt, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, Mask Fill Holes, SaveImage, ToBinaryMask, UNETLoader, VAEDecode, VAELoader, easy ifElse]
problems: []
missing: [CR Text, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, Mask Fill Holes, easy boolean]
members: [图片生成/文生图/1985864428728066050.json, 图片生成/文生图/1989239057773367297.json, 视频生成/图生视频/1981616130160762881.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1985864428728066050.json、图片生成/文生图/1989239057773367297.json、视频生成/图生视频/1981616130160762881.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ColorCorrect`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImpactInt`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `Mask Fill Holes`
- `SaveImage`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `easy boolean` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerMask: MaskGrow、LayerUtility: CropByMask V2、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: RestoreCropBox
