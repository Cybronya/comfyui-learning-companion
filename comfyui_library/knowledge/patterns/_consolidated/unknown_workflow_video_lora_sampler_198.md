---
name: unknown_workflow_video_lora_sampler_198
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.932833
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinite Talk 视频生视频数字人（单人）_1958059584550219777.json, 数字人/数字人/Infinite Talk图片生成数字人_1959115013590036482.json, 数字人/数字人/Infinite Talk数字人_1958455819090214913.json, 数字人/数字人/Infinite Talk数字人视频生视频流双人版_2073262552674557954.json, 数字人/数字人/Infinite Talk超自然无限长度视频生视频数字人（单人）_1958011933066768385.json, 数字人/数字人/InfiniteTalk视频生数字人_1959476452968312833.json, 数字人/数字人/InfiniteTalk视频生数字人_1999076022924570625.json, 数字人/数字人/单人版InfiniteTalk超自然无限长度图生视频数字人_1965336268190138370.json, 视频生成/图生视频/Infinite Talk图片生成数字人_1999023790376017922.json, 视频生成/图生视频/wan2.2-图生数字人_1986321706753150978.json, 视频生成/图生视频/图生数字人+配音（自动匹配音频时长）_1986106739839946753.json, 视频生成/图生视频/西游唱歌infinitetalk工作流_1984917641024454657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_198

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/Infinite Talk 视频生视频数字人（单人）_1958059584550219777.json、数字人/数字人/Infinite Talk图片生成数字人_1959115013590036482.json、数字人/数字人/Infinite Talk数字人_1958455819090214913.json、数字人/数字人/Infinite Talk数字人视频生视频流双人版_2073262552674557954.json、数字人/数字人/Infinite Talk超自然无限长度视频生视频数字人（单人）_1958011933066768385.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `AudioCrop` —— 10/12 个有
- `GetImageRangeFromBatch` —— 9/12 个有
- `GetImageSizeAndCount` —— 9/12 个有
- `WanVideoEncode` —— 9/12 个有
- `Anything Everywhere` —— 8/12 个有
- `LoadImage` —— 7/12 个有
- `RH_GetAudioDuration` —— 7/12 个有
- `VHS_LoadVideo` —— 7/12 个有
- `CR String To Number` —— 6/12 个有
- `JWInteger` —— 6/12 个有
- `MathExpression|pysssss` —— 6/12 个有
- `easy showAnything` —— 6/12 个有
- `ImageBatchMulti` —— 4/12 个有
- `ReverseImageBatch` —— 4/12 个有
- `ImageResizeKJv2` —— 3/12 个有
- `Apply Whisper` —— 2/12 个有
- `LayerUtility: PurgeVRAM` —— 2/12 个有
- `Primitive integer [Crystools]` —— 2/12 个有
- `SoundFlow_TrimAudio` —— 2/12 个有
- `String Literal` —— 2/12 个有
- `VoxCPM_TTS` —— 2/12 个有
- `easy anythingIndexSwitch` —— 2/12 个有
- `Float to Int` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
