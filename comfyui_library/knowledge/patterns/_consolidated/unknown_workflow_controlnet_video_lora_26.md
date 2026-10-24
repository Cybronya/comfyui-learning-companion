---
name: unknown_workflow_controlnet_video_lora_26
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.524
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageBlend, ImageResizeKJv2, Int, LoadImage, MaskToImage, MemoryCleaner, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewAny, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy sam3GetObjectIds, easy sam3ModelLoader, easy sam3VideoModelExtraConfig, easy sam3VideoSegmentation, easy sam3Visualization]
problems: []
missing: []
members: [图片生成/图生图/空白工作流_2029100592844513281.json, 视频生成/图生视频/wan-2.2-人物替换-V5_2067889293686820865.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/空白工作流_2029100592844513281.json、视频生成/图生视频/wan-2.2-人物替换-V5_2067889293686820865.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageBlend`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `MaskToImage`
- `MemoryCleaner`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewAny`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy sam3GetObjectIds`
- `easy sam3ModelLoader`
- `easy sam3VideoModelExtraConfig`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`

**可变部分**（部分 workflow 才有）：
- `DuckHideNode` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `ZML_AnyTypeSwitchFive` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
