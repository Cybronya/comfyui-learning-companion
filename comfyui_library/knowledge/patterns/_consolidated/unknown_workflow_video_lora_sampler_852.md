---
name: unknown_workflow_video_lora_sampler_852
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5135
common_nodes: [CLIPVisionLoader, DWPreprocessor, EmptyImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, ImpactSwitch, LoadImage, MathExpression|pysssss, PixelPerfectResolution, PreviewAny, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy batchAnything, easy cleanGpuUsed, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy int]
problems: []
missing: []
members: [视频生成/图生视频/wan_animate+KJ版+长视频动作迁移+分辨率、帧率选择，首尾帧丢弃选择_1970700408228376577.json, 视频生成/图生视频/wan_animate+长视频不限时长人物替换_1970265248752148481.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_852

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan_animate+KJ版+长视频动作迁移+分辨率、帧率选择，首尾帧丢弃选择_1970700408228376577.json、视频生成/图生视频/wan_animate+长视频不限时长人物替换_1970265248752148481.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `EmptyImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `LoadImage`
- `MathExpression|pysssss`
- `PixelPerfectResolution`
- `PreviewAny`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/2 个有
- `ConvertAny2Int` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `FaceMaskFromPoseKeypoints` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `Florence2toCoordinates` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `ImageCropByMaskAndResize` —— 1/2 个有
- `PointsEditor` —— 1/2 个有
- `Sam2Segmentation` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
