---
name: unknown_workflow_video_lora_sampler_670
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.957333
common_nodes: [CR Text, DownloadAndLoadWav2VecModel, Float to Int, GetImageSizeAndCount, INTConstant, ImpactInt, IndexTTS2Run, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, RH_GetAudioDuration, SimpleMath+, Text, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1958161496469549058.json, 视频生成/图生视频/1966806156851154945.json, 视频生成/图生视频/1989260751770710018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_670

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1958161496469549058.json、视频生成/图生视频/1966806156851154945.json、视频生成/图生视频/1989260751770710018.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `Float to Int`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImpactInt`
- `IndexTTS2Run`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `RH_GetAudioDuration`
- `SimpleMath+`
- `Text`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `intToFloat _O` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
