---
name: unknown_workflow_video_lora_sampler_954
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.693
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Text, Display Int (rgthree), DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [音频生成/音频生成/infinitetalk对口型工作流_1995386268756402178.json, 音频生成/音频生成/视频对口型 音频驱动生视频   数字人 视频重绘 二次编辑_2063855129274707970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_954

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/infinitetalk对口型工作流_1995386268756402178.json、音频生成/音频生成/视频对口型 音频驱动生视频   数字人 视频重绘 二次编辑_2063855129274707970.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `Display Int (rgthree)`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `ToInt`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `JWIntegerToString` —— 1/2 个有
- `ReverseImageBatch` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
