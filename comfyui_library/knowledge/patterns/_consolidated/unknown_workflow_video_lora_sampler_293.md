---
name: unknown_workflow_video_lora_sampler_293
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.770714
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, Float to Int, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk视频转数字人-动态更强更自然_2043528487876694017.json, 视频生成/图生视频/2015607180996644865.json, 视频生成/图生视频/1992841755221618690.json, 视频生成/图生视频/1998779897466249217.json, 视频生成/图生视频/1993207838587764737.json, 视频生成/图生视频/1964947566926417921.json, 视频生成/图生视频/1958149674144321538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_293

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/Infinitetalk视频转数字人-动态更强更自然_2043528487876694017.json、视频生成/图生视频/2015607180996644865.json、视频生成/图生视频/1992841755221618690.json、视频生成/图生视频/1998779897466249217.json、视频生成/图生视频/1993207838587764737.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `Float to Int`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `Int` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `SoundFlow_GetLength` —— 5/7 个有
- `LoadWanVideoT5TextEncoder` —— 4/7 个有
- `WanVideoTextEncode` —— 4/7 个有
- `WanVideoTextEncodeCached` —— 3/7 个有
- `GetImageRangeFromBatch` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `RH_GetAudioDuration` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `WanVideoEncode` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `Getter` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `SeparateMasks` —— 1/7 个有
- `Setter` —— 1/7 个有
- `WanVideoTorchCompileSettings` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
