---
name: unknown_workflow_video_lora_sampler_535
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.976
common_nodes: [AudioSeparation, Display Any (rgthree), Display Int (rgthree), HAIGC_VideoLastFrame, HuMoEmbeds, INTConstant, ImageBatchMulti, ImageFromBatch, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, Seed_, SimpleMath+, SoundFlow_GetLength, SoundFlow_TrimAudio, Text, ToFloat, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoCombineEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader, WhisperModelLoader, easy imageRemBg, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2034484341866237954.json, 视频生成/图生视频/2029082504245809153.json, 视频生成/图生视频/2032263750392225793.json, 视频生成/图生视频/2028749472515235842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_535

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2034484341866237954.json、视频生成/图生视频/2029082504245809153.json、视频生成/图生视频/2032263750392225793.json、视频生成/图生视频/2028749472515235842.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioSeparation`
- `Display Any (rgthree)`
- `Display Int (rgthree)`
- `HAIGC_VideoLastFrame`
- `HuMoEmbeds`
- `INTConstant`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `Seed_`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `SoundFlow_TrimAudio`
- `Text`
- `ToFloat`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoCombineEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
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
- `AudioBeforeAfterSilence` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `JWImageBatchCount` —— 1/4 个有
- `MaxNode` —— 1/4 个有
- `ZML_ImageBatchToInt` —— 1/4 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/4 个有
- `easy indexTTSGenerateSimple` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
