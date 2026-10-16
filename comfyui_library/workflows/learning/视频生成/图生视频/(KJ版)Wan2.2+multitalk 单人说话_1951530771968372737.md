---
key: 视频生成/图生视频/(KJ版)Wan2.2+multitalk 单人说话_1951530771968372737.json
name: (KJ版)Wan2.2+multitalk 单人说话_1951530771968372737.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1951530771968372737.json
hash: 5d8fe0f6dddebc84
coverage: 0.913043
learned_at: 2026-10-15 22:30:58
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, GetImageSizeAndCount, CreateCFGScheduleFloatList, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, Note, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, MultiTalkModelLoader, WanVideoClipVisionEncode, CLIPVisionLoader, INTConstant, INTConstant, DownloadAndLoadWav2VecModel, SaveLatent, WanVideoVAELoader, WanVideoSampler, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, AudioCrop, AudioSeparation, LoadImage, WanVideoImageToVideoEncode, MultiTalkWav2VecEmbeds, CR Prompt Text, PreviewAudio, LoadAudio, easy seed, JWInteger, Note, WanVideoTorchCompileSettings, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, MathExpression|pysssss, Int, Note, CR Integer To String]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版)Wan2.2+multitalk 单人说话_1951530771968372737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951530771968372737.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MultiTalkModelLoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `INTConstant`
- `INTConstant`
- `DownloadAndLoadWav2VecModel`
- `SaveLatent`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `AudioCrop`
- `AudioSeparation`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `MultiTalkWav2VecEmbeds`
- `CR Prompt Text`
- `PreviewAudio`
- `LoadAudio`
- `easy seed`
- `JWInteger`
- `Note`
- `WanVideoTorchCompileSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `Int`
- `Note`
- `CR Integer To String`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTextEncode`、`MultiTalkModelLoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`INTConstant`、`DownloadAndLoadWav2VecModel`、`SaveLatent`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoLoraSelect`、`AudioCrop`、`AudioSeparation`、`LoadImage`、`WanVideoImageToVideoEncode`、`MultiTalkWav2VecEmbeds`、`CR Prompt Text`、`PreviewAudio`、`LoadAudio`、`easy seed`、`JWInteger`、`WanVideoTorchCompileSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`MathExpression|pysssss`、`Int`、`CR Integer To String`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、SaveLatent、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
