---
name: unknown_workflow_video_sampler_clip_256
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.946
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImageResize+, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, WanVideoVRAMManagement]
problems: []
missing: []
members: [视频生成/图生视频/【首尾帧】Wan2.1 FLF2V首尾帧工作流-KJ版_1913886030926180353.json, 视频生成/图生视频/万相视频Wan2.1超级首尾帧控制_1905171860894437377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_256

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【首尾帧】Wan2.1 FLF2V首尾帧工作流-KJ版_1913886030926180353.json、视频生成/图生视频/万相视频Wan2.1超级首尾帧控制_1905171860894437377.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResize+`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `Upscale Model Loader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
