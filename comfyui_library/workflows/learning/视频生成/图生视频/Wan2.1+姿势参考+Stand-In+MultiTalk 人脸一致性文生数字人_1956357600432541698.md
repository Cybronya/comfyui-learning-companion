---
key: 视频生成/图生视频/Wan2.1+姿势参考+Stand-In+MultiTalk 人脸一致性文生数字人_1956357600432541698.json
name: Wan2.1+姿势参考+Stand-In+MultiTalk 人脸一致性文生数字人_1956357600432541698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956357600432541698.json
hash: 4ab7a7df021a02a6
coverage: 0.828125
learned_at: 2026-10-15 22:31:13
nodes: [Wan22PromptSelector, ImpactSwitch, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, JWInteger, Text Concatenate, RH_LLMAPI_NODE, easy imageScaleDownToSize, JWInteger, easy showAnything, FaceProcessorLoader, LayerUtility: ImageRemoveAlpha, PreviewImage, WanVideoTextEncode, GetNode, GetNode, AudioSeparation, GetNode, ImageConcatMulti, easy cleanGpuUsed, SetNode, SetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, WanVideoVACEModelSelect, CR Text, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, InspyrenetRembg, ApplyFaceProcessor, WanVideoEncode, SimpleMath+, WanVideoDecode, WanVideoAddStandInLatent, ImageConcatMulti, WanVideoVACEEncode, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, JWIntegerToString, AudioCrop, PreviewAudio, WanVideoVACEStartToEndFrame, ImageFromBatch+, VHS_VideoInfo, VHS_LoadVideo, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, OpenposePreprocessor, WanVideoSampler, WanVideoModelLoader, ImageResizeKJv2, PreviewImage, JWInteger, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+姿势参考+Stand-In+MultiTalk 人脸一致性文生数字人_1956357600432541698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956357600432541698.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（64 个）：
- `Wan22PromptSelector`
- `ImpactSwitch`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `JWInteger`
- `Text Concatenate`
- `RH_LLMAPI_NODE`
- `easy imageScaleDownToSize`
- `JWInteger`
- `easy showAnything`
- `FaceProcessorLoader`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `AudioSeparation`
- `GetNode`
- `ImageConcatMulti`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `WanVideoVACEModelSelect`
- `CR Text`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `InspyrenetRembg`
- `ApplyFaceProcessor`
- `WanVideoEncode`
- `SimpleMath+`
- `WanVideoDecode`
- `WanVideoAddStandInLatent`
- `ImageConcatMulti`
- `WanVideoVACEEncode`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `JWIntegerToString`
- `AudioCrop`
- `PreviewAudio`
- `WanVideoVACEStartToEndFrame`
- `ImageFromBatch+`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `OpenposePreprocessor`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `JWInteger`
- `WanVideoLoraSelect`

## 知识

覆盖率 **83%**（53/64）

**有卡**：`Wan22PromptSelector`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`JWInteger`、`Text Concatenate`、`RH_LLMAPI_NODE`、`easy imageScaleDownToSize`、`FaceProcessorLoader`、`LayerUtility: ImageRemoveAlpha`、`WanVideoTextEncode`、`AudioSeparation`、`ImageConcatMulti`、`easy cleanGpuUsed`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`MultiTalkModelLoader`、`WanVideoVACEModelSelect`、`CR Text`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`InspyrenetRembg`、`ApplyFaceProcessor`、`WanVideoEncode`、`SimpleMath+`、`WanVideoDecode`、`WanVideoAddStandInLatent`、`WanVideoVACEEncode`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`JWIntegerToString`、`AudioCrop`、`PreviewAudio`、`WanVideoVACEStartToEndFrame`、`ImageFromBatch+`、`VHS_VideoInfo`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoadImage`、`OpenposePreprocessor`、`WanVideoSampler`、`WanVideoModelLoader`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、OpenposePreprocessor、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
