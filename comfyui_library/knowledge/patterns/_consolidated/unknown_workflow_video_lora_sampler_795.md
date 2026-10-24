---
name: unknown_workflow_video_lora_sampler_795
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6745
common_nodes: [DrawViTPose, ForLoopClose, ForLoopOpen, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, OnnxDetectionModelLoader, PoseAndFaceDetection, PoseDetectionOneToAllAnimation, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAddOneToAllPoseEmbeds, WanVideoAddOneToAllReferenceEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy batchAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan OnetoAll分镜跳舞视频 动作迁移_2061847616996069378.json, 视频生成/图生视频/Wan OnetoAll动作迁移跳舞视频_2061833238460583938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_795

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan OnetoAll分镜跳舞视频 动作迁移_2061847616996069378.json、视频生成/图生视频/Wan OnetoAll动作迁移跳舞视频_2061833238460583938.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `DrawViTPose`
- `ForLoopClose`
- `ForLoopOpen`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoAddOneToAllReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy batchAnything`

**可变部分**（部分 workflow 才有）：
- `Any To String (mtb)` —— 1/2 个有
- `CM_IntToBool` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `ExtractStoryboards_xuhuan1024` —— 1/2 个有
- `FloatConstant` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageBatchExtendWithOverlap` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `Int` —— 1/2 个有
- `IntBatchSize_xuhuan1024` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `SplitStringByDelimiter` —— 1/2 个有
- `StringToInt` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `VHS_GetImageCount` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanVideoAddOneToAllExtendEmbeds` —— 1/2 个有
- `WanVideoScheduler` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
