---
name: unknown_workflow_video_lora_sampler_358
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7225
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, ImageResizeKJv2, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_GetAudioDuration, SaveAudio, SetNode, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1959861917236015105.json, 视频生成/图生视频/1959926509467283458.json, 视频生成/图生视频/1995653735567261698.json, 视频生成/图生视频/1983895730928713729.json, 视频生成/图生视频/1964183198169186306.json, 视频生成/图生视频/1966856780053614593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_358

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1959861917236015105.json、视频生成/图生视频/1959926509467283458.json、视频生成/图生视频/1995653735567261698.json、视频生成/图生视频/1983895730928713729.json、视频生成/图生视频/1964183198169186306.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RH_GetAudioDuration`
- `SaveAudio`
- `SetNode`
- `SimpleMath+`
- `ToInt`
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
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `INTConstant` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `Anything Everywhere` —— 3/6 个有
- `Int` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `Primitive string multiline [Crystools]` —— 3/6 个有
- `SeargeIntegerConstant` —— 3/6 个有
- `SimpleCondition+` —— 3/6 个有
- `VHS_LoadVideoFFmpeg` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `easy clearCacheAll` —— 3/6 个有
- `CM_IntToFloat` —— 1/6 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/6 个有
- `FantasyPortraitFaceDetector` —— 1/6 个有
- `FantasyPortraitModelLoader` —— 1/6 个有
- `GIMMVFI_interpolate` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `WanVideoAddFantasyPortrait` —— 1/6 个有
- `WanVideoEncode` —— 1/6 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/6 个有
- `WanVideoUni3C_embeds` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
