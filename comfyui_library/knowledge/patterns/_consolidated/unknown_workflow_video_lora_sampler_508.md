---
name: unknown_workflow_video_lora_sampler_508
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.864833
common_nodes: [AudioCrop, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/数字人-口播_2088243121611173889.json, 数字人/数字人/数字人_1961694108299542529.json, 数字人/数字人/数字人项目_1986113856391053314.json, 视频生成/图生视频/数字人-图片-infinite 【720P+高清+声音克隆】_1958081939452342273.json, 视频生成/图生视频/数字人-文本驱动-图片+视频+声音克隆】_1989952363156918273.json, 音频生成/音频生成/数字人_视频_infinite【720P+高清+声音克隆】_1984533428567687169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_508

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/数字人-口播_2088243121611173889.json、数字人/数字人/数字人_1961694108299542529.json、数字人/数字人/数字人项目_1986113856391053314.json、视频生成/图生视频/数字人-图片-infinite 【720P+高清+声音克隆】_1958081939452342273.json、视频生成/图生视频/数字人-文本驱动-图片+视频+声音克隆】_1989952363156918273.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 5/6 个有
- `Float to Int` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `LoadWanVideoT5TextEncoder` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `RH_GetAudioDuration` —— 5/6 个有
- `WanVideoTextEncode` —— 5/6 个有
- `easy anythingIndexSwitch` —— 5/6 个有
- `Apply Whisper` —— 4/6 个有
- `IndexTTS2Run` —— 4/6 个有
- `SaveAudio` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `ImageUpscaleWithModel` —— 3/6 个有
- `LayerUtility: PurgeVRAM V2` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `UpscaleModelLoader` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `JWIntegerToString` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `OmniVoiceVoiceCloneTTS` —— 1/6 个有
- `OmniVoiceWhisperLoader` —— 1/6 个有
- `SaveAudioMP3` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `SeedVR2BlockSwap` —— 1/6 个有
- `WanVideoEncode` —— 1/6 个有
- `WanVideoTextEncodeCached` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
