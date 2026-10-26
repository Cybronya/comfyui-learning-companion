---
key: 数字人/数字人/邪修-wan2.2-infinitetalk-三采动态加强版_2015606744763867137.json
name: 邪修-wan2.2-infinitetalk-三采动态加强版_2015606744763867137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/邪修-wan2.2-infinitetalk-三采动态加强版_2015606744763867137.json
hash: ffb679745dd43bca
coverage: 0.859375
learned_at: 2026-10-26 02:05:49
nodes: [DownloadAndLoadWav2VecModel, MelBandRoFormerModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, WanVideoTextEncodeSingle, INTConstant, INTConstant, easy showAnything, StringToInt, WanVideoImageToVideoEncode, Int, Int, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoVAELoader, ImageResizeKJv2, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM V2, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoApplyNAG, WanVideoTextEncodeSingle, Any Switch (rgthree), easy showAnything, RH_LLMAPI_NODE, CR Text, CR Text, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), RHHiddenNodes, LoadAudio, ImageFromBatch+, WanVideoDecode, SimpleMath+, SimpleMath+, WanVideoSampler, VHS_VideoCombine, MelBandRoFormerSampler, AudioCrop, LoadImage, RunningHub Deepcleaner, LayerUtility: PurgeVRAM V2, Frames Concat Latent, WanVideoSampler, Frames Slice Latent, Frames Slice Latent, ImageFromBatch+, AudioToFPS, WanVideoImageToVideoEncode, SimpleMath+, SimpleMath+, easy showAnything, RHHiddenNodes, WanVideoDecode, GetImageSizeAndCount, MarkdownNote, easy seed, CR Text, Fast Groups Bypasser (rgthree), MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# 数字人/数字人/邪修-wan2.2-infinitetalk-三采动态加强版_2015606744763867137.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/邪修-wan2.2-infinitetalk-三采动态加强版_2015606744763867137.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（64 个）：
- `DownloadAndLoadWav2VecModel`
- `MelBandRoFormerModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `WanVideoTextEncodeSingle`
- `INTConstant`
- `INTConstant`
- `easy showAnything`
- `StringToInt`
- `WanVideoImageToVideoEncode`
- `Int`
- `Int`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `Any Switch (rgthree)`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `CR Text`
- `CR Text`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `RHHiddenNodes`
- `LoadAudio`
- `ImageFromBatch+`
- `WanVideoDecode`
- `SimpleMath+`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `MelBandRoFormerSampler` ★核心
- `AudioCrop`
- `LoadImage`
- `RunningHub Deepcleaner`
- `LayerUtility: PurgeVRAM V2`
- `Frames Concat Latent`
- `WanVideoSampler` ★核心
- `Frames Slice Latent`
- `Frames Slice Latent`
- `ImageFromBatch+`
- `AudioToFPS`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `SimpleMath+`
- `easy showAnything`
- `RHHiddenNodes`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `MarkdownNote`
- `easy seed`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **86%**（55/64）

**有卡**：`DownloadAndLoadWav2VecModel`、`MelBandRoFormerModelLoader`、`MultiTalkWav2VecEmbeds`、`WanVideoTextEncodeSingle`、`INTConstant`、`StringToInt`、`WanVideoImageToVideoEncode`、`Int`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`ImageResizeKJv2`、`LoadWanVideoT5TextEncoder`、`LayerUtility: PurgeVRAM V2`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoApplyNAG`、`RH_LLMAPI_NODE`、`CR Text`、`Mute / Bypass Relay (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`RHHiddenNodes`、`LoadAudio`、`ImageFromBatch+`、`WanVideoDecode`、`SimpleMath+`、`WanVideoSampler`、`VHS_VideoCombine`、`MelBandRoFormerSampler`、`AudioCrop`、`LoadImage`、`RunningHub Deepcleaner`、`Frames Concat Latent`、`Frames Slice Latent`、`AudioToFPS`、`GetImageSizeAndCount`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
