---
name: unknown_workflow_video_sampler_vae_115
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.899
common_nodes: [DWPreprocessor, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatch, ImageResizeKJv2, Int, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, SetNode, SimpleMath+, VHS_BatchManager, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/转绘循环-8帧重叠_1942816632961961986.json, 视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json, 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113.json, 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_1967169915356581890.json, 视频生成/文生视频/无限时长视频转绘Lynx+InfiniteTalk+VACE_1976202797450428418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_115

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/转绘循环-8帧重叠_1942816632961961986.json、视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json、视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_1967140300189786113.json、视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_1967169915356581890.json、视频生成/文生视频/无限时长视频转绘Lynx+InfiniteTalk+VACE_1976202797450428418.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `DWPreprocessor`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatch`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `SetNode`
- `SimpleMath+`
- `VHS_BatchManager`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `String Literal` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `WanVideoSetBlockSwap` —— 4/5 个有
- `WanVideoSetLoRAs` —— 4/5 个有
- `WanVideoVACEModelSelect` —— 4/5 个有
- `WanVideoScheduler` —— 3/5 个有
- `WanVideoSigmaToStep` —— 3/5 个有
- `easy globalSeed` —— 3/5 个有
- `LoadLynxResampler` —— 2/5 个有
- `LynxEncodeFaceIP` —— 2/5 个有
- `LynxInsightFaceCrop` —— 2/5 个有
- `MultiTalkModelLoader` —— 2/5 个有
- `WanVideoAddLynxEmbeds` —— 2/5 个有
- `WanVideoExtraModelSelect` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `ACE_AudioCrop` —— 1/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `AudioSeparation` —— 1/5 个有
- `DepthCrafter` —— 1/5 个有
- `DownloadAndLoadDepthCrafterModel` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `MultiTalkWav2VecEmbeds` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `WanVideoEnhanceAVideo` —— 1/5 个有
- `WanVideoExperimentalArgs` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有
- `WanVideoSLG` —— 1/5 个有
- `WanVideoTeaCache` —— 1/5 个有
- `WanVideoTextEncodeCached` —— 1/5 个有
- `Wav2VecModelLoader` —— 1/5 个有
- `floatToText _O` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
