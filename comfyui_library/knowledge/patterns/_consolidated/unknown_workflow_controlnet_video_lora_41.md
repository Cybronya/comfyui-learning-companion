---
name: unknown_workflow_controlnet_video_lora_41
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9545
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageResizeKJv2, JWInteger, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Animate 动作迁移（单人、多人、非人）_2036708435315658754.json, 视频生成/图生视频/吴京梗 _ 无音频动作&表情迁移 _ 采访类视频_1983890278471925762.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_41

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Animate 动作迁移（单人、多人、非人）_2036708435315658754.json、视频生成/图生视频/吴京梗 _ 无音频动作&表情迁移 _ 采访类视频_1983890278471925762.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoSetBlockSwap` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
