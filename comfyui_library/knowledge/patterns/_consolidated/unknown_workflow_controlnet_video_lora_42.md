---
name: unknown_workflow_controlnet_video_lora_42
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4915
common_nodes: [CLIPVisionLoader, CR Prompt Text, GetNode, ImageResizeKJv2, JWInteger, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SDPoseOODLoader, SDPoseOODProcessor, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Animate动作迁移[教学注释]_2039186628425551874.json, 视频生成/图生视频/animate动作迁移_1983367608349171713.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_42

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Animate动作迁移[教学注释]_2039186628425551874.json、视频生成/图生视频/animate动作迁移_1983367608349171713.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `GetNode`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `DrawViTPose` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `GroundingDinoModelLoader_SDPose` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `PDIMAGE_LongerSize` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有
- `TT_img_enc_v2` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
