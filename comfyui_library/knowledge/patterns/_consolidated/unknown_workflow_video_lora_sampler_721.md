---
name: unknown_workflow_video_lora_sampler_721
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.674
common_nodes: [AppendStringsToList, CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, SplineEditor, VHS_VideoCombine, WanVideoATITracks, WanVideoATITracksVisualize, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1989933219632082946.json, 视频生成/图生视频/1929724832999489537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_721

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1989933219632082946.json、视频生成/图生视频/1929724832999489537.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `AppendStringsToList`
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoATITracks`
- `WanVideoATITracksVisualize`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
