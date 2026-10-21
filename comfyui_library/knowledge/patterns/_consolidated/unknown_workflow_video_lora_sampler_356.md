---
name: unknown_workflow_video_lora_sampler_356
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.945667
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1999023790376017922.json, 视频生成/图生视频/1986321706753150978.json, 视频生成/图生视频/1994362409961857025.json, 视频生成/图生视频/1986106739839946753.json, 视频生成/图生视频/1984917641024454657.json, 音频生成/音频生成/wan 2.2 数字人对口型_1986380429831925762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_356

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1999023790376017922.json、视频生成/图生视频/1986321706753150978.json、视频生成/图生视频/1994362409961857025.json、视频生成/图生视频/1986106739839946753.json、视频生成/图生视频/1984917641024454657.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 5/6 个有
- `RH_GetAudioDuration` —— 5/6 个有
- `Apply Whisper` —— 4/6 个有
- `CR Prompt Text` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `SoundFlow_TrimAudio` —— 4/6 个有
- `String Literal` —— 4/6 个有
- `VoxCPM_TTS` —— 4/6 个有
- `Float to Int` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `AudioCrop` —— 2/6 个有
- `CR String To Number` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `easy anythingIndexSwitch` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `ImageBatchMulti` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `ReverseImageBatch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
