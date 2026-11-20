---
name: unknown_workflow_video_inpaint_lora_8
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.576571
common_nodes: [Any Switch (rgthree), ClothesSegment, FaceSegment, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), GetImageSize+, GetImageSizeAndCount, GetNode, GrowMask, INPAINT_MaskedFill, ImageFromBatch, ImageResize+, InvertMask, Label (rgthree), LoadImage, LoadWanVideoT5TextEncoder, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PreviewImage, PrimitiveStringMultiline, RMBG, ResizeMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed, easy int, easy seed]
problems: []
missing: []
members: [平台全量/wan2.1 视频人物替换换人工作流视频换人_1952207188704047105.json, 平台全量/wan2.1 视频编辑重绘V1 -阿硕（已更新到V4）_1946890674786721793.json, 平台全量/wan2.1 视频编辑重绘_1967788000916701186.json, 平台全量/wan2.1+视频编辑重绘V1+-阿硕（已更新到V4）_1985671719744614402.json, 平台全量/视频编辑视频转绘视频重绘V1（阿硕v1）_1968916025309843458.json, 视频生成/图生视频/wan2.1 视频编辑重绘 多功能遮罩版（单独换脸、服装、动作、背景、或自定义遮罩）_1981001980585840642.json, 视频生成/图生视频/wan2.1VACE+Lightx2v换服装_2007176668045123586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_8

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/wan2.1 视频人物替换换人工作流视频换人_1952207188704047105.json、平台全量/wan2.1 视频编辑重绘V1 -阿硕（已更新到V4）_1946890674786721793.json、平台全量/wan2.1 视频编辑重绘_1967788000916701186.json、平台全量/wan2.1+视频编辑重绘V1+-阿硕（已更新到V4）_1985671719744614402.json、平台全量/视频编辑视频转绘视频重绘V1（阿硕v1）_1968916025309843458.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `ClothesSegment`
- `FaceSegment`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INPAINT_MaskedFill`
- `ImageFromBatch`
- `ImageResize+`
- `InvertMask`
- `Label (rgthree)`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RMBG`
- `ResizeMask`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `ImageResizeKJ` —— 6/7 个有
- `MaskToImage` —— 6/7 个有
- `PrimitiveString` —— 6/7 个有
- `StringConcatenate` —— 6/7 个有
- `BBoxesToSAM2` —— 5/7 个有
- `DownloadAndLoadQwenModel` —— 5/7 个有
- `DownloadAndLoadSAM2Model` —— 5/7 个有
- `LayerMask: DrawBBoxMaskV2` —— 5/7 个有
- `LayerMask: ObjectDetectorMask` —— 5/7 个有
- `LayerMask: SAM2VideoUltra` —— 5/7 个有
- `QwenVLDetection` —— 5/7 个有
- `Sam2Segmentation` —— 5/7 个有
- `Bookmark (rgthree)` —— 4/7 个有
- `GrowMaskWithBlur` —— 3/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LayerMask: BiRefNetUltraV2` —— 1/7 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
