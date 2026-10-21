---
name: unknown_workflow_video_lora_sampler_631
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.527667
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, ImageFromBatch, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewAny, PrimitiveFloat, PrimitiveInt, RIFE VFI, SaveAudio, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy sam3ModelLoader, easy sam3VideoSegmentation]
problems: []
missing: []
members: [视频生成/图生视频/2013817436742619137.json, 视频生成/图生视频/2013818136428027906.json, 视频生成/文生视频/多功能视频编辑WanAnimate V2_2035282698587086850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_631

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2013817436742619137.json、视频生成/图生视频/2013818136428027906.json、视频生成/文生视频/多功能视频编辑WanAnimate V2_2035282698587086850.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RIFE VFI`
- `SaveAudio`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `DrawViTPose` —— 2/3 个有
- `LayerMask: MaskInvert` —— 2/3 个有
- `MuyeTextEditOutput` —— 2/3 个有
- `OnnxDetectionModelLoader` —— 2/3 个有
- `PoseAndFaceDetection` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
