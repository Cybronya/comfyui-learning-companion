---
name: unknown_workflow_video_lora_sampler_241
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.975556
common_nodes: [AudioSeparation, Display Int (rgthree), HuMoEmbeds, INTConstant, ImageAddMulti, ImageBatchMulti, ImageFromBatch, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, SimpleMath+, SoundFlow_GetLength, SoundFlow_TrimAudio, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoCombineEmbeds, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader, WhisperModelLoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2033171510558461953.json, 视频生成/图生视频/2031295926127566850.json, 视频生成/图生视频/2026262067400941570.json, 视频生成/图生视频/2022664705512316929.json, 视频生成/图生视频/2034600586854801410.json, 视频生成/图生视频/2041512808247988226.json, 视频生成/图生视频/2027669520621510658.json, 视频生成/图生视频/2046569919550066689.json, 视频生成/文生视频/双图参考生MTV三分镜视频 Humo+Infinite talk_2048690659820838913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_241

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2033171510558461953.json、视频生成/图生视频/2031295926127566850.json、视频生成/图生视频/2026262067400941570.json、视频生成/图生视频/2022664705512316929.json、视频生成/图生视频/2034600586854801410.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioSeparation`
- `Display Int (rgthree)`
- `HuMoEmbeds`
- `INTConstant`
- `ImageAddMulti`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
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
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 7/9 个有
- `ImageConcanate` —— 7/9 个有
- `PreviewAudio` —— 7/9 个有
- `RecordAudio` —— 7/9 个有
- `easy imageRemBg` —— 7/9 个有
- `CR Prompt Text` —— 2/9 个有
- `CR Text` —— 2/9 个有
- `PrimitiveFloat` —— 2/9 个有
- `Qwen3TTSModelLoader` —— 2/9 个有
- `Qwen3TTSVoiceDesign` —— 2/9 个有
- `SaveAudio` —— 2/9 个有
- `TextInput_` —— 2/9 个有
- `JWStringGetLine` —— 1/9 个有
- `JWStringSplit` —— 1/9 个有
- `JWStringToFloat` —— 1/9 个有
- `StringSubstring` —— 1/9 个有
- `TextBoxMira` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
