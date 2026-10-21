---
name: unknown_workflow_video_lora_sampler_902
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.908
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CreateCFGScheduleFloatList, DF_Int_to_Float, DownloadAndLoadWav2VecModel, FL_FloatToInt, GetNode, INTConstant, ImageResize+, JWInteger, JjkText, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_GetAudioDuration, SetNode, SimpleMath+, Text, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy convertAnything, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/2058173593900638210.json, 视频生成/图生视频/2058418858171658242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_902

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2058173593900638210.json、视频生成/图生视频/2058418858171658242.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CreateCFGScheduleFloatList`
- `DF_Int_to_Float`
- `DownloadAndLoadWav2VecModel`
- `FL_FloatToInt`
- `GetNode`
- `INTConstant`
- `ImageResize+`
- `JWInteger`
- `JjkText`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RH_GetAudioDuration`
- `SetNode`
- `SimpleMath+`
- `Text`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
