---
name: unknown_workflow_video_lora_sampler_685
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.659
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, ImageResizeKJv2, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, Primitive string multiline [Crystools], RH_GetAudioDuration, SaveAudio, SeargeIntegerConstant, SetNode, SimpleCondition+, SimpleMath+, ToInt, VHS_LoadVideoFFmpeg, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk单人图片数字人 无限时长_1959861917236015105.json, 视频生成/图生视频/InfiniteTalk单人视频驱动数字人_1959926509467283458.json, 视频生成/图生视频/多人版InfiniteTalk高质量数字人_1964183198169186306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_685

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk单人图片数字人 无限时长_1959861917236015105.json、视频生成/图生视频/InfiniteTalk单人视频驱动数字人_1959926509467283458.json、视频生成/图生视频/多人版InfiniteTalk高质量数字人_1964183198169186306.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `Primitive string multiline [Crystools]`
- `RH_GetAudioDuration`
- `SaveAudio`
- `SeargeIntegerConstant`
- `SetNode`
- `SimpleCondition+`
- `SimpleMath+`
- `ToInt`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/3 个有
- `FantasyPortraitFaceDetector` —— 1/3 个有
- `FantasyPortraitModelLoader` —— 1/3 个有
- `GIMMVFI_interpolate` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `WanVideoAddFantasyPortrait` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/3 个有
- `WanVideoUni3C_embeds` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
