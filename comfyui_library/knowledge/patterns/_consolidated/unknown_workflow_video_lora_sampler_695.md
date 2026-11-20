---
name: unknown_workflow_video_lora_sampler_695
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.64475
common_nodes: [BlockifyMask, CLIPVisionLoader, ConvertAny2Int, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GetImageRangeFromBatch, GetImageSizeAndCount, GrowMask, ImageConcatMulti, ImageResizeKJv2, LayerUtility: ImageBlend, LoadImage, MathExpression|pysssss, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, SoundFlow_TrimAudio, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy float, easy int]
problems: []
missing: []
members: [平台全量/人物替换+动作迁移+对口型（根叔）_1977242202525048833.json, 数字人/数字人/长视频wan_animate-自动人物替换+动作迁移+InfiniteTalk对口型-电商数字人_1975573542223876097.json, 数字人/数字人/长视频wan_animate-自动人物替换+动作迁移-唱歌跳舞_1972675635229446145.json, 视频生成/图生视频/wan_animate+KJ版+长视频全自动+替换人物+动作迁移+首尾帧丢弃_1972178005500030977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_695

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/人物替换+动作迁移+对口型（根叔）_1977242202525048833.json、数字人/数字人/长视频wan_animate-自动人物替换+动作迁移+InfiniteTalk对口型-电商数字人_1975573542223876097.json、数字人/数字人/长视频wan_animate-自动人物替换+动作迁移-唱歌跳舞_1972675635229446145.json、视频生成/图生视频/wan_animate+KJ版+长视频全自动+替换人物+动作迁移+首尾帧丢弃_1972178005500030977.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 4 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `ConvertAny2Int`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GrowMask`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `MathExpression|pysssss`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `SoundFlow_TrimAudio`
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
- `easy float`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `AudioSeparation` —— 2/4 个有
- `DownloadAndLoadWav2VecModel` —— 2/4 个有
- `MultiTalkModelLoader` —— 2/4 个有
- `MultiTalkWav2VecEmbeds` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `WanVideoEncode` —— 2/4 个有
- `WanVideoImageToVideoMultiTalk` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `EmptyImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
