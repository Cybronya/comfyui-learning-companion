---
name: unknown_workflow_video_lora_sampler_261
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.67225
common_nodes: [GetImageRangeFromBatch, GetNode, GrowMask, ImageResizeKJv2, LoadImage, MaskPreview, MochaEmbeds, PointsEditor, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1982464273806966785.json, 视频生成/图生视频/2013864867756773377.json, 视频生成/图生视频/1980911162026016770.json, 视频生成/图生视频/1979526023647760386.json, 视频生成/图生视频/1980827522109755393.json, 视频生成/图生视频/1986007241096605697.json, 视频生成/图生视频/1980912658343968770.json, 视频生成/文生视频/（双参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980845806502760449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_261

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1982464273806966785.json、视频生成/图生视频/2013864867756773377.json、视频生成/图生视频/1980911162026016770.json、视频生成/图生视频/1979526023647760386.json、视频生成/图生视频/1980827522109755393.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 8 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskPreview`
- `MochaEmbeds`
- `PointsEditor`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 6/8 个有
- `SeCModelLoader` —— 5/8 个有
- `SeCVideoSegmentation` —— 5/8 个有
- `easy imageRemBg` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `RMBG` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `Crop Face` —— 3/8 个有
- `DownloadAndLoadSAM2Model` —— 3/8 个有
- `Int` —— 3/8 个有
- `Load RetinaFace` —— 3/8 个有
- `Sam2Segmentation` —— 3/8 个有
- `VHS_VideoInfo` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `JWInteger` —— 2/8 个有
- `PDIMAGE_LongerSize` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `DF_Int_to_Float` —— 1/8 个有
- `DeepTranslatorTextNode` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
