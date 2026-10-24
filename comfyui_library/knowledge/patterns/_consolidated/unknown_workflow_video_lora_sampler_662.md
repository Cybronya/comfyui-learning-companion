---
name: unknown_workflow_video_lora_sampler_662
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.875667
common_nodes: [CLIPVisionLoader, DrawViTPose, Evaluate Integers, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, PrimitiveStringMultiline, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/【🛫书墨】人物换装-参考动作、表情(多图)_2011369143001423874.json, 视频生成/图生视频/人物换装-参考动作、表情(多图)_2050270742914322434.json, 音频生成/音频生成/wan2-2唱歌参考动态表情动作AnimateKJ_v2视频生成工作流_1982391407681912834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_662

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【🛫书墨】人物换装-参考动作、表情(多图)_2011369143001423874.json、视频生成/图生视频/人物换装-参考动作、表情(多图)_2050270742914322434.json、音频生成/音频生成/wan2-2唱歌参考动态表情动作AnimateKJ_v2视频生成工作流_1982391407681912834.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `Evaluate Integers`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 2/3 个有
- `Evaluate Floats` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Image Batch` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `SynVowImageBatchRangeIndex` —— 2/3 个有
- `SynVowImageTotalGroups` —— 2/3 个有
- `easy batchAnything` —— 2/3 个有
- `easy convertAnything` —— 2/3 个有
- `easy float` —— 2/3 个有
- `easy forLoopEnd` —— 2/3 个有
- `easy forLoopStart` —— 2/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
