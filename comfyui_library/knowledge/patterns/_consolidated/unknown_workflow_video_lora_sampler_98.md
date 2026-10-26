---
name: unknown_workflow_video_lora_sampler_98
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.984875
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/251230002.infinitetalk图片对口型_2005797859406610434.json, 数字人/数字人/AA--数字人唱歌说话InfiniteTalk对口型图生视频_2006334086171860994.json, 数字人/数字人/AI对口型 唱歌 MV 数字人 超自然版本 InfiniTetalk_2070151514823417858.json, 数字人/数字人/IndexTTS语音克隆+Multitalk数字人对口型_2014970237870936065.json, 数字人/数字人/infinitetalk单人图片数字人_1998671281597861890.json, 数字人/数字人/infinitetalk数字人-灵影自用_1984800186230849537.json, 数字人/数字人/【数字人说话】 语音克隆音频驱动对口型_2056897514678345729.json, 数字人/数字人/数字人_1961694108299542529.json, 视频生成/图生视频/Multitalk数字人一条龙加强_1954868813227593730.json, 视频生成/图生视频/【数字人说话】 语音克隆音频驱动对口型 对口型数字人sonic【图片+音频】_1979755261789376514.json, 视频生成/图生视频/声音克隆+文字引导+图片生成数字人对口型说话-阿浩_2026920860375851010.json, 视频生成/图生视频/💂_IndexTTS语音克隆+Multitalk数字人对口型💂__1954737241992118273.json, 视频生成/文生视频/视频数字人对口 IndexTTS V2 带情绪的声音克隆 能生成一段音频，根据不同类型音调克隆声音_1994301248816037890.json, 音频生成/音频生成/IndexTTS语音克隆+Multitalk数字人对口型_1954811221523390466.json, 音频生成/音频生成/【数字人说话】 语音克隆音频驱动对口型_1957341883464871937.json, 音频生成/音频生成/【文字转音频】IndexTTS V2 带情绪的声音克隆 能生成一段音频，根据不同类型音调克隆声音_1986588000891109378.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_98

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（数字人/数字人/251230002.infinitetalk图片对口型_2005797859406610434.json、数字人/数字人/AA--数字人唱歌说话InfiniteTalk对口型图生视频_2006334086171860994.json、数字人/数字人/AI对口型 唱歌 MV 数字人 超自然版本 InfiniTetalk_2070151514823417858.json、数字人/数字人/IndexTTS语音克隆+Multitalk数字人对口型_2014970237870936065.json、数字人/数字人/infinitetalk单人图片数字人_1998671281597861890.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 15/16 个有
- `ImpactInt` —— 14/16 个有
- `CR Text` —— 13/16 个有
- `WanVideoTorchCompileSettings` —— 13/16 个有
- `Audio Duration (mtb)` —— 12/16 个有
- `ImageResizeKJv2` —— 11/16 个有
- `IndexTTSRun` —— 10/16 个有
- `MultiLinePromptIndex` —— 10/16 个有
- `SaveAudioMP3` —— 10/16 个有
- `AudioCrop` —— 6/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/16 个有
- `AudioSeparation` —— 4/16 个有
- `JWIntegerToString` —— 2/16 个有
- `CreateVideo` —— 1/16 个有
- `Float to Int` —— 1/16 个有
- `GetImageRangeFromBatch` —— 1/16 个有
- `INTConstant` —— 1/16 个有
- `MathExpression|pysssss` —— 1/16 个有
- `SaveVideo` —— 1/16 个有
- `SoundFlow_GetLength` —— 1/16 个有
- `ToInt` —— 1/16 个有
- `easy positive` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
