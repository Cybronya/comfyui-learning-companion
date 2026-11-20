---
name: unknown_workflow_video_inpaint_upscale_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.777667
common_nodes: [CreateCFGScheduleFloatList, Fast Groups Muter (rgthree), GetImageSizeAndCount, GetNode, GrowMask, INPAINT_MaskedFill, INTConstant, ImageFromBatch, ImageFromBatch+, ImageUpscaleWithModelBatched, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerMask: SAM2VideoUltra, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, MaskToImage, RH_Translator, RIFE VFI, SetNode, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.2 VACE任意视频换背景_2010874604692185090.json, 平台全量/wan2.2视频换背景_1957367973776388098.json, 平台全量/wan2.2视频换背景_2040699589145141250.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_upscale_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Wan2.2 VACE任意视频换背景_2010874604692185090.json、平台全量/wan2.2视频换背景_1957367973776388098.json、平台全量/wan2.2视频换背景_2040699589145141250.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `Fast Groups Muter (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INPAINT_MaskedFill`
- `INTConstant`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImageUpscaleWithModelBatched`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LayerMask: SAM2VideoUltra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `RH_Translator`
- `RIFE VFI`
- `SetNode`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `MaskPreview` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `Sa2VANodeTpl` —— 1/3 个有
- `SeCModelLoader` —— 1/3 个有
- `SeCVideoSegmentation` —— 1/3 个有
- `TTP_text_mix` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
