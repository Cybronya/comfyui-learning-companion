---
name: unknown_workflow_video_lora_sampler_356
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.906833
common_nodes: [CreateCFGScheduleFloatList, HuMoEmbeds, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, PreviewAudio, SimpleMath+, SoundFlow_GetLength, SoundFlow_TrimAudio, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader, easy int]
problems: []
missing: [SimpleMath+, easy int]
members: [视频生成/图生视频/1967417931208515586.json, 视频生成/图生视频/2037199894196264961.json, 视频生成/文生视频/1968279752563937282.json, 视频生成/文生视频/1966919444201136129.json, 视频生成/文生视频/humo单图参考+配音_2072999564942286848.json, 音频生成/音频生成/12.Humo电商展示+语音_录音_2000793155027038209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_356

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1967417931208515586.json、视频生成/图生视频/2037199894196264961.json、视频生成/文生视频/1968279752563937282.json、视频生成/文生视频/1966919444201136129.json、视频生成/文生视频/humo单图参考+配音_2072999564942286848.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `HuMoEmbeds`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `PreviewAudio`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `SoundFlow_TrimAudio`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WhisperModelLoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMulti` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `AudioSeparation` —— 4/6 个有
- `Display Int (rgthree)` —— 4/6 个有
- `ImageConcanate` —— 3/6 个有
- `LoadWanVideoT5TextEncoder` —— 3/6 个有
- `RecordAudio` —— 3/6 个有
- `WanVideoSetBlockSwap` —— 3/6 个有
- `WanVideoSetLoRAs` —— 3/6 个有
- `WanVideoTextEncode` —— 3/6 个有
- `WanVideoTextEncodeCached` —— 3/6 个有
- `easy imageRemBg` —— 3/6 个有
- `MelBandRoFormerModelLoader` —— 2/6 个有
- `MelBandRoFormerSampler` —— 2/6 个有
- `NormalizeAudioLoudness` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+、easy int
