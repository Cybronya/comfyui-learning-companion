---
name: unknown_workflow_video_lora_sampler_745
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.824
common_nodes: [CreateCFGScheduleFloatList, HuMoEmbeds, INTConstant, ImageBatchMulti, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PreviewAudio, PreviewImage, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/IndexTTS2音频生成+Humo数字人_1957726679996399618.json, 视频生成/文生视频/humo单图参考+配音_1968279752563937282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_745

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/IndexTTS2音频生成+Humo数字人_1957726679996399618.json、视频生成/文生视频/humo单图参考+配音_1968279752563937282.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `HuMoEmbeds`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `PreviewAudio`
- `PreviewImage`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `AudioToFPS` —— 1/2 个有
- `IndexTTS2Run` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SoundFlow_GetLength` —— 1/2 个有
- `SoundFlow_TrimAudio` —— 1/2 个有
- `ToInt` —— 1/2 个有
- `easy int` —— 1/2 个有
- `ttN text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
