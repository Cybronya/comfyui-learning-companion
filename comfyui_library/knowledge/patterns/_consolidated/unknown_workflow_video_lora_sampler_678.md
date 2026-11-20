---
name: unknown_workflow_video_lora_sampler_678
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.629
common_nodes: [AIO_Preprocessor, ApplyFaceProcessor, CLIPLoader, CLIPTextEncode, DWPreprocessor, EsesImageEffectLevels, FaceProcessorLoader, FloatConstant, GetImageRangeFromBatch, GetNode, INTConstant, ImageBatchMulti, ImageBlend, ImageFromBatch, ImageResizeKJv2, LayerUtility: PurgeVRAM, LoadImage, MaskToImage, MathExpression|pysssss, MultiTalkModelLoader, PreviewImage, SetNode, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy seed, easy showAnything]
problems: []
missing: []
members: [平台全量/WAN-VACE人物位置调整，指定位置添加自定义人物搭配STAND IN完美复刻人物和动作_1957126901270548481.json, 平台全量/WAN-VACE指定替换视频人物，搭配STAND IN完美复刻动作，还原人物_1956871832618065921.json, 数字人/数字人/WAN-VACE+MultiTalk+Stand-In移动人物位置，添加自定义人物，同台演唱_1957556428611448834.json, 音频生成/音频生成/WAN-VACE+MultiTalk+Stand-In完美复刻舞蹈唱歌_1955906696134754305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_678

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/WAN-VACE人物位置调整，指定位置添加自定义人物搭配STAND IN完美复刻人物和动作_1957126901270548481.json、平台全量/WAN-VACE指定替换视频人物，搭配STAND IN完美复刻动作，还原人物_1956871832618065921.json、数字人/数字人/WAN-VACE+MultiTalk+Stand-In移动人物位置，添加自定义人物，同台演唱_1957556428611448834.json、音频生成/音频生成/WAN-VACE+MultiTalk+Stand-In完美复刻舞蹈唱歌_1955906696134754305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFaceProcessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
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
- `PreviewImage`
- `SetNode`
- `VHS_GetImageCount`
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
- `DeepTranslatorTextNode` —— 3/4 个有
- `DownloadAndLoadFlorence2Model` —— 3/4 个有
- `DownloadAndLoadSAM2Model` —— 3/4 个有
- `Florence2Run` —— 3/4 个有
- `Florence2toCoordinates` —— 3/4 个有
- `LayerMask: MaskGrow` —— 3/4 个有
- `LayerUtility: ImageBlendAdvance` —— 3/4 个有
- `PointsEditor` —— 3/4 个有
- `PreviewAnimation` —— 3/4 个有
- `RMBG` —— 3/4 个有
- `Sam2Segmentation` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `AudioSeparation` —— 2/4 个有
- `DownloadAndLoadWav2VecModel` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LayerMask: BBoxJoin` —— 2/4 个有
- `LayerUtility: LaMa` —— 2/4 个有
- `Masks Combine Regions` —— 2/4 个有
- `MultiTalkWav2VecEmbeds` —— 2/4 个有
- `ProPainterInpaint` —— 2/4 个有
- `SaveAudioMP3` —— 2/4 个有
- `SeedVR2` —— 2/4 个有
- `SeedVR2BlockSwap` —— 2/4 个有
- `VHS_LoadAudioUpload` —— 2/4 个有
- `WanVideoEasyCache` —— 2/4 个有
- `DepthAnythingV2Preprocessor` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `VHS_VideoInfoSource` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
