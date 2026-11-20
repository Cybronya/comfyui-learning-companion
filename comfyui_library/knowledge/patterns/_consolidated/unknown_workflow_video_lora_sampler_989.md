---
name: unknown_workflow_video_lora_sampler_989
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5925
common_nodes: [GetNode, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, RHHiddenNodes, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/wanvideo_Fun_2_2_control_深度图控制_2038434723374047234.json, 视频生成/图生视频/Wan2.2 FUN 控制模型 视频姿态动作迁移_1957318001500549121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_989

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/wanvideo_Fun_2_2_control_深度图控制_2038434723374047234.json、视频生成/图生视频/Wan2.2 FUN 控制模型 视频姿态动作迁移_1957318001500549121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RHHiddenNodes`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerMask: RemBgUltra` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoImageToVideoEncode_v2` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
