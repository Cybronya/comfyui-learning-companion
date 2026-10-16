---
key: 视频生成/图生视频/wan2.2Animate_2027745342615195649.json
name: wan2.2Animate_2027745342615195649.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2027745342615195649.json
hash: 6d7effea55816d6c
coverage: 0.692308
learned_at: 2026-10-15 22:35:18
nodes: [CLIPTextEncode, GrowMask, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, LoraLoaderModelOnly, UNETLoader, MarkdownNote, ModelSamplingSD3, CLIPLoader, VAELoader, BlockifyMask, MaskToImage, Sam2Segmentation, DrawMaskOnImage, DownloadAndLoadSAM2Model, VHS_VideoCombine, WanVideoSampler, CLIPTextEncode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, GrowMask, LoadImage, CLIPVisionLoader, LoadVideo, DWPreprocessor, DrawMaskOnImage, SetNode, BlockifyMask, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, VHS_VideoCombine, MaskToImage, SetNode, SetNode, MarkdownNote, Note, GetVideoComponents, ImageScale, SetNode, VHS_VideoCombine, SetNode, PixelPerfectResolution, VHS_LoadVideo, SetNode, VHS_VideoCombine, SetNode, PrimitiveInt, WanVideoClipVisionEncode, VHS_VideoCombine, SeCVideoSegmentation, MarkdownNote, VHS_VideoCombine, SeCModelLoader, WanVideoTextEncodeCached, PointsEditor, GetNode, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, PrimitiveInt, SetNode, GetNode, WanVideoVAELoader, GetNode, WanVideoAnimateEmbeds, Float, easy imageSwitch, easy imageSwitch, VHS_LoadVideo, DWPreprocessor]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2Animate_2027745342615195649.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027745342615195649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（78 个）：
- `CLIPTextEncode` ★核心
- `GrowMask`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `BlockifyMask`
- `MaskToImage`
- `Sam2Segmentation`
- `DrawMaskOnImage`
- `DownloadAndLoadSAM2Model`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `GrowMask`
- `LoadImage`
- `CLIPVisionLoader`
- `LoadVideo`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `SetNode`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `MaskToImage`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `Note`
- `GetVideoComponents`
- `ImageScale`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `PrimitiveInt`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `SeCVideoSegmentation`
- `MarkdownNote`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `WanVideoTextEncodeCached`
- `PointsEditor`
- `GetNode`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `WanVideoVAELoader`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `Float`
- `easy imageSwitch`
- `easy imageSwitch`
- `VHS_LoadVideo`
- `DWPreprocessor`

## 知识

覆盖率 **69%**（54/78）

**有卡**：`CLIPTextEncode`、`GrowMask`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`BlockifyMask`、`MaskToImage`、`Sam2Segmentation`、`DrawMaskOnImage`、`DownloadAndLoadSAM2Model`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`LoadImage`、`CLIPVisionLoader`、`LoadVideo`、`DWPreprocessor`、`WanVideoDecode`、`GetVideoComponents`、`ImageScale`、`PixelPerfectResolution`、`VHS_LoadVideo`、`WanVideoClipVisionEncode`、`SeCVideoSegmentation`、`SeCModelLoader`、`WanVideoTextEncodeCached`、`PointsEditor`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`Float`、`easy imageSwitch`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanVideoSampler、WanVideoDecode
