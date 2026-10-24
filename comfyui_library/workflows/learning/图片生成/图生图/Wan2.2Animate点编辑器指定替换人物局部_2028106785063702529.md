---
key: 图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json
name: Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json
hash: 19b34f119df4d345
coverage: 0.928571
learned_at: 2026-10-23 11:28:09
nodes: [CoordinatePlotter, PreviewImage, CoordinatePlotter, WanVideoModelLoader, LoadImage, INTConstant, WanVideoAnimateEmbeds, GrowMaskWithBlur, WanVideoClipVisionEncode, WanVideoSampler, CLIPVisionLoader, ImageResizeKJv2, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, SeCVideoSegmentation, WanVideoTextEncodeCached, VHS_VideoCombine, VHS_VideoCombine, DrawViTPose, DrawMaskOnImage, VHS_VideoCombine, PoseAndFaceDetection, BlockifyMask, GetImageSizeAndCount, OnnxDetectionModelLoader, PreviewImage, INTConstant, VHS_LoadVideo, PrimitiveInt, ImageFromBatch, SeCModelLoader, WanVideoDecode, VHS_VideoCombine, PDIMAGE_LongerSize, ImageConcatMulti, GetImageSizeAndCount, VHS_VideoCombine, PointsEditor, LayerMask: MaskPreview]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `CoordinatePlotter`
- `PreviewImage`
- `CoordinatePlotter`
- `WanVideoModelLoader`
- `LoadImage`
- `INTConstant`
- `WanVideoAnimateEmbeds`
- `GrowMaskWithBlur`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `SeCVideoSegmentation`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DrawViTPose`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `INTConstant`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `ImageFromBatch`
- `SeCModelLoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `PointsEditor`
- `LayerMask: MaskPreview`

## 知识

覆盖率 **93%**（39/42）

**有卡**：`CoordinatePlotter`、`WanVideoModelLoader`、`LoadImage`、`INTConstant`、`WanVideoAnimateEmbeds`、`GrowMaskWithBlur`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`SeCVideoSegmentation`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`DrawViTPose`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`BlockifyMask`、`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`VHS_LoadVideo`、`ImageFromBatch`、`SeCModelLoader`、`WanVideoDecode`、`PDIMAGE_LongerSize`、`ImageConcatMulti`、`PointsEditor`、`LayerMask: MaskPreview`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
