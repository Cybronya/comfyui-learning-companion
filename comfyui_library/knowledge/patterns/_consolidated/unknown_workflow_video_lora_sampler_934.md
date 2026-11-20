---
name: unknown_workflow_video_lora_sampler_934
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.518
common_nodes: [BlockifyMask, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageConcatMulti, ImageResizeKJv2, JWInteger, LayerMask: MaskPreview, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SAM3_Detect, SDPoseDrawKeypoints, SDPoseKeypointExtractor, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2animate视频人物替换_1969420590102814722.json, 视频生成/图生视频/wananimate视频动作迁移_1969490471846354945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_934

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan2.2animate视频人物替换_1969420590102814722.json、视频生成/图生视频/wananimate视频动作迁移_1969490471846354945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerMask: MaskPreview`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SAM3_Detect`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
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

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
