---
key: 数字人/数字人/舞蹈克隆_动作迁移表情迁移_改变原图背景_Wan2.2_1995364899742265346.json
name: 舞蹈克隆_动作迁移表情迁移_改变原图背景_Wan2.2_1995364899742265346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/舞蹈克隆_动作迁移表情迁移_改变原图背景_Wan2.2_1995364899742265346.json
hash: a34db3e735d3b99e
coverage: 0.552632
learned_at: 2026-10-26 02:04:36
nodes: [WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoModelLoader, INTConstant, SetNode, SetNode, INTConstant, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, CLIPVisionLoader, GetNode, WanVideoAnimateEmbeds, SetNode, SetNode, BlockifyMask, Sam2Segmentation, GrowMask, SetNode, SetNode, SetNode, DownloadAndLoadSAM2Model, PoseAndFaceDetection, DrawMaskOnImage, SetNode, SetNode, OnnxDetectionModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, DrawViTPose, GetImageSizeAndCount, SetNode, ImageResizeKJv2, GetNode, ImageBlend, PreviewImage, VHS_VideoCombine, PreviewImage, PreviewImage, GetNode, GetNode, WanVideoVAELoader, GetNode, SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), WanVideoTextEncodeCached, GetNode, SetNode, WanVideoSampler, VHS_VideoCombine, SaveLatent, WanVideoEncode, TT_img_enc_v2, ImageConcatMulti, Int, MathExpression|pysssss, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/舞蹈克隆_动作迁移表情迁移_改变原图背景_Wan2.2_1995364899742265346.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/舞蹈克隆_动作迁移表情迁移_改变原图背景_Wan2.2_1995364899742265346.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（76 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `INTConstant`
- `SetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `Sam2Segmentation`
- `GrowMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `DownloadAndLoadSAM2Model`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `ImageBlend`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `GetNode`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoTextEncodeCached`
- `GetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `SaveLatent`
- `WanVideoEncode`
- `TT_img_enc_v2`
- `ImageConcatMulti`
- `Int`
- `MathExpression|pysssss`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **55%**（42/76）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`INTConstant`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`BlockifyMask`、`Sam2Segmentation`、`GrowMask`、`DownloadAndLoadSAM2Model`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`DrawViTPose`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`ImageBlend`、`VHS_VideoCombine`、`WanVideoVAELoader`、`SaveImage`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`SaveLatent`、`WanVideoEncode`、`TT_img_enc_v2`、`ImageConcatMulti`、`Int`、`MathExpression|pysssss`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、SaveLatent、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
