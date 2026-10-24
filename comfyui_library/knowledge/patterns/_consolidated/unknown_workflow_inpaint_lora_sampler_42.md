---
name: unknown_workflow_inpaint_lora_sampler_42
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.496333
common_nodes: [Any Switch (rgthree), Bookmark (rgthree), CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ClothesSegment, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, Fast Groups Muter (rgthree), FluxGuidance, GetNode, ImageCrop+, ImageResizeKJv2, ImageToMask, InpaintModelConditioning, InpaintStitch, KSampler, Label (rgthree), LayerUtility: CropByMask V2, LoadImage, Mask Fill Holes, MaskToImage, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, PreviewImage, PrimitiveString, PrimitiveStringMultiline, RHHiddenNodes, RH_Translator, RMBG, SaveImage, SetNode, StringConcatenate, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy int, easy isMaskEmpty, easy makeImageForICLora, easy seed]
problems: []
missing: []
members: [图片生成/图生图/万物迁移 全功能V2-OneReward_1946894036416520193.json, 图片生成/图生图/最新OneReward全面万物迁移_1967256410645991425.json, 图片生成/文生图/万物迁移 全功能工作流 （Fill- OneReward）_1968918299654410242.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/万物迁移 全功能V2-OneReward_1946894036416520193.json、图片生成/图生图/最新OneReward全面万物迁移_1967256410645991425.json、图片生成/文生图/万物迁移 全功能工作流 （Fill- OneReward）_1968918299654410242.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bookmark (rgthree)`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ClothesSegment`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `GetNode`
- `ImageCrop+`
- `ImageResizeKJv2`
- `ImageToMask`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `Mask Fill Holes`
- `MaskToImage`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `RH_Translator`
- `RMBG`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy int`
- `easy isMaskEmpty`
- `easy makeImageForICLora`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Mute / Bypass Relay (rgthree)` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageAndMaskPreview` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
