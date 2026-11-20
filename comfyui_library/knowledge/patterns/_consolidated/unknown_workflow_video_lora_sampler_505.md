---
name: unknown_workflow_video_lora_sampler_505
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.918333
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/【AI代码侠土豆】V2V-Infinitetalk视频转数字人_1990280525246066689.json, 数字人/数字人/数字人-视频对口型-完美复刻动作，保持原视频动作一致_1988076238738796546.json, 数字人/数字人/🍐Infinitetalk视频转数字人🍐_2017760163519799298.json, 视频生成/图生视频/InfiniteTalk数字人 _ 视频生视频-自动对口型（支持唱歌_说话）高动态_1992841755221618690.json, 视频生成/图生视频/Infinitetalk视频转数字人-动态更强更自然_2114345766474051586.json, 视频生成/图生视频/Infinitetalk视频转数字人｜动态更强更自然的图生视频方案_2114631993609773057.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_505

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/【AI代码侠土豆】V2V-Infinitetalk视频转数字人_1990280525246066689.json、数字人/数字人/数字人-视频对口型-完美复刻动作，保持原视频动作一致_1988076238738796546.json、数字人/数字人/🍐Infinitetalk视频转数字人🍐_2017760163519799298.json、视频生成/图生视频/InfiniteTalk数字人 _ 视频生视频-自动对口型（支持唱歌_说话）高动态_1992841755221618690.json、视频生成/图生视频/Infinitetalk视频转数字人-动态更强更自然_2114345766474051586.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
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
- `Float to Int` —— 5/6 个有
- `SoundFlow_GetLength` —— 5/6 个有
- `Getter` —— 4/6 个有
- `ImageConcanate` —— 4/6 个有
- `Setter` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `PrimitiveInt` —— 2/6 个有
- `CM_FloatToInt` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `Int` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `Switch any [Crystools]` —— 1/6 个有
- `VHS_VideoInfoSource` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
