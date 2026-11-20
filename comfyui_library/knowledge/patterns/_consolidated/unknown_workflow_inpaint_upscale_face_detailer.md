---
name: unknown_workflow_inpaint_upscale_face_detailer
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8545
common_nodes: [Anything Everywhere, BasicScheduler, BboxDetectorSEGS, BiRefNet_Hugo, CFGGuider, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Apply LoRA Stack, CR Simple Image Compare, CR Text, ConditioningZeroOut, DepthAnything_V2, DifferentialDiffusion, DownloadAndLoadDepthAnythingV2Model, DownloadAndLoadFlorence2Model, DualCLIPLoader, EmptyImage, FaceDetailer, Float, Florence2Run, FluxGuidance, GetImageSize+, GetNode, ImageConcanate, ImageCrop, ImageResizeKJ, ImageToMask, InpaintModelConditioning, InstructPixToPixConditioning, KSampler, KSamplerSelect, LayerFilter: HDREffects, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingFlux, Multi Text Merge, PreviewImage, RH_Captioner, RMBG, RandomNoise, ReduxAdvanced, SamplerCustomAdvanced, SaveImage, Seed Everywhere, SegsToCombinedMask, SetNode, ShowText|pysssss, StyleModelApply, StyleModelLoader, TextCombinerTwo, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageSize, easy loraStack]
problems: []
missing: []
members: [图片生成/图生图/人物迁移_1965795383853101057.json, 平台全量/一致性人物迁移_基础版_1890882306801016834.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人物迁移_1965795383853101057.json、平台全量/一致性人物迁移_基础版_1890882306801016834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BasicScheduler`
- `BboxDetectorSEGS`
- `BiRefNet_Hugo`
- `CFGGuider`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Apply LoRA Stack`
- `CR Simple Image Compare`
- `CR Text`
- `ConditioningZeroOut`
- `DepthAnything_V2`
- `DifferentialDiffusion`
- `DownloadAndLoadDepthAnythingV2Model`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `EmptyImage`
- `FaceDetailer`
- `Float`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize+`
- `GetNode`
- `ImageConcanate`
- `ImageCrop`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `InstructPixToPixConditioning`
- `KSampler`
- `KSamplerSelect`
- `LayerFilter: HDREffects`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingFlux`
- `Multi Text Merge`
- `PreviewImage`
- `RH_Captioner`
- `RMBG`
- `RandomNoise`
- `ReduxAdvanced`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `SegsToCombinedMask`
- `SetNode`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `TextCombinerTwo`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy loraStack`

**可变部分**（部分 workflow 才有）：
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
