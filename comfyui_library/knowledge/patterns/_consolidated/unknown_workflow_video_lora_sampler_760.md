---
name: unknown_workflow_video_lora_sampler_760
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.574
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, GetNode, ImageResizeKJv2, IndexTTS2Run, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoPassImagesFromSamples, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/1993149833712254977.json, 视频生成/图生视频/2072325525946851330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_760

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1993149833712254977.json、视频生成/图生视频/2072325525946851330.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `IndexTTS2Run`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoPassImagesFromSamples`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `AudioToFPS` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImpactConditionalBranch` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
