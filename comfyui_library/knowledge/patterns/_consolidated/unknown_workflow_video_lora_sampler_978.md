---
name: unknown_workflow_video_lora_sampler_978
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.929
common_nodes: [BboxDetectorCombined_v2, GetImageSizeAndCount, GrowMaskWithBlur, ImageBatchToList, ImageCompositeMasked, ImageCropByMask, ImageFromBatch+, ImageRepeat, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, MaskComposite, MaskToImage, MathExpression|pysssss, RepeatImageBatch, SolidMask, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEasyCache, WanVideoEncode, WanVideoLoraSelect, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoSetRadialAttention, WanVideoTextEncode, WanVideoVAELoader, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy indexAnything, easy showAnything, easy showTensorShape]
problems: []
missing: []
members: [平台全量/V7 视频去水印 自动识别横竖屏_1974767152681103361.json, 平台全量/Wan_MiniMax_Remover-视频去字幕+水印去除工作流_1976309238094012417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_978

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/V7 视频去水印 自动识别横竖屏_1974767152681103361.json、平台全量/Wan_MiniMax_Remover-视频去字幕+水印去除工作流_1976309238094012417.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BboxDetectorCombined_v2`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `ImageBatchToList`
- `ImageCompositeMasked`
- `ImageCropByMask`
- `ImageFromBatch+`
- `ImageRepeat`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `MaskComposite`
- `MaskToImage`
- `MathExpression|pysssss`
- `RepeatImageBatch`
- `SolidMask`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetRadialAttention`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy indexAnything`
- `easy showAnything`
- `easy showTensorShape`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
