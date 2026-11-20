---
key: 平台全量/（（自用）-双参N版）Wan2.1 Mocha V2V人物视频替换V1（优化加速版）_1981010326328053761.json
name: （（自用）-双参N版）Wan2.1 Mocha V2V人物视频替换V1（优化加速版）_1981010326328053761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（（自用）-双参N版）Wan2.1 Mocha V2V人物视频替换V1（优化加速版）_1981010326328053761.json
hash: ce825ba707901e0a
coverage: 0.731707
learned_at: 2026-11-14 02:54:21
nodes: [ImageResizeKJv2, SetNode, GetNode, GetNode, GetImageRangeFromBatch, DownloadAndLoadSAM2Model, Sam2Segmentation, SetNode, GrowMask, GetNode, WanVideoSampler, MochaEmbeds, GetNode, MarkdownNote, Load RetinaFace, Crop Face, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, SetNode, JWInteger, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, RMBG, CR Prompt Text, WanVideoDecode, TT_img_enc_v2, VHS_VideoInfo, VHS_LoadVideo, Reroute, SaveImage, PointsEditor, MaskPreview, TT_img_enc, SaveImage, LoadImage, MarkdownNote, CR Prompt Text]
patterns: []
missing: []
---

# 平台全量/（（自用）-双参N版）Wan2.1 Mocha V2V人物视频替换V1（优化加速版）_1981010326328053761.json

> 来源文件 `comfyui_library/workflows/平台全量/（（自用）-双参N版）Wan2.1 Mocha V2V人物视频替换V1（优化加速版）_1981010326328053761.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `SetNode`
- `GrowMask`
- `GetNode`
- `WanVideoSampler` ★核心
- `MochaEmbeds`
- `GetNode`
- `MarkdownNote`
- `Load RetinaFace`
- `Crop Face`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `JWInteger`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `RMBG`
- `CR Prompt Text`
- `WanVideoDecode`
- `TT_img_enc_v2`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `Reroute`
- `SaveImage`
- `PointsEditor`
- `MaskPreview`
- `TT_img_enc`
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `CR Prompt Text`

## 知识

覆盖率 **73%**（30/41）

**有卡**：`ImageResizeKJv2`、`GetImageRangeFromBatch`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`WanVideoSampler`、`MochaEmbeds`、`Load RetinaFace`、`Crop Face`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`RMBG`、`CR Prompt Text`、`WanVideoDecode`、`TT_img_enc_v2`、`VHS_VideoInfo`、`VHS_LoadVideo`、`SaveImage`、`PointsEditor`、`MaskPreview`、`TT_img_enc`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CR Prompt Text
