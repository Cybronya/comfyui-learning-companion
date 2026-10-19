---
name: unknown_workflow_video_lora_sampler_748
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.55
common_nodes: [DWPreprocessor, DepthAnythingV2Preprocessor, GetImageRangeFromBatch, GetNode, GrowMaskWithBlur, INTConstant, ImageConcatMulti, ImageResize+, ImageResizeKJ, Int, JjkConcat, LTXVPromptEnhancer, LTXVPromptEnhancerLoader, LayerMask: LoadFlorence2Model, LayerMask: LoadSegmentAnythingModels, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerMask: SegmentAnythingUltra V3, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, Mix Color By Mask, RH_Captioner, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoVRAMManagement, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1938493424595042306.json, 视频生成/图生视频/1934648294230695938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_748

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1938493424595042306.json、视频生成/图生视频/1934648294230695938.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResize+`
- `ImageResizeKJ`
- `Int`
- `JjkConcat`
- `LTXVPromptEnhancer`
- `LTXVPromptEnhancerLoader`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LayerMask: SegmentAnythingUltra V3`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `Mix Color By Mask`
- `RH_Captioner`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`
- `easy cleanGpuUsed`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
