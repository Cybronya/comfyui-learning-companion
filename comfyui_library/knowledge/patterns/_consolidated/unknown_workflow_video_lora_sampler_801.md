---
name: unknown_workflow_video_lora_sampler_801
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.927
common_nodes: [AudioCrop, CR Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, INTConstant, ImageFromBatch+, ImageResizeKJv2, Int, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, PreviewAudio, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader, easy getNode, easy setNode, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [数字人/数字人/KJ-wan2.2-infinitetalk双采-魔改_2040992271016923137.json, 数字人/数字人/邪修-（KJ）wan2.2-infinitetalk三采_2040715355902976002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_801

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/KJ-wan2.2-infinitetalk双采-魔改_2040992271016923137.json、数字人/数字人/邪修-（KJ）wan2.2-infinitetalk三采_2040715355902976002.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `PreviewAudio`
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
- `easy getNode`
- `easy setNode`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `Frames Concat Latent` —— 1/2 个有
- `Frames Slice Latent` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `StringToInt` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
