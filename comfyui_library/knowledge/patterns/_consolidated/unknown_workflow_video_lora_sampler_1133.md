---
name: unknown_workflow_video_lora_sampler_1133
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6765
common_nodes: [FantasyPortraitFaceDetector, FantasyPortraitModelLoader, GetNode, INTConstant, ImageResizeKJv2, LandmarksToImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFantasyPortrait, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【FantasyPortrait】复刻钟馗怒目圆睁表情_1958352739837362177.json, 视频生成/文生视频/Fantasy Portrait（文生视频）_1958515950276526081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1133

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【FantasyPortrait】复刻钟馗怒目圆睁表情_1958352739837362177.json、视频生成/文生视频/Fantasy Portrait（文生视频）_1958515950276526081.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `FantasyPortraitFaceDetector`
- `FantasyPortraitModelLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LandmarksToImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddFantasyPortrait`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoSetBlockSwap` —— 1/2 个有
- `WanVideoSetLoRAs` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
