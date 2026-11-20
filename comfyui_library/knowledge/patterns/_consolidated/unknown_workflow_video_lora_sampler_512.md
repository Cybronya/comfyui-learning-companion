---
name: unknown_workflow_video_lora_sampler_512
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.975
common_nodes: [AudioSeparation, Display Int (rgthree), HuMoEmbeds, INTConstant, ImageFromBatch, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, SimpleMath+, SoundFlow_GetLength, SoundFlow_TrimAudio, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoCombineEmbeds, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader, WhisperModelLoader, easy imageRemBg, easy int]
problems: []
missing: []
members: [视频生成/图生视频/上传音频生成对应口播视频—Humo+Infinite+talk 优化后_2034484341866237954.json, 视频生成/图生视频/上传音频生成对应口播视频—Humo+Infinite+talk_2029082504245809153.json, 视频生成/图生视频/上传音频生成对应口播视频—Humo+Infinite+talk_2032263750392225793.json, 视频生成/图生视频/电商专用：口播视频—Humo+Infinite talk+IndexTTS_2028749472515235842.json, 音频生成/音频生成/Humo+Infinite talk音乐MV生成_1975845273735925761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_512

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/上传音频生成对应口播视频—Humo+Infinite+talk 优化后_2034484341866237954.json、视频生成/图生视频/上传音频生成对应口播视频—Humo+Infinite+talk_2029082504245809153.json、视频生成/图生视频/上传音频生成对应口播视频—Humo+Infinite+talk_2032263750392225793.json、视频生成/图生视频/电商专用：口播视频—Humo+Infinite talk+IndexTTS_2028749472515235842.json、音频生成/音频生成/Humo+Infinite talk音乐MV生成_1975845273735925761.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioSeparation`
- `Display Int (rgthree)`
- `HuMoEmbeds`
- `INTConstant`
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
- `Display Any (rgthree)` —— 4/5 个有
- `HAIGC_VideoLastFrame` —— 4/5 个有
- `ImageBatchMulti` —— 4/5 个有
- `Seed_` —— 4/5 个有
- `Text` —— 4/5 个有
- `ToFloat` —— 4/5 个有
- `WanVideoEncode` —— 4/5 个有
- `AudioBeforeAfterSilence` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `JWImageBatchCount` —— 1/5 个有
- `MaxNode` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `ZML_ImageBatchToInt` —— 1/5 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/5 个有
- `easy indexTTSGenerateSimple` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
