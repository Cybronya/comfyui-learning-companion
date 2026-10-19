---
name: unknown_workflow_video_lora_sampler_25
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.788962
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: [SimpleMath+]
members: [图片生成/文生图/1956947526549999617.json, 图片生成/文生图/1958496258287681537.json, 数字人/数字人/5分钟图片生视频对口型+情感口播++数字人+InfiniTetalk+超自然数字人对口型_2093607637110837250.json, 数字人/数字人/InfiniteTalk超自然数字人对口型单人视频驱动_2089373497083650049.json, 数字人/数字人/口播  带货 数字人  对口型  InfiniTetalk 超自然数字人对口型_2092517680044658690.json, 数字人/数字人/图片数字人-z_2103458494379814913.json, 数字人/数字人/对口型 mv唱歌  数字人 InfiniTetalk 超自然数字人对口型_2089756106502529026.json, 数字人/数字人/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2089916243682877441.json, 数字人/数字人/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2092260355593560065.json, 数字人/数字人/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2100264026080104449.json, 数字人/数字人/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2103048752205488130.json, 数字人/数字人/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2103743133040332802.json, 数字人/数字人/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2103806861056241665.json, 数字人/数字人/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2108852311643746305.json, 数字人/数字人/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2111016982731644929.json, 数字人/数字人/对口型_情感口播_数字人_InfiniTetalk_超自然数字人对口型_2100930385105473538.json, 数字人/数字人/数字人 对口型 情感口播   InfiniTetalk 超自然数字人对口型_2085410347422408705.json, 视频生成/图生视频/2059562023511482369.json, 视频生成/图生视频/2059627314367000578.json, 视频生成/图生视频/对口型_情感口播_数字人_InfiniTetalk_超自然数字人对口型_2100789211803766786.json, 视频生成/图生视频/对口型_情感口播_数字人_InfiniTetalk_超自然数字人对口型_2_2100790214015934465.json, 视频生成/图生视频/对口型_情感口播_数字人_InfiniTetalk_超自然数字人对口型_3_2100791112670736385.json, 视频生成/图生视频/2067590324024864769.json, 音频生成/音频生成/InfiniTetalk 音频+视频转数字人 配音必备神器_1998731179878666242.json, 音频生成/音频生成/InfiniteTalk单人视频对口型_2048286460733820930.json, 音频生成/音频生成/InfiniteTalk超自然视频对口型-单人_2015602473221758978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/1956947526549999617.json、图片生成/文生图/1958496258287681537.json、数字人/数字人/5分钟图片生视频对口型+情感口播++数字人+InfiniTetalk+超自然数字人对口型_2093607637110837250.json、数字人/数字人/InfiniteTalk超自然数字人对口型单人视频驱动_2089373497083650049.json、数字人/数字人/口播  带货 数字人  对口型  InfiniTetalk 超自然数字人对口型_2092517680044658690.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 25/26 个有
- `GetNode` —— 25/26 个有
- `LoadWanVideoT5TextEncoder` —— 25/26 个有
- `SetNode` —— 25/26 个有
- `WanVideoImageToVideoMultiTalk` —— 25/26 个有
- `WanVideoTextEncode` —— 25/26 个有
- `Audio Duration (mtb)` —— 24/26 个有
- `AudioSeparation` —— 24/26 个有
- `GetImageRangeFromBatch` —— 24/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 24/26 个有
- `MathExpression|pysssss` —— 24/26 个有
- `PlaySound|pysssss` —— 24/26 个有
- `LoadImage` —— 22/26 个有
- `PreviewAudio` —— 8/26 个有
- `WanVideoTorchCompileSettings` —— 8/26 个有
- `easy int` —— 8/26 个有
- `easy showAnything` —— 8/26 个有
- `Anything Everywhere` —— 6/26 个有
- `PreviewImage` —— 5/26 个有
- `EmptyImage` —— 4/26 个有
- `VHS_LoadVideo` —— 4/26 个有
- `WanVideoEncode` —— 4/26 个有
- `ColorCorrectOfUtils` —— 2/26 个有
- `ImageCASharpening+` —— 2/26 个有
- `ImageResizeKJv2` —— 2/26 个有
- `RH_GetAudioDuration` —— 2/26 个有
- `SimpleMath+` —— 2/26 个有
- `VHS_VideoInfoLoaded` —— 2/26 个有
- `Getter` —— 1/26 个有
- `Int` —— 1/26 个有
- `LogicUtil_SleepNodeAny` —— 1/26 个有
- `Setter` —— 1/26 个有
- `WanVideoImageToVideoEncode` —— 1/26 个有
- `WanVideoTextEncodeCached` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+
