---
key: 视频生成/图生视频/✅wan2.1 Infinite Talk-图片对口型_固定机位-图生视频，口播数字人_1964014354544869377.json
name: ✅wan2.1 Infinite Talk-图片对口型_固定机位-图生视频，口播数字人_1964014354544869377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964014354544869377.json
hash: f7ae06b82894971a
coverage: 0.586207
learned_at: 2026-10-15 22:31:34
nodes: [SetNode, SetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, SetNode, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, WanVideoVAELoader, GetNode, SetNode, SetNode, SetNode, GetNode, JWInteger, JWInteger, SetNode, ImageResizeKJv2, MultiTalkSilentEmbeds, GetImageSize, SetNode, IndexTTS2Run, CR Prompt Text, LoadAudio, SetNode, SaveAudio, AudioSeparation, Audio To Text (mtb), Load Whisper (mtb), easy showAnything, LoadAudio, CR Prompt Text, SetNode, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, PrimitiveNode, WanVideoDecode, GetNode, SetNode, GetNode, SetNode, LoadAudio, LoadAudio, GetNode, WanVideoTextEncode, WanVideoImageToVideoMultiTalk, SetNode, Note, ImpactSwitch, VHS_LoadVideo, GetNode, GetNode, MultiTalkModelLoader, MultiTalkModelLoader, WanVideoModelLoader, LoadImage, PreviewAudio, AudioBeforeAfterSilence, SetNode, SetNode, AudioSeparation, GetNode, AudioCrop, Bjornulf_ShowInt, MultiTalkWav2VecEmbeds, Bjornulf_ShowInt, GetNode, SetNode, SimpleMath+, ToInt, SoundFlow_GetLength, Bjornulf_ShowInt, WanVideoSampler, GetNode, ImageConcanate, VHS_VideoCombine, GetNode, GetNode, GetNode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/✅wan2.1 Infinite Talk-图片对口型_固定机位-图生视频，口播数字人_1964014354544869377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964014354544869377.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（87 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `WanVideoVAELoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `ImageResizeKJv2`
- `MultiTalkSilentEmbeds`
- `GetImageSize`
- `SetNode`
- `IndexTTS2Run`
- `CR Prompt Text`
- `LoadAudio`
- `SetNode`
- `SaveAudio`
- `AudioSeparation`
- `Audio To Text (mtb)`
- `Load Whisper (mtb)`
- `easy showAnything`
- `LoadAudio`
- `CR Prompt Text`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LoadAudio`
- `LoadAudio`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoImageToVideoMultiTalk`
- `SetNode`
- `Note`
- `ImpactSwitch`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `MultiTalkModelLoader`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `PreviewAudio`
- `AudioBeforeAfterSilence`
- `SetNode`
- `SetNode`
- `AudioSeparation`
- `GetNode`
- `AudioCrop`
- `Bjornulf_ShowInt`
- `MultiTalkWav2VecEmbeds`
- `Bjornulf_ShowInt`
- `GetNode`
- `SetNode`
- `SimpleMath+`
- `ToInt`
- `SoundFlow_GetLength`
- `Bjornulf_ShowInt`
- `WanVideoSampler` ★核心
- `GetNode`
- `ImageConcanate`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`

## 知识

覆盖率 **59%**（51/87）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`WanVideoVAELoader`、`JWInteger`、`ImageResizeKJv2`、`MultiTalkSilentEmbeds`、`GetImageSize`、`IndexTTS2Run`、`CR Prompt Text`、`LoadAudio`、`SaveAudio`、`AudioSeparation`、`Audio To Text (mtb)`、`Load Whisper (mtb)`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`VHS_LoadVideo`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LoadImage`、`PreviewAudio`、`AudioBeforeAfterSilence`、`AudioCrop`、`Bjornulf_ShowInt`、`MultiTalkWav2VecEmbeds`、`SimpleMath+`、`ToInt`、`SoundFlow_GetLength`、`WanVideoSampler`、`ImageConcanate`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
