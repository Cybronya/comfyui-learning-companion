---
name: unknown_workflow_video_inpaint_lora_15
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6165
common_nodes: [Any Switch (rgthree), Fast Groups Bypasser (rgthree), Florence2ModelLoader, Florence2Run, GetImageSizeAndCount, GetNode, GoogleTranslateTextNode, GrowMask, INPAINT_MaskedFill, ImageResizeKJ, InvertMask, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: SegmentAnythingUltra V2, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoVRAMManagement, easy int, easy positive, easy seed]
problems: []
missing: []
members: [平台全量/VACE_14B_局部编辑_1929828983905402881.json, 平台全量/啦啦啦_1948582029391736833.json, 平台全量/电商视频换景(文字转场景)_1972191247278534658.json, 平台全量/视频完美换背景(支持3D动画_CG等)_20251010_1976540683588771841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_15

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/VACE_14B_局部编辑_1929828983905402881.json、平台全量/啦啦啦_1948582029391736833.json、平台全量/电商视频换景(文字转场景)_1972191247278534658.json、平台全量/视频完美换背景(支持3D动画_CG等)_20251010_1976540683588771841.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSizeAndCount`
- `GetNode`
- `GoogleTranslateTextNode`
- `GrowMask`
- `INPAINT_MaskedFill`
- `ImageResizeKJ`
- `InvertMask`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
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
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`
- `easy int`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `GetImageSize+` —— 3/4 个有
- `ImageFromBatch` —— 3/4 个有
- `JoinStrings` —— 3/4 个有
- `MaskToImage` —— 3/4 个有
- `PointsEditor` —— 3/4 个有
- `ResizeMask` —— 3/4 个有
- `Sam2Segmentation` —— 3/4 个有
- `String Literal` —— 3/4 个有
- `Bookmark (rgthree)` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `Int` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `Mute / Bypass Relay (rgthree)` —— 2/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `WanVideoLoraSelectMulti` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
