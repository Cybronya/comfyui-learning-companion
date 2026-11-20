---
name: unknown_workflow_video_lora_sampler_450
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.712429
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, Display Int (rgthree), DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, ImageConcatMulti, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/TTS+Infinitetalk视频添加语音视频对口型_2013150744169422849.json, 视频生成/文生视频/Aiwood-改进版KJ-Infinitetalk视频对口型工作流_1963994200775737346.json, 音频生成/音频生成/InfiniteTalk视频转视频音频【AI小王子】_1962038038358593538.json, 音频生成/音频生成/Infinitetalk视频添加语音视频对口型_1979388744887341058.json, 音频生成/音频生成/Wan2.1-InfiniteTalk--视频对口型_2042411569077821442.json, 音频生成/音频生成/infinitetalk对口型工作流_1995386268756402178.json, 音频生成/音频生成/视频对口型 音频驱动生视频   数字人 视频重绘 二次编辑_2063855129274707970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_450

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/TTS+Infinitetalk视频添加语音视频对口型_2013150744169422849.json、视频生成/文生视频/Aiwood-改进版KJ-Infinitetalk视频对口型工作流_1963994200775737346.json、音频生成/音频生成/InfiniteTalk视频转视频音频【AI小王子】_1962038038358593538.json、音频生成/音频生成/Infinitetalk视频添加语音视频对口型_1979388744887341058.json、音频生成/音频生成/Wan2.1-InfiniteTalk--视频对口型_2042411569077821442.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `Display Int (rgthree)`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `ToInt`
- `VHS_LoadVideo`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `easy int` —— 6/7 个有
- `INTConstant` —— 5/7 个有
- `ImageBatchMulti` —— 4/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `ReverseImageBatch` —— 4/7 个有
- `CR Text` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Float` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `IndexTTS2Run` —— 1/7 个有
- `JWIntegerToString` —— 1/7 个有
- `MegaTTS3` —— 1/7 个有
- `MultiLinePromptIndex` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `SaveAudioMP3` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
