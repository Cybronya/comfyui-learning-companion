---
key: 音频生成/音频生成/WAN-VACE+MultiTalk+Stand-In完美复刻舞蹈唱歌_1955906696134754305.json
name: WAN-VACE+MultiTalk+Stand-In完美复刻舞蹈唱歌_1955906696134754305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/WAN-VACE+MultiTalk+Stand-In完美复刻舞蹈唱歌_1955906696134754305.json
hash: 1eac801b44d18f33
coverage: 0.610778
learned_at: 2026-10-18 01:24:02
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, VHS_GetImageCount, INTConstant, GetNode, easy imageRemBg, GetNode, GetNode, GetNode, GetNode, Reroute, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, ImageBatchMulti, VHS_VideoInfoSource, easy showAnything, GetNode, MathExpression|pysssss, GetNode, easy cleanGpuUsed, GetNode, easy cleanGpuUsed, CLIPTextEncode, SetNode, GetNode, WanVideoDecode, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, GetNode, GetNode, GetNode, easy cleanGpuUsed, AudioSeparation, AudioCrop, DownloadAndLoadWav2VecModel, MaskToImage, SetNode, SetNode, MultiTalkWav2VecEmbeds, easy cleanGpuUsed, AudioSeparation, DownloadAndLoadWav2VecModel, MathExpression|pysssss, GetImageRangeFromBatch, Reroute, MathExpression|pysssss, GetImageRangeFromBatch, WanVideoVACEStartToEndFrame, VHS_GetImageCount, easy forLoopStart, MathExpression|pysssss, easy showAnything, VHS_GetImageCount, easy showAnything, easy showAnything, GetNode, ImageFromBatch, VHS_GetImageCount, easy showAnything, GetNode, LayerUtility: PurgeVRAM, WanVideoSampler, VHS_GetImageCount, easy showAnything, GetNode, GetNode, SetNode, GetNode, Reroute, Reroute, LayerUtility: PurgeVRAM, GetNode, easy showAnything, GetNode, SetNode, GetNode, LayerUtility: PurgeVRAM, ImageResizeKJv2, GetNode, GetNode, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, easy cleanGpuUsed, WanVideoVACEEncode, WanVideoAddStandInLatent, easy forLoopEnd, ImageBlend, FaceProcessorLoader, GetNode, LayerUtility: PurgeVRAM, SetNode, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoBlockSwap, SetNode, VHS_VideoCombine, easy cleanGpuUsed, GetImageRangeFromBatch, WanVideoEnhanceAVideo, WanVideoSLG, easy cleanGpuUsed, WanVideoExperimentalArgs, WanVideoVACEEncode, WanVideoAddStandInLatent, PreviewImage, INTConstant, INTConstant, INTConstant, FloatConstant, MathExpression|pysssss, SaveAudioMP3, DWPreprocessor, CLIPTextEncode, DepthAnythingV2Preprocessor, MultiTalkWav2VecEmbeds, AIO_Preprocessor, WanVideoVAELoader, WanVideoLoraSelect, MultiTalkModelLoader, SetNode, GetNode, VHS_LoadAudioUpload, CLIPLoader, WanVideoLoraSelect, WanVideoSampler, INTConstant, WanVideoModelLoader, SetNode, INTConstant, Note, Note, VHS_VideoCombine, WanVideoEncode, EsesImageEffectLevels, MathExpression|pysssss, MathExpression|pysssss, Note, ApplyFaceProcessor, SetNode, GetNode, GetNode, VHS_LoadVideo, easy seed, VHS_VideoCombine, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoTextEmbedBridge, Note, WanVideoDecode, LayerUtility: PurgeVRAM, LoadImage, ImageResizeKJv2]
patterns: []
missing: []
---

# 音频生成/音频生成/WAN-VACE+MultiTalk+Stand-In完美复刻舞蹈唱歌_1955906696134754305.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/WAN-VACE+MultiTalk+Stand-In完美复刻舞蹈唱歌_1955906696134754305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（167 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `VHS_GetImageCount`
- `INTConstant`
- `GetNode`
- `easy imageRemBg`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `VHS_VideoInfoSource`
- `easy showAnything`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `AudioSeparation`
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `MaskToImage`
- `SetNode`
- `SetNode`
- `MultiTalkWav2VecEmbeds`
- `easy cleanGpuUsed`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `Reroute`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `WanVideoVACEStartToEndFrame`
- `VHS_GetImageCount`
- `easy forLoopStart`
- `MathExpression|pysssss`
- `easy showAnything`
- `VHS_GetImageCount`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `ImageFromBatch`
- `VHS_GetImageCount`
- `easy showAnything`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `VHS_GetImageCount`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `easy cleanGpuUsed`
- `WanVideoVACEEncode`
- `WanVideoAddStandInLatent`
- `easy forLoopEnd`
- `ImageBlend`
- `FaceProcessorLoader`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `GetImageRangeFromBatch`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `easy cleanGpuUsed`
- `WanVideoExperimentalArgs`
- `WanVideoVACEEncode`
- `WanVideoAddStandInLatent`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `FloatConstant`
- `MathExpression|pysssss`
- `SaveAudioMP3`
- `DWPreprocessor`
- `CLIPTextEncode` ★核心
- `DepthAnythingV2Preprocessor`
- `MultiTalkWav2VecEmbeds`
- `AIO_Preprocessor`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `SetNode`
- `GetNode`
- `VHS_LoadAudioUpload`
- `CLIPLoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoModelLoader`
- `SetNode`
- `INTConstant`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `EsesImageEffectLevels`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Note`
- `ApplyFaceProcessor`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `easy seed`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoTextEmbedBridge`
- `Note`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ImageResizeKJv2`

## 知识

覆盖率 **61%**（102/167）

**有卡**：`VHS_GetImageCount`、`INTConstant`、`easy imageRemBg`、`MathExpression|pysssss`、`ImageBatchMulti`、`VHS_VideoInfoSource`、`easy cleanGpuUsed`、`CLIPTextEncode`、`WanVideoDecode`、`AudioSeparation`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`MaskToImage`、`MultiTalkWav2VecEmbeds`、`GetImageRangeFromBatch`、`WanVideoVACEStartToEndFrame`、`easy forLoopStart`、`ImageFromBatch`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`ImageResizeKJv2`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoVACEEncode`、`WanVideoAddStandInLatent`、`easy forLoopEnd`、`ImageBlend`、`FaceProcessorLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`FloatConstant`、`SaveAudioMP3`、`DWPreprocessor`、`DepthAnythingV2Preprocessor`、`AIO_Preprocessor`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`VHS_LoadAudioUpload`、`CLIPLoader`、`WanVideoModelLoader`、`WanVideoEncode`、`EsesImageEffectLevels`、`ApplyFaceProcessor`、`VHS_LoadVideo`、`easy seed`、`WanVideoTextEmbedBridge`、`LoadImage`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、DepthAnythingV2Preprocessor、WanVideoSampler、easy seed、WanVideoDecode、WanVideoVAELoader
