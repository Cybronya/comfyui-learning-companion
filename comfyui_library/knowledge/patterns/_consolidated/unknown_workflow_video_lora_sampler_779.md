---
name: unknown_workflow_video_lora_sampler_779
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.892
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadGIMMVFIModel, DownloadAndLoadWav2VecModel, GIMMVFI_interpolate, JWInteger, JWIntegerToString, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveFloat, SimpleMath+, TextInput_, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1938175701055115265.json, 视频生成/图生视频/1937534979532591106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_779

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1938175701055115265.json、视频生成/图生视频/1937534979532591106.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadGIMMVFIModel`
- `DownloadAndLoadWav2VecModel`
- `GIMMVFI_interpolate`
- `JWInteger`
- `JWIntegerToString`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveFloat`
- `SimpleMath+`
- `TextInput_`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetTextFromJson` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `LoadJsonFromText` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `ReplaceText` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `SongGeneration_Sampler` —— 1/2 个有
- `SongGeneration_Stage1` —— 1/2 个有
- `SongGeneration_Stage2` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
