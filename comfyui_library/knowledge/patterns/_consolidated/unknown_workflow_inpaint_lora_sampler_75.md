---
name: unknown_workflow_inpaint_lora_sampler_75
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.687
common_nodes: [Anything Everywhere3, CLIPTextEncodeFlux, CLIPVisionLoader, CR Text, DeepTranslatorTextNode, DualCLIPLoader, GrowMaskWithBlur, InpaintModelConditioning, Int, KSampler (Efficient), LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskPreview, LayerUtility: CropByMask, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, PreviewImage, ReduxAdvanced, SDVN IC Lora Layout, SDVN IC Lora Layout Crop, SaveImage, Seed (rgthree), StyleModelLoader, UNETLoader, VAELoader, XY Input: Seeds++ Batch, XY Plot, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/「MCN」外景号视频生成_1955092873155788801.json, 数字人/数字人/物品替换通用_1967486177882333185.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_75

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/「MCN」外景号视频生成_1955092873155788801.json、数字人/数字人/物品替换通用_1967486177882333185.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `CR Text`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `InpaintModelConditioning`
- `Int`
- `KSampler (Efficient)`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskPreview`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReduxAdvanced`
- `SDVN IC Lora Layout`
- `SDVN IC Lora Layout Crop`
- `SaveImage`
- `Seed (rgthree)`
- `StyleModelLoader`
- `UNETLoader`
- `VAELoader`
- `XY Input: Seeds++ Batch`
- `XY Plot`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `CreateCFGScheduleFloatList` —— 1/2 个有
- `Float` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `Text Random Line` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoDecode` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoModelLoader` —— 1/2 个有
- `WanVideoSampler` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoVAELoader` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
