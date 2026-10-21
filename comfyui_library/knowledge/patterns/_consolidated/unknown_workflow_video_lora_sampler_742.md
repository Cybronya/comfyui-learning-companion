---
name: unknown_workflow_video_lora_sampler_742
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.822
common_nodes: [AddLabel, AudioSeparation, DWPreprocessor, DownloadAndLoadWav2VecModel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImagePadKJ, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MaskPreview, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/1949185140044570626.json, 视频生成/图生视频/1949385467585822721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_742

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1949185140044570626.json、视频生成/图生视频/1949385467585822721.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `AudioSeparation`
- `DWPreprocessor`
- `DownloadAndLoadWav2VecModel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
