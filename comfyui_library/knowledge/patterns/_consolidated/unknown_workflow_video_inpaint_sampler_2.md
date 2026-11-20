---
name: unknown_workflow_video_inpaint_sampler_2
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.71425
common_nodes: [AIO_Preprocessor, AddLabel, EmptyImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageConcanate, ImageConcatMulti, ImagePadKJ, ImageResizeKJ, InpaintPreprocessor, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [平台全量/VACE+FusionX+NAG_1933815638596964354.json, 平台全量/【大炮精选】VACE视频开源全系功能_1922836682058469377.json, 平台全量/龙明Wan+VACE视频编辑工作流（5合一完整版）_1928676917736587265.json, 视频生成/图生视频/VACE+ACCVID加速工作流_1927072484653223937.json, 视频生成/图生视频/VACE+ACCVID加速工作流_1927172015592210434.json, 视频生成/图生视频/VACE视频开源全系功能_1972511577779990529.json, 视频生成/图生视频/vace_all_1922695812248387585.json, 视频生成/图生视频/vace_全功能视频编辑工作流_1922711009637842946.json, 视频生成/图生视频/wan2.1-VACE多功能视频编辑合集_1988044304205680642.json, 视频生成/图生视频/龙明VACE+ACCVID加速工作流_1928697950808215553.json, 视频生成/图生视频/龙明VACE+FusionX+NAG_1934990691049086977.json, 视频生成/文生视频/CG迷-FusionX超强VACE视频编辑工作流_1937481495915466754.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_2

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/VACE+FusionX+NAG_1933815638596964354.json、平台全量/【大炮精选】VACE视频开源全系功能_1922836682058469377.json、平台全量/龙明Wan+VACE视频编辑工作流（5合一完整版）_1928676917736587265.json、视频生成/图生视频/VACE+ACCVID加速工作流_1927072484653223937.json、视频生成/图生视频/VACE+ACCVID加速工作流_1927172015592210434.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 12 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `EmptyImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 10/12 个有
- `WanVideoVACEModelSelect` —— 10/12 个有
- `MaskPreview+` —— 9/12 个有
- `WanVideoTeaCache` —— 9/12 个有
- `WanVideoTextEncode` —— 9/12 个有
- `ImageBlend` —— 6/12 个有
- `ImageResizeKJv2` —— 6/12 个有
- `DownloadAndLoadSAM2Model` —— 3/12 个有
- `ImageCompositeMasked` —— 3/12 个有
- `MaskPreview` —— 3/12 个有
- `PointsEditor` —— 3/12 个有
- `PreviewAnimation` —— 3/12 个有
- `Sam2Segmentation` —— 3/12 个有
- `ShowText|pysssss` —— 3/12 个有
- `VHS_VideoInfo` —— 3/12 个有
- `WanVideoApplyNAG` —— 3/12 个有
- `WanVideoTextEncodeSingle` —— 3/12 个有
- `WanVideoTorchCompileSettings` —— 3/12 个有
- `ImageResize+` —— 1/12 个有
- `Note Plus (mtb)` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
