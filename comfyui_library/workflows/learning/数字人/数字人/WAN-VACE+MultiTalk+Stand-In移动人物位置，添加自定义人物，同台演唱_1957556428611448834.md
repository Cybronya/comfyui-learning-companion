---
key: 数字人/数字人/WAN-VACE+MultiTalk+Stand-In移动人物位置，添加自定义人物，同台演唱_1957556428611448834.json
name: WAN-VACE+MultiTalk+Stand-In移动人物位置，添加自定义人物，同台演唱_1957556428611448834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/WAN-VACE+MultiTalk+Stand-In移动人物位置，添加自定义人物，同台演唱_1957556428611448834.json
hash: c3a644c7644fd565
coverage: 0.666667
learned_at: 2026-10-26 01:57:39
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, VHS_GetImageCount, INTConstant, GetNode, GetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, ImageBatchMulti, GetNode, MathExpression|pysssss, GetNode, easy cleanGpuUsed, GetNode, easy cleanGpuUsed, SetNode, GetNode, WanVideoDecode, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, GetNode, GetNode, easy cleanGpuUsed, AudioSeparation, AudioCrop, DownloadAndLoadWav2VecModel, MaskToImage, SetNode, SetNode, MultiTalkWav2VecEmbeds, easy cleanGpuUsed, AudioSeparation, DownloadAndLoadWav2VecModel, MathExpression|pysssss, Reroute, MathExpression|pysssss, GetImageRangeFromBatch, WanVideoVACEStartToEndFrame, VHS_GetImageCount, MathExpression|pysssss, easy showAnything, VHS_GetImageCount, easy showAnything, easy showAnything, GetNode, ImageFromBatch, VHS_GetImageCount, easy showAnything, GetNode, LayerUtility: PurgeVRAM, WanVideoSampler, VHS_GetImageCount, easy showAnything, GetNode, GetNode, SetNode, GetNode, Reroute, GetNode, SetNode, GetNode, LayerUtility: PurgeVRAM, GetNode, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, easy cleanGpuUsed, WanVideoVACEEncode, WanVideoAddStandInLatent, WanVideoEnhanceAVideo, WanVideoSLG, easy cleanGpuUsed, WanVideoExperimentalArgs, WanVideoAddStandInLatent, INTConstant, FloatConstant, MathExpression|pysssss, MultiTalkWav2VecEmbeds, SetNode, CLIPLoader, WanVideoSampler, INTConstant, SetNode, INTConstant, MathExpression|pysssss, MathExpression|pysssss, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoTextEmbedBridge, WanVideoDecode, LayerUtility: PurgeVRAM, easy forLoopEnd, easy forLoopStart, LayerUtility: PurgeVRAM, ShowText|pysssss, GetNode, LayerUtility: PurgeVRAM, easy showAnything, GetNode, GetNode, ImageBlend, AIO_Preprocessor, DWPreprocessor, ImageResizeKJv2, GetNode, LayerUtility: PurgeVRAM, PreviewAnimation, Sam2Segmentation, PointsEditor, Masks Combine Regions, LayerMask: BBoxJoin, DownloadAndLoadFlorence2Model, easy cleanGpuUsed, easy cleanGpuUsed, ImageResizeKJv2, INTConstant, INTConstant, DownloadAndLoadSAM2Model, GetNode, ImageResizeKJv2, Note, WanVideoVAELoader, WanVideoEncode, GetNode, FaceProcessorLoader, Reroute, Reroute, GetNode, SaveAudioMP3, RMBG, easy cleanGpuUsed, ImageResizeKJv2, GetImageRangeFromBatch, RMBG, GetNode, GetNode, GetNode, GetNode, SetNode, easy cleanGpuUsed, GetImageRangeFromBatch, GetNode, VHS_VideoCombine, MaskToImage, easy cleanGpuUsed, easy cleanGpuUsed, SeedVR2BlockSwap, easy seed, VHS_VideoCombine, VHS_LoadVideo, SeedVR2, VHS_LoadVideo, DeepTranslatorTextNode, Florence2Run, PreviewAnimation, Florence2toCoordinates, PreviewAnimation, PreviewAnimation, WanVideoVACEEncode, VHS_VideoCombine, MaskToImage, SetNode, VHS_VideoCombine, SetNode, LoadImage, ApplyFaceProcessor, PreviewImage, VHS_VideoCombine, PreviewAnimation, LayerUtility: ImageBlendAdvance, LayerUtility: ImageBlendAdvance, VHS_VideoCombine, VHS_LoadAudioUpload, LoadAudio, Note, EsesImageEffectLevels, WanVideoBlockSwap, WanVideoTorchCompileSettings, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, CLIPTextEncode, CLIPTextEncode, ProPainterInpaint, easy cleanGpuUsed, LayerUtility: ImageBlendAdvance, Note, Note, LayerUtility: PurgeVRAM, LayerUtility: LaMa, LayerMask: MaskGrow, Note]
patterns: []
missing: []
---

# 数字人/数字人/WAN-VACE+MultiTalk+Stand-In移动人物位置，添加自定义人物，同台演唱_1957556428611448834.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/WAN-VACE+MultiTalk+Stand-In移动人物位置，添加自定义人物，同台演唱_1957556428611448834.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（210 个）：
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
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
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
- `Reroute`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `WanVideoVACEStartToEndFrame`
- `VHS_GetImageCount`
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
- `GetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `easy cleanGpuUsed`
- `WanVideoVACEEncode`
- `WanVideoAddStandInLatent`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `easy cleanGpuUsed`
- `WanVideoExperimentalArgs`
- `WanVideoAddStandInLatent`
- `INTConstant`
- `FloatConstant`
- `MathExpression|pysssss`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `CLIPLoader`
- `WanVideoSampler` ★核心
- `INTConstant`
- `SetNode`
- `INTConstant`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoTextEmbedBridge`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `easy forLoopEnd`
- `easy forLoopStart`
- `LayerUtility: PurgeVRAM`
- `ShowText|pysssss`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `ImageBlend`
- `AIO_Preprocessor`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `PreviewAnimation`
- `Sam2Segmentation`
- `PointsEditor`
- `Masks Combine Regions`
- `LayerMask: BBoxJoin`
- `DownloadAndLoadFlorence2Model`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `ImageResizeKJv2`
- `Note`
- `WanVideoVAELoader`
- `WanVideoEncode`
- `GetNode`
- `FaceProcessorLoader`
- `Reroute`
- `Reroute`
- `GetNode`
- `SaveAudioMP3`
- `RMBG`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `RMBG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `GetImageRangeFromBatch`
- `GetNode`
- `VHS_VideoCombine`
- `MaskToImage`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SeedVR2BlockSwap`
- `easy seed`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `SeedVR2`
- `VHS_LoadVideo`
- `DeepTranslatorTextNode`
- `Florence2Run`
- `PreviewAnimation`
- `Florence2toCoordinates`
- `PreviewAnimation`
- `PreviewAnimation`
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `MaskToImage`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `LoadImage`
- `ApplyFaceProcessor`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewAnimation`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageBlendAdvance`
- `VHS_VideoCombine`
- `VHS_LoadAudioUpload`
- `LoadAudio`
- `Note`
- `EsesImageEffectLevels`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ProPainterInpaint`
- `easy cleanGpuUsed`
- `LayerUtility: ImageBlendAdvance`
- `Note`
- `Note`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: LaMa`
- `LayerMask: MaskGrow`
- `Note`

## 知识

覆盖率 **67%**（140/210）

**有卡**：`VHS_GetImageCount`、`INTConstant`、`MathExpression|pysssss`、`ImageBatchMulti`、`easy cleanGpuUsed`、`WanVideoDecode`、`AudioSeparation`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`MaskToImage`、`MultiTalkWav2VecEmbeds`、`GetImageRangeFromBatch`、`WanVideoVACEStartToEndFrame`、`ImageFromBatch`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoVACEEncode`、`WanVideoAddStandInLatent`、`FloatConstant`、`CLIPLoader`、`WanVideoTextEmbedBridge`、`easy forLoopEnd`、`easy forLoopStart`、`ImageBlend`、`AIO_Preprocessor`、`DWPreprocessor`、`ImageResizeKJv2`、`PreviewAnimation`、`Sam2Segmentation`、`PointsEditor`、`Masks Combine Regions`、`LayerMask: BBoxJoin`、`DownloadAndLoadFlorence2Model`、`DownloadAndLoadSAM2Model`、`WanVideoVAELoader`、`WanVideoEncode`、`FaceProcessorLoader`、`SaveAudioMP3`、`RMBG`、`VHS_VideoCombine`、`SeedVR2BlockSwap`、`easy seed`、`VHS_LoadVideo`、`SeedVR2`、`DeepTranslatorTextNode`、`Florence2Run`、`Florence2toCoordinates`、`LoadImage`、`ApplyFaceProcessor`、`LayerUtility: ImageBlendAdvance`、`VHS_LoadAudioUpload`、`LoadAudio`、`EsesImageEffectLevels`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CLIPTextEncode`、`ProPainterInpaint`、`LayerUtility: LaMa`、`LayerMask: MaskGrow`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、SeedVR2、SeedVR2BlockSwap、WanVideoSampler、easy seed、WanVideoDecode
