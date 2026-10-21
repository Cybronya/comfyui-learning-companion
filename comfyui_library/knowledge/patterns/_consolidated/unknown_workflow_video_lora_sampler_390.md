---
name: unknown_workflow_video_lora_sampler_390
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.837167
common_nodes: [DWPreprocessor, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatch, ImageResizeKJv2, Int, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, SetNode, SimpleMath+, VHS_BatchManager, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy seed]
problems: []
missing: [MathExpression|pysssss, SimpleMath+, String Literal, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy globalSeed, easy seed]
members: [视频生成/图生视频/1942816632961961986.json, 视频生成/文生视频/1967140300189786113.json, 视频生成/文生视频/1967169915356581890.json, 视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json, 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_2072999578611523584.json, 视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环深度引导控制+参考_2072999578032709632.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_390

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1942816632961961986.json、视频生成/文生视频/1967140300189786113.json、视频生成/文生视频/1967169915356581890.json、视频生成/文生视频/Wan 2.2 姿态引导下的 SVI 2.0 视频到视频无限循环延长与高一致性生成工作流_1998603727122653185.json、视频生成/文生视频/Wan 2.2-Fun-VACE转绘8帧重叠循环姿态引导控制+参考_2072999578611523584.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `String Literal` —— 5/6 个有
- `WanVideoScheduler` —— 5/6 个有
- `WanVideoSetBlockSwap` —— 5/6 个有
- `WanVideoSetLoRAs` —— 5/6 个有
- `WanVideoSigmaToStep` —— 5/6 个有
- `easy globalSeed` —— 5/6 个有
- `DepthCrafter` —— 2/6 个有
- `DownloadAndLoadDepthCrafterModel` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `LoadLynxResampler` —— 1/6 个有
- `LynxEncodeFaceIP` —— 1/6 个有
- `LynxInsightFaceCrop` —— 1/6 个有
- `MultiTalkModelLoader` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `WanVideoAddLynxEmbeds` —— 1/6 个有
- `WanVideoEnhanceAVideo` —— 1/6 个有
- `WanVideoExperimentalArgs` —— 1/6 个有
- `WanVideoExtraModelSelect` —— 1/6 个有
- `WanVideoSLG` —— 1/6 个有
- `WanVideoTeaCache` —— 1/6 个有
- `WanVideoTorchCompileSettings` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、SimpleMath+、String Literal、easy batchAnything、easy forLoopEnd
