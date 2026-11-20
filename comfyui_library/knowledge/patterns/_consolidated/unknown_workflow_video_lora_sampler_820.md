---
name: unknown_workflow_video_lora_sampler_820
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.511667
common_nodes: [CLIPVisionLoader, DWPreprocessor, EmptyImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, ImpactSwitch, LoadImage, MathExpression|pysssss, PixelPerfectResolution, PreviewAny, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy batchAnything, easy cleanGpuUsed, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy int]
problems: []
missing: []
members: [平台全量/wan_animate+KJ版+长视频人物替换+分辨率、帧率选择，首尾帧丢弃选择_1970333097428480001.json, 视频生成/图生视频/wan_animate+KJ版+长视频动作迁移+分辨率、帧率选择，首尾帧丢弃选择_1970700408228376577.json, 视频生成/图生视频/wan_animate+长视频不限时长人物替换_1970265248752148481.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_820

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/wan_animate+KJ版+长视频人物替换+分辨率、帧率选择，首尾帧丢弃选择_1970333097428480001.json、视频生成/图生视频/wan_animate+KJ版+长视频动作迁移+分辨率、帧率选择，首尾帧丢弃选择_1970700408228376577.json、视频生成/图生视频/wan_animate+长视频不限时长人物替换_1970265248752148481.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 3 个 workflow 都包含：
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
- `BlockifyMask` —— 2/3 个有
- `ConvertAny2Int` —— 2/3 个有
- `DownloadAndLoadSAM2Model` —— 2/3 个有
- `DrawMaskOnImage` —— 2/3 个有
- `FaceMaskFromPoseKeypoints` —— 2/3 个有
- `GrowMask` —— 2/3 个有
- `ImageCropByMaskAndResize` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `Sam2Segmentation` —— 2/3 个有
- `easy float` —— 2/3 个有
- `Display Int (rgthree)` —— 1/3 个有
- `DownloadAndLoadFlorence2Model` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `Florence2toCoordinates` —— 1/3 个有
- `SoundFlow_TrimAudio` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
