---
name: unknown_workflow_video_lora_sampler_774
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7955
common_nodes: [CLIPVisionLoader, DrawViTPose, INTConstant, ImageFromBatch, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json, 视频生成/图生视频/传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_774

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json、视频生成/图生视频/传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
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
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorToMask` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: ImageBlend V2` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `SDPoseOODLoader` —— 1/2 个有
- `SDPoseOODProcessor` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
