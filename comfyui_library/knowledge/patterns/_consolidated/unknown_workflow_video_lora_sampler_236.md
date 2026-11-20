---
name: unknown_workflow_video_lora_sampler_236
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.984091
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/251230002.infinitetalk图片对口型_2005797859406610434.json, 数字人/数字人/AA--数字人唱歌说话InfiniteTalk对口型图生视频_2006334086171860994.json, 数字人/数字人/AI对口型 唱歌 MV 数字人 超自然版本 InfiniTetalk_2070151514823417858.json, 数字人/数字人/IndexTTS语音克隆+Multitalk数字人对口型_2014970237870936065.json, 数字人/数字人/InfiniteTalk数字人图生长视频-自动对口型（支持唱歌_说话）_api+(8)_2078178475407659010.json, 数字人/数字人/infinitetalk单人图片数字人_1998671281597861890.json, 数字人/数字人/infinitetalk数字人-灵影自用_1984800186230849537.json, 数字人/数字人/【数字人说话】 语音克隆音频驱动对口型_2056897514678345729.json, 视频生成/图生视频/Multitalk数字人一条龙加强_1954868813227593730.json, 视频生成/图生视频/【数字人说话】 语音克隆音频驱动对口型 对口型数字人sonic【图片+音频】_1979755261789376514.json, 视频生成/图生视频/声音克隆+文字引导+图片生成数字人对口型说话-阿浩_2026920860375851010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_236

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/251230002.infinitetalk图片对口型_2005797859406610434.json、数字人/数字人/AA--数字人唱歌说话InfiniteTalk对口型图生视频_2006334086171860994.json、数字人/数字人/AI对口型 唱歌 MV 数字人 超自然版本 InfiniTetalk_2070151514823417858.json、数字人/数字人/IndexTTS语音克隆+Multitalk数字人对口型_2014970237870936065.json、数字人/数字人/InfiniteTalk数字人图生长视频-自动对口型（支持唱歌_说话）_api+(8)_2078178475407659010.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
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
- `SimpleMath+` —— 10/11 个有
- `ImpactInt` —— 8/11 个有
- `Audio Duration (mtb)` —— 7/11 个有
- `CR Text` —— 7/11 个有
- `ImageResizeKJv2` —— 7/11 个有
- `WanVideoTorchCompileSettings` —— 7/11 个有
- `AudioCrop` —— 6/11 个有
- `AudioSeparation` —— 5/11 个有
- `IndexTTSRun` —— 5/11 个有
- `MultiLinePromptIndex` —— 5/11 个有
- `SaveAudioMP3` —— 5/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/11 个有
- `Float to Int` —— 2/11 个有
- `SoundFlow_GetLength` —— 2/11 个有
- `CreateVideo` —— 1/11 个有
- `GetImageRangeFromBatch` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `Int` —— 1/11 个有
- `JWIntegerToString` —— 1/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `SaveVideo` —— 1/11 个有
- `ToInt` —— 1/11 个有
- `easy positive` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
