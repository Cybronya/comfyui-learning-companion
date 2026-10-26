---
key: 数字人/数字人/Wan Animate2.2动作迁移_1977479722311524353.json
name: Wan Animate2.2动作迁移_1977479722311524353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan Animate2.2动作迁移_1977479722311524353.json
hash: 5bc14f6bd0874b7f
coverage: 0.5625
learned_at: 2026-10-26 01:57:43
nodes: [GetNode, SetNode, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoContextOptions, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, CLIPVisionLoader, GetNode, GetNode, DownloadAndLoadGIMMVFIModel, WanVideoDecode, WanVideoBlockSwap, GetNode, VRAM_Debug, VHS_VideoInfo, GIMMVFI_interpolate, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoTorchCompileSettings, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, WanVideoModelLoader, WanVideoLoraSelectMulti, EmptyImage, VHS_VideoCombine, SaveImage, GetImageSizeAndCount, ImageFromBatch, GetImageSizeAndCount, ImpactSwitch, LoadImage, TT_img_dec, ImpactSwitch, GetNode, TT_img_enc_v2, VHS_VideoCombine, SetNode, ImpactSwitch, PoseAndFaceDetection, OnnxDetectionModelLoader, Reroute, SetNode, SetNode, Reroute, Reroute, GetNode, GetNode, SetNode, Note, PoseDetectionOneToAllAnimation, GetNode, DrawViTPose, ImpactSwitch, easy mathInt, easy mathInt, GetNode, GetNode, JWInteger, easy mathInt, SetNode, VHS_LoadVideo, ImageFromBatch, ImageFromBatch, GetImageSize, SetNode, SetNode, ImageResizeKJv2, JWInteger, CR Prompt Text, PreviewImage, ImageScaleToTotalPixels, Float]
patterns: []
missing: []
---

# 数字人/数字人/Wan Animate2.2动作迁移_1977479722311524353.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan Animate2.2动作迁移_1977479722311524353.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（80 个）：
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `GetNode`
- `VRAM_Debug`
- `VHS_VideoInfo`
- `GIMMVFI_interpolate`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `EmptyImage`
- `VHS_VideoCombine`
- `SaveImage`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `ImpactSwitch`
- `LoadImage`
- `TT_img_dec`
- `ImpactSwitch`
- `GetNode`
- `TT_img_enc_v2`
- `VHS_VideoCombine`
- `SetNode`
- `ImpactSwitch`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `Reroute`
- `SetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `PoseDetectionOneToAllAnimation`
- `GetNode`
- `DrawViTPose`
- `ImpactSwitch`
- `easy mathInt`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `JWInteger`
- `easy mathInt`
- `SetNode`
- `VHS_LoadVideo`
- `ImageFromBatch`
- `ImageFromBatch`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `JWInteger`
- `CR Prompt Text`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `Float`

## 知识

覆盖率 **56%**（45/80）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`DownloadAndLoadGIMMVFIModel`、`WanVideoDecode`、`WanVideoBlockSwap`、`VRAM_Debug`、`VHS_VideoInfo`、`GIMMVFI_interpolate`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`EmptyImage`、`VHS_VideoCombine`、`SaveImage`、`GetImageSizeAndCount`、`ImageFromBatch`、`LoadImage`、`TT_img_dec`、`TT_img_enc_v2`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`PoseDetectionOneToAllAnimation`、`DrawViTPose`、`easy mathInt`、`JWInteger`、`VHS_LoadVideo`、`GetImageSize`、`ImageResizeKJv2`、`CR Prompt Text`、`ImageScaleToTotalPixels`、`Float`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
