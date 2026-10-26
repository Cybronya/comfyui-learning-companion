---
key: 数字人/数字人/长视频 人物替换动作迁移wan2.2-Animate_1976989855852961793.json
name: 长视频 人物替换动作迁移wan2.2-Animate_1976989855852961793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/长视频 人物替换动作迁移wan2.2-Animate_1976989855852961793.json
hash: 41916ff554a4dc94
coverage: 0.536232
learned_at: 2026-10-26 02:05:51
nodes: [GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Sam2Segmentation, GrowMaskWithBlur, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DownloadAndLoadSAM2Model, GetImageSizeAndCount, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, BlockifyMask, SetNode, DrawViTPose, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, VHS_VideoCombine, WanVideoDecode, ImageConcatMulti, GetImageSizeAndCount, ImageConcatMulti, GetNode, WanVideoVAELoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, VHS_VideoCombine, Note, WanVideoTextEncodeCached, GetNode, WanVideoSampler, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, CLIPVisionLoader, SetNode, SetNode, INTConstant, SetNode, INTConstant, ImageResizeKJv2, ConvertAny2Int, easy float, SetNode, SetNode, SetNode, LoadImage, GetNode, VHS_LoadVideo, Text]
patterns: []
missing: []
---

# 数字人/数字人/长视频 人物替换动作迁移wan2.2-Animate_1976989855852961793.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/长视频 人物替换动作迁移wan2.2-Animate_1976989855852961793.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（69 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `Sam2Segmentation`
- `GrowMaskWithBlur`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `GetImageSizeAndCount`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `SetNode`
- `DrawViTPose`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `VHS_VideoCombine`
- `Note`
- `WanVideoTextEncodeCached`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ConvertAny2Int`
- `easy float`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `VHS_LoadVideo`
- `Text`

## 知识

覆盖率 **54%**（37/69）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`Sam2Segmentation`、`GrowMaskWithBlur`、`DownloadAndLoadSAM2Model`、`GetImageSizeAndCount`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`BlockifyMask`、`DrawViTPose`、`DrawMaskOnImage`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`CLIPVisionLoader`、`INTConstant`、`ImageResizeKJv2`、`ConvertAny2Int`、`easy float`、`LoadImage`、`VHS_LoadVideo`、`Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
