---
name: unknown_workflow_video_lora_sampler_723
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.582
common_nodes: [Display Int (rgthree), GetImageRangeFromBatch, GetNode, HuMoEmbeds, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, SoundFlow_GetLength, SoundFlow_TrimAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoCombineEmbeds, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader, WhisperModelLoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/48. 多镜头长音频：Humo+Infinite MV直接生成_1984202703800778754.json, 视频生成/图生视频/单镜头：Humo+Infinite MV直接生成_1982621163400642562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_723

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/48. 多镜头长音频：Humo+Infinite MV直接生成_1984202703800778754.json、视频生成/图生视频/单镜头：Humo+Infinite MV直接生成_1982621163400642562.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `Display Int (rgthree)`
- `GetImageRangeFromBatch`
- `GetNode`
- `HuMoEmbeds`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `SoundFlow_GetLength`
- `SoundFlow_TrimAudio`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoCombineEmbeds`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`
- `WhisperModelLoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy promptLine` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
