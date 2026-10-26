---
key: 数字人/数字人/KJ-wan2.2-infinitetalk双采-魔改_2040992271016923137.json
name: KJ-wan2.2-infinitetalk双采-魔改_2040992271016923137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/KJ-wan2.2-infinitetalk双采-魔改_2040992271016923137.json
hash: 6768a0af83dc1d3d
coverage: 0.921053
learned_at: 2026-10-26 01:55:35
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoImageToVideoEncode, GetImageSizeAndCount, easy showAnything, ImageFromBatch+, WanVideoVAELoader, WanVideoTextEncodeSingle, easy setNode, easy setNode, LoadWanVideoT5TextEncoder, easy setNode, easy setNode, VHS_VideoCombine, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, WanVideoApplyNAG, easy getNode, WanVideoTextEncodeSingle, WanVideoDecode, easy setNode, easy setNode, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, MelBandRoFormerModelLoader, easy setNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, llama_cpp_model_loader, easy getNode, easy getNode, easy setNode, ImageResizeKJv2, MelBandRoFormerSampler, Reroute, Reroute, MultiTalkModelLoader, LayerUtility: PurgeVRAM V2, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM V2, Int, Int, easy showAnything, PreviewAudio, CR Text, easy getNode, LoadImage, LoadAudio, AudioCrop, CR Text, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoImageToVideoEncode, PreviewAny, INTConstant, WanVideoSampler, WanVideoSampler, INTConstant, WanVideoContextOptions, MarkdownNote]
patterns: []
missing: []
---

# 数字人/数字人/KJ-wan2.2-infinitetalk双采-魔改_2040992271016923137.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/KJ-wan2.2-infinitetalk双采-魔改_2040992271016923137.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（76 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `GetImageSizeAndCount`
- `easy showAnything`
- `ImageFromBatch+`
- `WanVideoVAELoader`
- `WanVideoTextEncodeSingle`
- `easy setNode`
- `easy setNode`
- `LoadWanVideoT5TextEncoder`
- `easy setNode`
- `easy setNode`
- `VHS_VideoCombine`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `WanVideoApplyNAG`
- `easy getNode`
- `WanVideoTextEncodeSingle`
- `WanVideoDecode`
- `easy setNode`
- `easy setNode`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `MelBandRoFormerModelLoader`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `llama_cpp_model_loader`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `ImageResizeKJv2`
- `MelBandRoFormerSampler` ★核心
- `Reroute`
- `Reroute`
- `MultiTalkModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `Int`
- `easy showAnything`
- `PreviewAudio`
- `CR Text`
- `easy getNode`
- `LoadImage`
- `LoadAudio`
- `AudioCrop`
- `CR Text`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `PreviewAny`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoContextOptions`
- `MarkdownNote`

## 知识

覆盖率 **92%**（70/76）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`ImageFromBatch+`、`WanVideoVAELoader`、`WanVideoTextEncodeSingle`、`easy setNode`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`easy getNode`、`WanVideoApplyNAG`、`WanVideoDecode`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`MelBandRoFormerModelLoader`、`llama_cpp_model_loader`、`ImageResizeKJv2`、`MelBandRoFormerSampler`、`MultiTalkModelLoader`、`LayerUtility: PurgeVRAM V2`、`llama_cpp_instruct_adv`、`Int`、`PreviewAudio`、`CR Text`、`LoadImage`、`LoadAudio`、`AudioCrop`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`INTConstant`、`WanVideoSampler`、`WanVideoContextOptions`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
