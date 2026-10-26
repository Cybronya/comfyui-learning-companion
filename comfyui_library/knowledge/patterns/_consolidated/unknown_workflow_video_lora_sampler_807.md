---
name: unknown_workflow_video_lora_sampler_807
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.639
common_nodes: [AIO_Preprocessor, ApplyFaceProcessor, AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, DWPreprocessor, DownloadAndLoadWav2VecModel, EsesImageEffectLevels, FaceProcessorLoader, FloatConstant, GetImageRangeFromBatch, GetNode, INTConstant, ImageBatchMulti, ImageBlend, ImageFromBatch, ImageResizeKJv2, LayerUtility: PurgeVRAM, LoadImage, MaskToImage, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, SaveAudioMP3, SetNode, VHS_GetImageCount, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy seed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/WAN-VACE+MultiTalk+Stand-In移动人物位置，添加自定义人物，同台演唱_1957556428611448834.json, 音频生成/音频生成/WAN-VACE+MultiTalk+Stand-In完美复刻舞蹈唱歌_1955906696134754305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_807

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/WAN-VACE+MultiTalk+Stand-In移动人物位置，添加自定义人物，同台演唱_1957556428611448834.json、音频生成/音频生成/WAN-VACE+MultiTalk+Stand-In完美复刻舞蹈唱歌_1955906696134754305.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFaceProcessor`
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
- `DownloadAndLoadWav2VecModel`
- `EsesImageEffectLevels`
- `FaceProcessorLoader`
- `FloatConstant`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageBlend`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `SaveAudioMP3`
- `SetNode`
- `VHS_GetImageCount`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEmbedBridge`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `Florence2toCoordinates` —— 1/2 个有
- `LayerMask: BBoxJoin` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance` —— 1/2 个有
- `LayerUtility: LaMa` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `Masks Combine Regions` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `PreviewAnimation` —— 1/2 个有
- `ProPainterInpaint` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `Sam2Segmentation` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `VHS_VideoInfoSource` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
