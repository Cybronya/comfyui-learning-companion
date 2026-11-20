---
name: unknown_workflow_video_lora_sampler_1137
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.708
common_nodes: [AppendStringsToList, CLIPVisionLoader, CreateShapeImageOnPath, LoadWanVideoT5TextEncoder, SplineEditor, VHS_VideoCombine, WanVideoATITracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【控制视频运动轨迹】字节ATI-Wan2.1图生视频（详细讲解使用）_1929446481839734785.json, 视频生成/图生视频/万相ATI轨迹控制_1928843752012681217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1137

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【控制视频运动轨迹】字节ATI-Wan2.1图生视频（详细讲解使用）_1929446481839734785.json、视频生成/图生视频/万相ATI轨迹控制_1928843752012681217.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `AppendStringsToList`
- `CLIPVisionLoader`
- `CreateShapeImageOnPath`
- `LoadWanVideoT5TextEncoder`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoATITracks`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `CogVideoEnhanceAVideo` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoadAndResizeImage` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
