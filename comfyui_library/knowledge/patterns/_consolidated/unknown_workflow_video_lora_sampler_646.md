---
name: unknown_workflow_video_lora_sampler_646
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.530333
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: ["视频生成/图生视频/WanAnimate_全新骨骼绑定优化版(更稳,细节更好)_1999863444146974722.json", 视频生成/图生视频/WanAnimate_去油版V2.3_1970903768109850626.json, 视频生成/文生视频/wan animate v2——优化版_1975351604679413761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_646

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/WanAnimate_全新骨骼绑定优化版(更稳,细节更好)_1999863444146974722.json、视频生成/图生视频/WanAnimate_去油版V2.3_1970903768109850626.json、视频生成/文生视频/wan animate v2——优化版_1975351604679413761.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
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

**可变部分**（部分 workflow 才有）：
- `ApplyFaceProcessor` —— 2/3 个有
- `ConvertAny2Float` —— 2/3 个有
- `FaceProcessorLoader` —— 2/3 个有
- `FrameSelector` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `SoundFlow_SetLength` —— 2/3 个有
- `Textbox` —— 2/3 个有
- `VideoInputPreprocessor` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ttN float` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有
- `PoseDetectionOneToAllAnimation` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `int _O` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
