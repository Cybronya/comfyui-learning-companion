---
name: unknown_workflow_video_lora_sampler_207
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9378
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk视频转数字人-V2V_2042509042618208258.json, 数字人/数字人/Infinitetalk视频转数字人-动态更强更自然_2043528487876694017.json, 数字人/数字人/WH-AI-Studio视频生视频数字人-视频对口型（带情感音频生成）_2022275473673297921.json, 数字人/数字人/【AI代码侠土豆】V2V-Infinitetalk视频转数字人_1990280525246066689.json, 数字人/数字人/数字人视频生视频_2004472334562066434.json, 数字人/数字人/数字人视频生视频_2041675802936352769.json, 数字人/数字人/🍐Infinitetalk视频转数字人🍐_2017760163519799298.json, 视频生成/图生视频/InfiniteTalk图像双人对口型_1971843495331819522.json, 视频生成/图生视频/Infinitetalk视频转数字人-动态更强更自然_2114345766474051586.json, 视频生成/图生视频/Infinitetalk视频转数字人｜动态更强更自然的图生视频方案_2114631993609773057.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_207

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/Infinitetalk视频转数字人-V2V_2042509042618208258.json、数字人/数字人/Infinitetalk视频转数字人-动态更强更自然_2043528487876694017.json、数字人/数字人/WH-AI-Studio视频生视频数字人-视频对口型（带情感音频生成）_2022275473673297921.json、数字人/数字人/【AI代码侠土豆】V2V-Infinitetalk视频转数字人_1990280525246066689.json、数字人/数字人/数字人视频生视频_2004472334562066434.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `SimpleMath+` —— 9/10 个有
- `PrimitiveInt` —— 7/10 个有
- `Float to Int` —— 6/10 个有
- `Getter` —— 6/10 个有
- `ImageConcanate` —— 6/10 个有
- `Setter` —— 6/10 个有
- `SoundFlow_GetLength` —— 6/10 个有
- `easy cleanGpuUsed` —— 6/10 个有
- `CR Text` —— 5/10 个有
- `GetImageSizeAndCount` —— 4/10 个有
- `ImageFromBatch+` —— 4/10 个有
- `Audio Duration (mtb)` —— 3/10 个有
- `WanVideoTorchCompileSettings` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `PreviewAudio` —— 2/10 个有
- `ImageResize+` —— 1/10 个有
- `ImpactInt` —— 1/10 个有
- `IndexTTS2Run` —— 1/10 个有
- `Int` —— 1/10 个有
- `JWFloat` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `TwoWaySwitch` —— 1/10 个有
- `VHS_VideoInfo` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
