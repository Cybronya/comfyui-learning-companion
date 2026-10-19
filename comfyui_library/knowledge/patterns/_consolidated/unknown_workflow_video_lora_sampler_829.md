---
name: unknown_workflow_video_lora_sampler_829
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5325
common_nodes: [ApplyFaceProcessor, BlockifyMask, CLIPVisionLoader, ConvertAny2Float, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, FaceProcessorLoader, FrameSelector, GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageResizeKJv2, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewAudio, Sam2Segmentation, SetNode, SoundFlow_SetLength, Textbox, VHS_LoadVideo, VHS_VideoCombine, VideoInputPreprocessor, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything, ttN float]
problems: []
missing: []
members: [视频生成/图生视频/1999863444146974722.json, 视频生成/图生视频/1970903768109850626.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_829

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1999863444146974722.json、视频生成/图生视频/1970903768109850626.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFaceProcessor`
- `BlockifyMask`
- `CLIPVisionLoader`
- `ConvertAny2Float`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `FaceProcessorLoader`
- `FrameSelector`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewAudio`
- `Sam2Segmentation`
- `SetNode`
- `SoundFlow_SetLength`
- `Textbox`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VideoInputPreprocessor`
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
- `easy showAnything`
- `ttN float`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 1/2 个有
- `PoseDetectionOneToAllAnimation` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
