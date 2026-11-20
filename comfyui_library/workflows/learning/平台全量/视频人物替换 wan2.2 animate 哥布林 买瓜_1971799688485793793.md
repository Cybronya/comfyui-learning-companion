---
key: 平台全量/视频人物替换 wan2.2 animate 哥布林 买瓜_1971799688485793793.json
name: 视频人物替换 wan2.2 animate 哥布林 买瓜_1971799688485793793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频人物替换 wan2.2 animate 哥布林 买瓜_1971799688485793793.json
hash: 887aa96080bb6bea
coverage: 0.613333
learned_at: 2026-11-14 02:35:12
nodes: [SetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, SetNode, GetNode, GetNode, SetNode, GetNode, WanVideoClipVisionEncode, WanVideoVAELoader, CLIPVisionLoader, GetNode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoDecode, ResizeAndPadImage, RMBG, Textbox, LoadImage, PreviewImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RH_Translator, DF_Get_image_size, SetNode, SetNode, INTConstant, INTConstant, SetNode, ImageResizeKJv2, SetNode, LayerUtility: ColorImage V2, SetNode, INTConstant, SetNode, SetNode, AILab_ImageCombiner, GetImageSizeAndCount, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, easy showAnything, WanVideoTextEncodeCached, MarkdownNote, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, DrawMaskOnImage, GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoAnimateEmbeds, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, Sam2Segmentation, DownloadAndLoadSAM2Model, GrowMask, PreviewImage, SetNode, RHHiddenNodes, BlockifyMask, WanVideoSampler, PointsEditor, VHS_LoadVideo, VHS_VideoInfo, RepeatImageBatch, ImageResizeKJv2, Frame Select]
patterns: []
missing: []
---

# 平台全量/视频人物替换 wan2.2 animate 哥布林 买瓜_1971799688485793793.json

> 来源文件 `comfyui_library/workflows/平台全量/视频人物替换 wan2.2 animate 哥布林 买瓜_1971799688485793793.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（75 个）：
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `ResizeAndPadImage`
- `RMBG`
- `Textbox`
- `LoadImage`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RH_Translator`
- `DF_Get_image_size`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `LayerUtility: ColorImage V2`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `AILab_ImageCombiner`
- `GetImageSizeAndCount`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy showAnything`
- `WanVideoTextEncodeCached`
- `MarkdownNote`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `DrawMaskOnImage`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoAnimateEmbeds`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `GrowMask`
- `PreviewImage`
- `SetNode`
- `RHHiddenNodes`
- `BlockifyMask`
- `WanVideoSampler` ★核心
- `PointsEditor`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `RepeatImageBatch`
- `ImageResizeKJv2`
- `Frame Select`

## 知识

覆盖率 **61%**（46/75）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoDecode`、`ResizeAndPadImage`、`RMBG`、`Textbox`、`LoadImage`、`RH_Translator`、`DF_Get_image_size`、`INTConstant`、`ImageResizeKJv2`、`LayerUtility: ColorImage V2`、`AILab_ImageCombiner`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`DrawMaskOnImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoAnimateEmbeds`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`GrowMask`、`RHHiddenNodes`、`BlockifyMask`、`WanVideoSampler`、`PointsEditor`、`VHS_LoadVideo`、`VHS_VideoInfo`、`RepeatImageBatch`、`Frame Select`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
