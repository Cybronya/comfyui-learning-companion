---
name: unknown_workflow_video_lora_sampler_724
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.616
common_nodes: [AudioEvenSplitNode, AudioSelectNode, AudioSplitNode, Display Int (rgthree), GetImageRangeFromBatch, GetNode, HuMoEmbeds, ImageStringBatch, JWDatetimeString, LoadAudio, LoadImage, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, PreviewImage, PrimitiveStringMultiline, RandomPrompt, SelectImageString, SetNode, ShowText|pysssss, SoundFlow_GetLength, SoundFlow_TrimAudio, Text, VHS_VideoCombine, VideoTransitionNode, WanVideoBlockSwap, WanVideoCombineEmbeds, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader, WhisperModelLoader, easy batchAnything, easy clearCacheAll, easy forLoopEnd, easy forLoopStart, easy int, easy textSwitch]
problems: []
missing: []
members: [视频生成/图生视频/50. 智能分割音频 多张照片提示词引作分镜  humo+infinite 长视频转场MV_1985906370425827330.json, 视频生成/图生视频/数字人humo+infinite-长视频+转场_1986239863164993538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_724

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/50. 智能分割音频 多张照片提示词引作分镜  humo+infinite 长视频转场MV_1985906370425827330.json、视频生成/图生视频/数字人humo+infinite-长视频+转场_1986239863164993538.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEvenSplitNode`
- `AudioSelectNode`
- `AudioSplitNode`
- `Display Int (rgthree)`
- `GetImageRangeFromBatch`
- `GetNode`
- `HuMoEmbeds`
- `ImageStringBatch`
- `JWDatetimeString`
- `LoadAudio`
- `LoadImage`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomPrompt`
- `SelectImageString`
- `SetNode`
- `ShowText|pysssss`
- `SoundFlow_GetLength`
- `SoundFlow_TrimAudio`
- `Text`
- `VHS_VideoCombine`
- `VideoTransitionNode`
- `WanVideoBlockSwap`
- `WanVideoCombineEmbeds`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`
- `WhisperModelLoader`
- `easy batchAnything`
- `easy clearCacheAll`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `GODMT_AnyCast` —— 1/2 个有
- `Int2Any_AS` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
