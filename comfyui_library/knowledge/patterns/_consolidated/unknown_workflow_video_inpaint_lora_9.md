---
name: unknown_workflow_video_inpaint_lora_9
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.748667
common_nodes: [AIO_Preprocessor, AddLabel, AddMask, CLIPTextEncode, CLIPVisionLoader, ColorMatch, DWPreprocessor, DualCLIPLoader, EmptyImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize+, GetImageSizeAndCount, GetNode, ImageBlend, ImageConcanate, ImageConcatMulti, ImageCrop+, ImagePadKJ, ImageResizeKJ, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerMask: ObjectDetectorYOLO8, LayerMask: PersonMaskUltra V2, LayerMask: SAM2Ultra, LayerStyle: ColorOverlay V2, LayerUtility: ColorImage V2, LayerUtility: CropByMask, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, Mask Threshold Region, MaskPreview+, MaskToImage, PreviewImage, Primitive integer [Crystools], ReduxAdvanced, SaveImage, SetNode, ShowText|pysssss, StyleModelLoader, SubtractMask, Switch any [Crystools], TeaCache, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Work-Fisher全自动换装+视频动作迁移_1966100651086442497.json, 视频生成/图生视频/全自动换装+视频动作迁移_2003707711252512769.json, 视频生成/图生视频/全自动换装+视频动作迁移_2056018798037225473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Work-Fisher全自动换装+视频动作迁移_1966100651086442497.json、视频生成/图生视频/全自动换装+视频动作迁移_2003707711252512769.json、视频生成/图生视频/全自动换装+视频动作迁移_2056018798037225473.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `AddMask`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ColorMatch`
- `DWPreprocessor`
- `DualCLIPLoader`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBlend`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageCrop+`
- `ImagePadKJ`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskGrow`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SAM2Ultra`
- `LayerStyle: ColorOverlay V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `Mask Threshold Region`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `ReduxAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StyleModelLoader`
- `SubtractMask`
- `Switch any [Crystools]`
- `TeaCache`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
