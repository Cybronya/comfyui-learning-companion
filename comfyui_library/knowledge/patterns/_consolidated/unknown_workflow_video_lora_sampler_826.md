---
name: unknown_workflow_video_lora_sampler_826
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5585
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1998769286015504386.json, 视频生成/图生视频/2018217919682973698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_826

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1998769286015504386.json、视频生成/图生视频/2018217919682973698.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
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
- `DrawViTPose` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `PoseAndFaceDetection` —— 1/2 个有
- `PoseDetectionOneToAllAnimation` —— 1/2 个有
- `RepeatImageBatch` —— 1/2 个有
- `Text` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/2 个有
- `WanVideoUni3C_embeds` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
