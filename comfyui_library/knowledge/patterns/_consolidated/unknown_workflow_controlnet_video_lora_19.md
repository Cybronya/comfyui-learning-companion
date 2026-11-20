---
name: unknown_workflow_controlnet_video_lora_19
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.683571
common_nodes: [AILab_MiniCPM_4_V, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, ConvertOpenPoseKeypointsToDWPose, CreateVideo, DWPreprocessor, DownloadAndLoadNLFModel, FloatConstant, Florence2ModelLoader, Florence2Run, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageFromBatch, ImageFromBatch+, ImageResizeKJv2, ImpactFloat, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MemoryCleaner, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PreviewImage, PrimitiveFloat, RH_Captioner, RenderNLFPoses, SaveImage, SetNode, ShowText|pysssss, SimpleMath+, StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy imageSize, easy int, easy positive, easy promptReplace, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [平台全量/视频-视频生视频(动作)-wan2.1-SCAIL-KJ_2018746990150033409.json, 平台全量/视频-视频生视频(动作)-wan2.1-SCAIL-KJ_2066055929386561536.json, 平台全量/视频-视频生视频动作(分割)-wan2.1-SCAIL-KJ_2019385555640913922.json, 平台全量/视频-视频生视频动作参考图(分割)-wan2.1-SCAIL-KJ_2019670989998657537.json, 平台全量/视频-视频生视频动作参考图(分割)-wan2.1_2041349449766674433.json, 平台全量/视频生图_2041416747802173442.json, 视频生成/图生视频/视频-视频生视频(动作)-wan2.1-SCAIL-KJ+_2046415072397893633.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_19

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/视频-视频生视频(动作)-wan2.1-SCAIL-KJ_2018746990150033409.json、平台全量/视频-视频生视频(动作)-wan2.1-SCAIL-KJ_2066055929386561536.json、平台全量/视频-视频生视频动作(分割)-wan2.1-SCAIL-KJ_2019385555640913922.json、平台全量/视频-视频生视频动作参考图(分割)-wan2.1-SCAIL-KJ_2019670989998657537.json、平台全量/视频-视频生视频动作参考图(分割)-wan2.1_2041349449766674433.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `AILab_MiniCPM_4_V`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConvertOpenPoseKeypointsToDWPose`
- `CreateVideo`
- `DWPreprocessor`
- `DownloadAndLoadNLFModel`
- `FloatConstant`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImpactFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MemoryCleaner`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PreviewImage`
- `PrimitiveFloat`
- `RH_Captioner`
- `RenderNLFPoses`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy imageSize`
- `easy int`
- `easy positive`
- `easy promptReplace`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 5/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `EmptyLatentImage` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `ImpactInt` —— 5/7 个有
- `KSamplerAdvanced` —— 5/7 个有
- `ModelPatchLoader` —— 5/7 个有
- `ZImageFunControlnet` —— 5/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `Switch any [Crystools]` —— 4/7 个有
- `AnyBatchSliceNode` —— 3/7 个有
- `CFGGuider` —— 3/7 个有
- `CM_BoolToInt` —— 3/7 个有
- `CM_IntToBool` —— 3/7 个有
- `CM_IntUnaryOperation` —— 3/7 个有
- `CR Float To Integer` —— 3/7 个有
- `CR String To Number` —— 3/7 个有
- `EmptyFlux2LatentImage` —— 3/7 个有
- `FL_VideoCadence` —— 3/7 个有
- `Float` —— 3/7 个有
- `Flux2Scheduler` —— 3/7 个有
- `GODMT_ListToBatch` —— 3/7 个有
- `ImageConcanate` —— 3/7 个有
- `ImageToDevice+` —— 3/7 个有
- `Int` —— 3/7 个有
- `KSamplerSelect` —— 3/7 个有
- `RandomNoise` —— 3/7 个有
- `ReferenceLatent` —— 3/7 个有
- `SamplerCustomAdvanced` —— 3/7 个有
- `SegmentFrameAdjuster` —— 3/7 个有
- `Text List to Text` —— 3/7 个有
- `TextSplitByDelimiter` —— 3/7 个有
- `VAEEncode` —— 3/7 个有
- `easy batchAnything` —— 3/7 个有
- `easy forLoopEnd` —— 3/7 个有
- `easy forLoopStart` —— 3/7 个有
- `easy lengthAnything` —— 3/7 个有
- `easy mathInt` —— 3/7 个有
- `AutoCropFaces` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `easy imageRemBg` —— 2/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有
- `easy anythingInversedSwitch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1920 - 1920 | 5 | 100% |
| 高度 | 1080 | 1080 - 1080 | 5 | 100% |
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1920，观测区间 1920 - 1920，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
