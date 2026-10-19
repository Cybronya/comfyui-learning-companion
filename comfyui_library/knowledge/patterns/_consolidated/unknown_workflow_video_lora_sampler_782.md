---
name: unknown_workflow_video_lora_sampler_782
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8745
common_nodes: [AudioSeparation, Display Int (rgthree), HuMoEmbeds, ImageFromBatch, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, SimpleMath+, SoundFlow_GetLength, SoundFlow_TrimAudio, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoCombineEmbeds, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader, WhisperModelLoader, easy imageRemBg, easy int]
problems: []
missing: []
members: [视频生成/图生视频/1968935101226704898.json, 音频生成/音频生成/Humo+Infinite talk音乐MV生成_1975845273735925761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_782

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1968935101226704898.json、音频生成/音频生成/Humo+Infinite talk音乐MV生成_1975845273735925761.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `Display Int (rgthree)`
- `HuMoEmbeds`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `SoundFlow_TrimAudio`
- `ToInt`
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
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `Anything Everywhere3` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
