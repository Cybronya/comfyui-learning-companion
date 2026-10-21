---
name: unknown_workflow_video_lora_sampler_490
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7975
common_nodes: [CreateCFGScheduleFloatList, HuMoEmbeds, INTConstant, ImageBatchMulti, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: [SimpleMath+, easy int]
members: [视频生成/图生视频/1957726679996399618.json, 视频生成/文生视频/1968180863945027585.json, 视频生成/文生视频/1968279752563937282.json, 视频生成/文生视频/humo单图参考+配音_2072999564942286848.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_490

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1957726679996399618.json、视频生成/文生视频/1968180863945027585.json、视频生成/文生视频/1968279752563937282.json、视频生成/文生视频/humo单图参考+配音_2072999564942286848.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PreviewImage`
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
- `PreviewAudio` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `SaveImage` —— 2/4 个有
- `SoundFlow_GetLength` —— 2/4 个有
- `SoundFlow_TrimAudio` —— 2/4 个有
- `ToInt` —— 2/4 个有
- `easy int` —— 2/4 个有
- `AudioToFPS` —— 1/4 个有
- `IndexTTS2Run` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `SaveAudio` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `ttN text` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+、easy int
