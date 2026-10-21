---
name: unknown_workflow_inpaint_sampler_clip
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.76775
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, ImpactInt, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, Mask Fill Holes, easy boolean]
members: [图片生成/文生图/1985864428728066050.json, 图片生成/文生图/1989239057773367297.json, 图片生成/文生图/OneReward-Fill最强扩图【无损原图效果炸裂】_1990118350430851073.json, 视频生成/图生视频/1981616130160762881.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1985864428728066050.json、图片生成/文生图/1989239057773367297.json、图片生成/文生图/OneReward-Fill最强扩图【无损原图效果炸裂】_1990118350430851073.json、视频生成/图生视频/1981616130160762881.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImpactInt`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorCorrect` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LayerUtility: CropByMask V2` —— 3/4 个有
- `LayerUtility: RestoreCropBox` —— 3/4 个有
- `Mask Fill Holes` —— 3/4 个有
- `ToBinaryMask` —— 3/4 个有
- `easy ifElse` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `easy boolean` —— 2/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `ImageComposite+` —— 1/4 个有
- `ImagePadForOutpaintMasked` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `RH_Translator` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerMask: MaskGrow、LayerUtility: CropByMask V2、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: RestoreCropBox
