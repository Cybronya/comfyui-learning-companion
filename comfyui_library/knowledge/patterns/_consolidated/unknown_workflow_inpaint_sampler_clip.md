---
name: unknown_workflow_inpaint_sampler_clip
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.882056
common_nodes: [CLIPTextEncode, ColorCorrect, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), ImpactInt, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, Mask Fill Holes, SaveImage, ToBinaryMask, UNETLoader, VAEDecode, VAELoader, easy ifElse]
problems: []
missing: []
members: [图片生成/图生图/Fill -OneReward 万物重绘增强版_1980477800337616897.json, 图片生成/图生图/Flux手动去水印_2006193627856379905.json, 图片生成/图生图/OneReward-Fill 最强局部重绘 - 框选模式 （直出4K大图）_1982037924495663105.json, 图片生成/图生图/OneReward-Fill 最强局部重绘 - 涂抹模式 （直出4K大图）_1980525783024357377.json, 图片生成/图生图/OneReward-Fill-最强局部重绘-框选遮罩_1981340609220870145.json, 图片生成/图生图/OneReward-Fill-最强局部重绘-遮罩涂抹模式_1981313979459035137.json, 图片生成/图生图/OneReward-Fill最强擦除【支持超大面积擦除】_1996020269028458497.json, 图片生成/图生图/OneReward-Fill最强重绘【4K直出不挑图】_1978644930367262722.json, 图片生成/图生图/OneReward-Fill最强重绘【4K直出不挑图】_1980971341039984641.json, 图片生成/图生图/OneReward-Fill最强重绘【4K直出不挑图】许老师版_1978949823430823937.json, 图片生成/图生图/OneReward-Fill重绘_1991413143960309762.json, 图片生成/图生图/局部重绘Flux-Fill最强局部重绘-OneReward-Fill1.0_1985568936228016129.json, 图片生成/图生图/局部重绘Flux-OneReward-Fill_2061649505245818881.json, 图片生成/图生图/局部重绘Flux-OneReward-Fill自用_1997666079226966018.json, 图片生成/图生图/局部重绘丨Flux-Fill最新最强局部重绘-OneReward-Fill最强重绘【高清直出】_1979068377333403649.json, 图片生成/图生图/手部修复-OneReward-Fill重绘修手_1981942247061110786.json, 图片生成/图生图/最强重绘4K直出不挑图_1980059607995420674.json, 图片生成/图生图/最强重绘OneReward-Fill 工作流 不限尺寸 想改啥改啥_1979444855506112514.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Fill -OneReward 万物重绘增强版_1980477800337616897.json、图片生成/图生图/Flux手动去水印_2006193627856379905.json、图片生成/图生图/OneReward-Fill 最强局部重绘 - 框选模式 （直出4K大图）_1982037924495663105.json、图片生成/图生图/OneReward-Fill 最强局部重绘 - 涂抹模式 （直出4K大图）_1980525783024357377.json、图片生成/图生图/OneReward-Fill-最强局部重绘-框选遮罩_1981340609220870145.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `ColorCorrect`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
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
- `easy boolean` —— 14/18 个有
- `CR Text` —— 12/18 个有
- `DeepTranslatorTextNode` —— 11/18 个有
- `LoraLoader` —— 4/18 个有
- `PrimitiveBoolean` —— 4/18 个有
- `RH_Translator` —— 4/18 个有
- `LoraLoaderModelOnly` —— 2/18 个有
- `easy showAnything` —— 2/18 个有
- `ApplyFBCacheOnModel` —— 1/18 个有
- `ImageConcatMulti` —— 1/18 个有
- `LayerMask: LoadSAM2Model` —— 1/18 个有
- `LayerMask: ObjectDetectorYOLO8` —— 1/18 个有
- `LayerMask: SAM2UltraV2` —— 1/18 个有
- `MaskPreview` —— 1/18 个有
- `Note Plus (mtb)` —— 1/18 个有
- `PreviewImage` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 18 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，18 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
