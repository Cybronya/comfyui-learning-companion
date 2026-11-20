---
name: unknown_workflow_controlnet_inpaint_lora_13
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.456333
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPVisionLoader, ConditioningZeroOut, ControlNetLoader, DWPreprocessor, DifferentialDiffusion, EmptyImage, FluxGuidance, GetNode, ImageCrop+, ImageToMask, InpaintModelConditioning, KSamplerSelect, LayerColor: Brightness & Contrast, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewImage, RH_Translator, RandomNoise, RebatchLatents, ReduxAdvanced, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, StyleModelLoader, TeaCache, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageConcat]
problems: []
missing: []
members: [平台全量/😯Flux.1 fill+ACE+Redux （自动抠图版）换装_服装迁移_1953165783826370561.json, 平台全量/😯Flux.1 fill+ACE+Redux+CN 主体置换到场景_替换人物_人物迁移_1931796829946445826.json, 平台全量/😯Flux.1 fill+ACE+Redux+CN （手动版）换装_服装迁移_主体迁移_万物迁移_1932615546397466626.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/😯Flux.1 fill+ACE+Redux （自动抠图版）换装_服装迁移_1953165783826370561.json、平台全量/😯Flux.1 fill+ACE+Redux+CN 主体置换到场景_替换人物_人物迁移_1931796829946445826.json、平台全量/😯Flux.1 fill+ACE+Redux+CN （手动版）换装_服装迁移_主体迁移_万物迁移_1932615546397466626.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DWPreprocessor`
- `DifferentialDiffusion`
- `EmptyImage`
- `FluxGuidance`
- `GetNode`
- `ImageCrop+`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSamplerSelect`
- `LayerColor: Brightness & Contrast`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `RH_Translator`
- `RandomNoise`
- `RebatchLatents`
- `ReduxAdvanced`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `StyleModelLoader`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `BackgroundScaler` —— 2/3 个有
- `CFGZeroStar` —— 2/3 个有
- `CLIPTextEncodeFlux` —— 2/3 个有
- `ControlNetApplySD3` —— 2/3 个有
- `DualCLIPLoaderGGUF` —— 2/3 个有
- `LayerMask: PersonMaskUltra V2` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `ApplyInstantID` —— 1/3 个有
- `BiRefNetRMBG` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `ImageAndMaskPreview` —— 1/3 个有
- `InpaintCropImproved` —— 1/3 个有
- `InpaintStitchImproved` —— 1/3 个有
- `InstantIDFaceAnalysis` —— 1/3 个有
- `InstantIDModelLoader` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/3 个有
- `Masks Combine Regions` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `SubtractMask` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1.5 | - | 1 | 100% |
| 采样算法 | dpmpp_2m | - | 1 | 100% |
| 调度器 | karras | - | 1 | 100% |
| 重绘幅度 | 0.5 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
