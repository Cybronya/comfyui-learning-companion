---
name: unknown_workflow_video_sampler_vae_72
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.639143
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wanvideo_infinitetalk_单人工作流_1958061014984118274.json, 视频生成/图生视频/wanvideo_infinitetalk_双人工作流_1958075798320197633.json, 视频生成/图生视频/wanvideo_infinitetalk_图片转视频单人工作流_2014174614657703937.json, 视频生成/图生视频/万象视频MultiTalk——MV制造机_1943647883407360002.json, 视频生成/图生视频/数字人-图片-infinite 【720P+高清+声音克隆】_1958081939452342273.json, 视频生成/图生视频/数字人-文本驱动-图片+视频+声音克隆】_1989952363156918273.json, 音频生成/音频生成/数字人_视频_infinite【720P+高清+声音克隆】_1984533428567687169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_72

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/wanvideo_infinitetalk_单人工作流_1958061014984118274.json、视频生成/图生视频/wanvideo_infinitetalk_双人工作流_1958075798320197633.json、视频生成/图生视频/wanvideo_infinitetalk_图片转视频单人工作流_2014174614657703937.json、视频生成/图生视频/万象视频MultiTalk——MV制造机_1943647883407360002.json、视频生成/图生视频/数字人-图片-infinite 【720P+高清+声音克隆】_1958081939452342273.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 6/7 个有
- `WanVideoImageToVideoMultiTalk` —— 6/7 个有
- `WanVideoLoraSelect` —— 6/7 个有
- `WanVideoTextEncode` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `VHS_LoadVideo` —— 5/7 个有
- `INTConstant` —— 4/7 个有
- `LayerUtility: PurgeVRAM V2` —— 4/7 个有
- `RH_GetAudioDuration` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `Apply Whisper` —— 3/7 个有
- `Float to Int` —— 3/7 个有
- `ImageUpscaleWithModel` —— 3/7 个有
- `IndexTTS2Run` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `SaveAudio` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `UpscaleModelLoader` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 3/7 个有
- `easy anythingIndexSwitch` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `WanVideoContextOptions` —— 1/7 个有
- `WanVideoEncode` —— 1/7 个有
- `WanVideoEnhanceAVideo` —— 1/7 个有
- `WanVideoImageToVideoEncode` —— 1/7 个有
- `WanVideoSLG` —— 1/7 个有
- `WanVideoTextEncodeCached` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
