---
name: unknown_workflow_video_sampler_vae_13
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.90055
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/infinitetalk数字人_2084490925362999297.json, 数字人/数字人/infinitetalk数字人_唱歌_口播_MV（视频驱动）_1995518772859568129.json, 数字人/数字人/infinitetalk数字人_唱歌_口播_MV（视频驱动）_2007303254241189889.json, 数字人/数字人/infinitetalk数字人_唱歌_口播_MV（视频驱动）_2032262989809717249.json, 数字人/数字人/infinitetalk数字人_唱歌_口播_MV（视频驱动）_2034574563287240705.json, 数字人/数字人/infinitetalk视频数字人_1998378694949396481.json, 数字人/数字人/infinitetalk视频数字人_2061112641858392065.json, 数字人/数字人/infinitetalk视频数字人_2061129593624551425.json, 数字人/数字人/infinitetalk视频数字人最新优化版_2032797229207003137.json, 数字人/数字人/视频对口型 infinite talk_1959510782524469249.json, 数字人/数字人/视频对口型(加速版)720p_2036439340041113601.json, 数字人/数字人/视频对口型-2_2081905037042868225.json, 数字人/数字人/视频对口型，效果完美_1972132760125173761.json, 数字人/数字人/视频数字人最新优化版infinitetalk_2035600145890418689.json, 数字人/数字人/视频数字人最新优化版infinitetalk_2045833153872400385.json, 数字人/数字人/超自然对口型唱歌_2034521956808138754.json, 视频生成/图生视频/InfiniteTalk数字人-唱歌自由_2018667682865881089.json, 视频生成/图生视频/数字人口播_2006243874485833729.json, 视频生成/图生视频/超强视频对口型（唱歌数字人））_2000589265400721409.json, 视频生成/图生视频/超自然对口型+视频数字人_2000608709594185729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_13

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（数字人/数字人/infinitetalk数字人_2084490925362999297.json、数字人/数字人/infinitetalk数字人_唱歌_口播_MV（视频驱动）_1995518772859568129.json、数字人/数字人/infinitetalk数字人_唱歌_口播_MV（视频驱动）_2007303254241189889.json、数字人/数字人/infinitetalk数字人_唱歌_口播_MV（视频驱动）_2032262989809717249.json、数字人/数字人/infinitetalk数字人_唱歌_口播_MV（视频驱动）_2034574563287240705.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 20 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 19/20 个有
- `GetImageRangeFromBatch` —— 18/20 个有
- `WanVideoTorchCompileSettings` —— 18/20 个有
- `WanVideoLoraSelect` —— 17/20 个有
- `easy int` —— 14/20 个有
- `Anything Everywhere` —— 13/20 个有
- `INTConstant` —— 13/20 个有
- `Audio Duration (mtb)` —— 5/20 个有
- `MathExpression|pysssss` —— 4/20 个有
- `WanVideoLoraSelectMulti` —— 4/20 个有
- `Int` —— 3/20 个有
- `LoadImage` —— 3/20 个有
- `VHS_VideoInfo` —— 3/20 个有
- `ImageFromBatch` —— 2/20 个有
- `JjkText` —— 2/20 个有
- `GetAudioDurationFromAudio` —— 1/20 个有
- `SimpleMath+` —— 1/20 个有
- `easy cleanGpuUsed` —— 1/20 个有
- `easy mathInt` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
