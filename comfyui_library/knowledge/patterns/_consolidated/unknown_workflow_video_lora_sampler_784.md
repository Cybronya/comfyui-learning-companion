---
name: unknown_workflow_video_lora_sampler_784
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, GetImageSizeAndCount, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, VHS_VideoCombine, WanVideoAddAudioEmbeds, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1981025809483829250.json, 视频生成/图生视频/1960662179517259778.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_784

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1981025809483829250.json、视频生成/图生视频/1960662179517259778.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `VHS_VideoCombine`
- `WanVideoAddAudioEmbeds`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_SplitImages` —— 1/2 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
