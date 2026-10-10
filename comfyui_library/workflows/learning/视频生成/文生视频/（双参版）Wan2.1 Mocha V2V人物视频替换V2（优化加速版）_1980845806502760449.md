---
key: 视频生成/文生视频/（双参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980845806502760449.json
name: （双参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980845806502760449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（双参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980845806502760449.json
hash: 4c4e5f49a51ef7ce
coverage: 0.625
learned_at: 2026-10-11 02:45:05
nodes: [ImageResizeKJv2, SetNode, GetNode, GetNode, GetImageRangeFromBatch, MaskPreview, DownloadAndLoadSAM2Model, Sam2Segmentation, SetNode, GrowMask, GetNode, PreviewImage, WanVideoSampler, MochaEmbeds, GetNode, MarkdownNote, LoadImage, Load RetinaFace, Crop Face, SaveImage, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageConcanate, SetNode, PointsEditor, PreviewImage, SaveImage, JWInteger, SetNode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, ImageConcanate, ImageConcanate, PDIMAGE_LongerSize, MarkdownNote, RMBG, CR Prompt Text, LoadImage, PreviewImage, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoInfo]
patterns: []
missing: [Crop Face, LayerUtility: ImageScaleByAspectRatio V2, Load RetinaFace, CR Prompt Text]
discoveries: [次要节点 `Crop Face` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Load RetinaFace` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（双参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980845806502760449.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（双参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980845806502760449.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `MaskPreview`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `SetNode`
- `GrowMask`
- `GetNode`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `MochaEmbeds`
- `GetNode`
- `MarkdownNote`
- `LoadImage`
- `Load RetinaFace`
- `Crop Face`
- `SaveImage`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageConcanate`
- `SetNode`
- `PointsEditor`
- `PreviewImage`
- `SaveImage`
- `JWInteger`
- `SetNode`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `ImageConcanate`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `MarkdownNote`
- `RMBG`
- `CR Prompt Text`
- `LoadImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoInfo`

## 知识

覆盖率 **62%**（30/48）

**有卡**：`ImageResizeKJv2`、`GetImageRangeFromBatch`、`MaskPreview`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`WanVideoSampler`、`MochaEmbeds`、`LoadImage`、`SaveImage`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageConcanate`、`PointsEditor`、`JWInteger`、`PDIMAGE_LongerSize`、`RMBG`、`VHS_VideoCombine`、`WanVideoDecode`、`VHS_LoadVideo`、`VHS_VideoInfo`

**缺卡**（4）：`Crop Face`、`LayerUtility: ImageScaleByAspectRatio V2`、`Load RetinaFace`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelectMulti、ImageResizeKJv2、PDIMAGE_LongerSize

## 学习发现

- 次要节点 `Crop Face` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Load RetinaFace` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
