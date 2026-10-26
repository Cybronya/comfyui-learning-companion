---
key: 数字人/数字人/邪修-（KJ）wan2.2-infinitetalk三采_2040715355902976002.json
name: 邪修-（KJ）wan2.2-infinitetalk三采_2040715355902976002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/邪修-（KJ）wan2.2-infinitetalk三采_2040715355902976002.json
hash: 48814dfbc9c525a7
coverage: 0.933333
learned_at: 2026-10-26 02:05:50
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoVAELoader, WanVideoTextEncodeSingle, easy setNode, easy setNode, LoadWanVideoT5TextEncoder, easy setNode, easy setNode, VHS_VideoCombine, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, WanVideoApplyNAG, easy setNode, easy setNode, PreviewAny, DownloadAndLoadWav2VecModel, MelBandRoFormerModelLoader, easy setNode, easy getNode, easy getNode, easy setNode, easy setNode, llama_cpp_model_loader, easy getNode, easy getNode, easy setNode, ImageResizeKJv2, MelBandRoFormerSampler, MultiTalkModelLoader, LayerUtility: PurgeVRAM V2, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM V2, Int, Int, easy showAnything, PreviewAudio, WanVideoModelLoader, easy setNode, easy getNode, ImageFromBatch+, easy getNode, MultiTalkWav2VecEmbeds, INTConstant, easy getNode, easy getNode, easy getNode, LoadImage, CR Text, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoDecode, ImageFromBatch+, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoImageToVideoEncode, Frames Slice Latent, Frames Slice Latent, Frames Concat Latent, WanVideoSampler, WanVideoDecode, easy showAnything, SimpleMath+, StringToInt, easy showAnything, SimpleMath+, SimpleMath+, SimpleMath+, Reroute, Reroute, easy seed, INTConstant, WanVideoLoraSelect, CR Text, LoadAudio, AudioCrop, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTextEncodeSingle]
patterns: []
missing: []
---

# 数字人/数字人/邪修-（KJ）wan2.2-infinitetalk三采_2040715355902976002.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/邪修-（KJ）wan2.2-infinitetalk三采_2040715355902976002.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（90 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
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
- `WanVideoApplyNAG`
- `easy setNode`
- `easy setNode`
- `PreviewAny`
- `DownloadAndLoadWav2VecModel`
- `MelBandRoFormerModelLoader`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `llama_cpp_model_loader`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `ImageResizeKJv2`
- `MelBandRoFormerSampler` ★核心
- `MultiTalkModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `Int`
- `easy showAnything`
- `PreviewAudio`
- `WanVideoModelLoader`
- `easy setNode`
- `easy getNode`
- `ImageFromBatch+`
- `easy getNode`
- `MultiTalkWav2VecEmbeds`
- `INTConstant`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `LoadImage`
- `CR Text`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `ImageFromBatch+`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `Frames Slice Latent`
- `Frames Slice Latent`
- `Frames Concat Latent`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `easy showAnything`
- `SimpleMath+`
- `StringToInt`
- `easy showAnything`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `Reroute`
- `Reroute`
- `easy seed`
- `INTConstant`
- `WanVideoLoraSelect`
- `CR Text`
- `LoadAudio`
- `AudioCrop`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTextEncodeSingle`

## 知识

覆盖率 **93%**（84/90）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoTextEncodeSingle`、`easy setNode`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`easy getNode`、`WanVideoApplyNAG`、`DownloadAndLoadWav2VecModel`、`MelBandRoFormerModelLoader`、`llama_cpp_model_loader`、`ImageResizeKJv2`、`MelBandRoFormerSampler`、`MultiTalkModelLoader`、`LayerUtility: PurgeVRAM V2`、`llama_cpp_instruct_adv`、`Int`、`PreviewAudio`、`WanVideoModelLoader`、`ImageFromBatch+`、`MultiTalkWav2VecEmbeds`、`INTConstant`、`LoadImage`、`CR Text`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`WanVideoSampler`、`Frames Slice Latent`、`Frames Concat Latent`、`SimpleMath+`、`StringToInt`、`easy seed`、`LoadAudio`、`AudioCrop`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
