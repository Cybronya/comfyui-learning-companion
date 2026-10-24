---
name: unknown_workflow_video_lora_sampler_211
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.930333
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Infinite Talk图片生成数字人_1999023790376017922.json, 视频生成/图生视频/Infinite Talk数字人图生视频流V2极速版_2073246385209700353.json, 视频生成/图生视频/Infinite Talk数字人图生视频流双人版_2073246674415349762.json, 视频生成/图生视频/InfiniteTalk数字人-唱歌自由_2018667682865881089.json, 视频生成/图生视频/wan2.2-图生数字人_1986321706753150978.json, 视频生成/图生视频/【亲测好用】最强视频数字人对口型万相wan2.1Q8+InfiniteTalk+VoxCPM TTS超长超自然_1994362409961857025.json, 视频生成/图生视频/图生数字人+配音（自动匹配音频时长）_1986106739839946753.json, 视频生成/图生视频/西游唱歌infinitetalk工作流_1984917641024454657.json, 音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_211

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Infinite Talk图片生成数字人_1999023790376017922.json、视频生成/图生视频/Infinite Talk数字人图生视频流V2极速版_2073246385209700353.json、视频生成/图生视频/Infinite Talk数字人图生视频流双人版_2073246674415349762.json、视频生成/图生视频/InfiniteTalk数字人-唱歌自由_2018667682865881089.json、视频生成/图生视频/wan2.2-图生数字人_1986321706753150978.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
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
- `GetImageRangeFromBatch` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `WanVideoEncode` —— 7/9 个有
- `Anything Everywhere` —— 6/9 个有
- `CR Prompt Text` —— 6/9 个有
- `GetImageSizeAndCount` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `AudioCrop` —— 5/9 个有
- `ImageResizeKJv2` —— 5/9 个有
- `RH_GetAudioDuration` —— 5/9 个有
- `Apply Whisper` —— 4/9 个有
- `JWInteger` —— 4/9 个有
- `SoundFlow_TrimAudio` —— 4/9 个有
- `String Literal` —— 4/9 个有
- `VoxCPM_TTS` —— 4/9 个有
- `Float to Int` —— 3/9 个有
- `INTConstant` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `CR String To Number` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `easy anythingIndexSwitch` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `GetNode` —— 1/9 个有
- `ImageBatchMulti` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `ReverseImageBatch` —— 1/9 个有
- `WanVideoTorchCompileSettings` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
