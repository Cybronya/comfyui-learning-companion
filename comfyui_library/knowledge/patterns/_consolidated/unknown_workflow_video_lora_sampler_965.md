---
name: unknown_workflow_video_lora_sampler_965
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7815
common_nodes: [Florence2Run, GetImageSizeAndCount, ImageBlend, ImageFromBatch, ImageResizeKJ, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [平台全量/10s+长视频自动完整视频转绘_1913560429715517441.json, 平台全量/For循环分批次的Wan2.1-Fun视频转绘_1909861024038645762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_965

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/10s+长视频自动完整视频转绘_1913560429715517441.json、平台全量/For循环分批次的Wan2.1-Fun视频转绘_1909861024038645762.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Florence2Run`
- `GetImageSizeAndCount`
- `ImageBlend`
- `ImageFromBatch`
- `ImageResizeKJ`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `KepStringLiteral` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `VHS_BatchManager` —— 1/2 个有
- `VHS_VideoInfoSource` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy promptReplace` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
