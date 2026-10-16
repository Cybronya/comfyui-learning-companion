---
key: 视频生成/图生视频/IndexTTS2+InfiniteTalk图生数字人单人-B站UP主@好奇漫步!音频数字人同时生成_1983563401169444866.json
name: IndexTTS2+InfiniteTalk图生数字人单人-B站UP主@好奇漫步!音频数字人同时生成_1983563401169444866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1983563401169444866.json
hash: a444a1245c54a8b9
coverage: 0.769231
learned_at: 2026-10-15 22:32:45
nodes: [AudioCrop, WanVideoClipVisionEncode, WanVideoTorchCompileSettings, WanVideoBlockSwap, ToInt, MultiTalkWav2VecEmbeds, easy showAnything, Int, SimpleMath+, Audio Duration (mtb), LoadImage, WanVideoDecode, WanVideoSampler, WanVideoImageToVideoMultiTalk, LoadImage, VHS_VideoCombine, WanVideoTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, CR Text, PrimitiveFloat, IndexTTS2_Emotion, LoadAudio, AudioSeparation, SaveAudio, LoadAudio, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/IndexTTS2+InfiniteTalk图生数字人单人-B站UP主@好奇漫步!音频数字人同时生成_1983563401169444866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983563401169444866.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `AudioCrop`
- `WanVideoClipVisionEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `ToInt`
- `MultiTalkWav2VecEmbeds`
- `easy showAnything`
- `Int`
- `SimpleMath+`
- `Audio Duration (mtb)`
- `LoadImage`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `CR Text`
- `PrimitiveFloat`
- `IndexTTS2_Emotion`
- `LoadAudio`
- `AudioSeparation`
- `SaveAudio`
- `LoadAudio`
- `ImageResizeKJv2`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`AudioCrop`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`ToInt`、`MultiTalkWav2VecEmbeds`、`Int`、`SimpleMath+`、`Audio Duration (mtb)`、`LoadImage`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`VHS_VideoCombine`、`WanVideoTextEncode`、`CLIPVisionLoader`、`DownloadAndLoadWav2VecModel`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`CR Text`、`IndexTTS2_Emotion`、`LoadAudio`、`AudioSeparation`、`SaveAudio`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
