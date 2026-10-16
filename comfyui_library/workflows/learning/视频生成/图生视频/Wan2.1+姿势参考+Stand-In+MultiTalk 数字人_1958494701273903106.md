---
key: 视频生成/图生视频/Wan2.1+姿势参考+Stand-In+MultiTalk 数字人_1958494701273903106.json
name: Wan2.1+姿势参考+Stand-In+MultiTalk 数字人_1958494701273903106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958494701273903106.json
hash: 5cd0ef693c04b846
coverage: 0.835821
learned_at: 2026-10-15 22:31:22
nodes: [WanVideoLoraSelect, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, MultiTalkModelLoader, LoadWanVideoT5TextEncoder, FaceProcessorLoader, LoadAudio, VHS_VideoCombine, VHS_VideoCombine, Reroute, WanVideoDecode, ImageConcanate, ImageConcanate, WanVideoVAELoader, WanVideoModelLoader, WanVideoVACEModelSelect, Wan22PromptSelector, Text Concatenate, RH_LLMAPI_NODE, ImpactSwitch, VHS_VideoInfo, Reroute, WanVideoVACEStartToEndFrame, ImageResizeKJv2, MathExpression|pysssss, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, JWIntegerToString, WanVideoSampler, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadImage, PrimitiveStringMultiline, ImageFromBatch+, WanVideoTextEncode, easy clearCacheAll, WanVideoVACEEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, ApplyFaceProcessor, WanVideoEncode, ImageResizeKJv2, Reroute, Reroute, InspyrenetRembg, LayerUtility: ImageRemoveAlpha, PreviewImage, WanVideoAddStandInLatent, easy cleanGpuUsed, easy clearCacheAll, JWIntegerToString, AudioCrop, AudioSeparation, DownloadAndLoadWav2VecModel, SaveAudio, MultiTalkWav2VecEmbeds, easy clearCacheAll, easy cleanGpuUsed, OpenposePreprocessor, ShowText|pysssss, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+姿势参考+Stand-In+MultiTalk 数字人_1958494701273903106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958494701273903106.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（67 个）：
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `MultiTalkModelLoader`
- `LoadWanVideoT5TextEncoder`
- `FaceProcessorLoader`
- `LoadAudio`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoDecode`
- `ImageConcanate`
- `ImageConcanate`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `Wan22PromptSelector`
- `Text Concatenate`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `VHS_VideoInfo`
- `Reroute`
- `WanVideoVACEStartToEndFrame`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `JWIntegerToString`
- `WanVideoSampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ImageFromBatch+`
- `WanVideoTextEncode`
- `easy clearCacheAll`
- `WanVideoVACEEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `ApplyFaceProcessor`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `Reroute`
- `Reroute`
- `InspyrenetRembg`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `WanVideoAddStandInLatent`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `JWIntegerToString`
- `AudioCrop`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `SaveAudio`
- `MultiTalkWav2VecEmbeds`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `OpenposePreprocessor`
- `ShowText|pysssss`
- `VHS_LoadVideo`

## 知识

覆盖率 **84%**（56/67）

**有卡**：`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`MultiTalkModelLoader`、`LoadWanVideoT5TextEncoder`、`FaceProcessorLoader`、`LoadAudio`、`VHS_VideoCombine`、`WanVideoDecode`、`ImageConcanate`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`Wan22PromptSelector`、`Text Concatenate`、`RH_LLMAPI_NODE`、`VHS_VideoInfo`、`WanVideoVACEStartToEndFrame`、`ImageResizeKJv2`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`JWIntegerToString`、`WanVideoSampler`、`LoadImage`、`ImageFromBatch+`、`WanVideoTextEncode`、`easy clearCacheAll`、`WanVideoVACEEncode`、`easy cleanGpuUsed`、`ApplyFaceProcessor`、`WanVideoEncode`、`InspyrenetRembg`、`LayerUtility: ImageRemoveAlpha`、`WanVideoAddStandInLatent`、`AudioCrop`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`SaveAudio`、`MultiTalkWav2VecEmbeds`、`OpenposePreprocessor`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、OpenposePreprocessor、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
