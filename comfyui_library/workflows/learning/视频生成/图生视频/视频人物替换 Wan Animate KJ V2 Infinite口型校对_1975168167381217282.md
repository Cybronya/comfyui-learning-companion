---
key: 视频生成/图生视频/视频人物替换 Wan Animate KJ V2 Infinite口型校对_1975168167381217282.json
name: 视频人物替换 Wan Animate KJ V2 Infinite口型校对_1975168167381217282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1975168167381217282.json
hash: 49a1d23230f5d728
coverage: 0.692308
learned_at: 2026-10-15 22:32:07
nodes: [DownloadAndLoadWav2VecModel, GetNode, easy cleanGpuUsed, AudioSeparation, MultiTalkModelLoader, SaveAudio, Anything Everywhere, GetNode, WanVideoBlockSwap, easy cleanGpuUsed, WanVideoDecode, GetNode, easy cleanGpuUsed, GetNode, SimpleMath+, INTConstant, WanVideoModelLoader, WanVideoLoraSelectMulti, SetNode, SimpleMath+, SetNode, easy showAnything, VHS_VideoCombine, SetNode, SetNode, VHS_VideoCombine, VHS_LoadVideo, SetNode, SetNode, SetNode, OnnxDetectionModelLoader, Reroute, PoseAndFaceDetection, Sam2Segmentation, VHS_VideoCombine, GrowMask, BlockifyMask, VHS_VideoCombine, VHS_VideoCombine, MaskToImage, WanVideoVAELoader, SetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawViTPose, DrawMaskOnImage, INTConstant, INTConstant, WanVideoTextEncodeCached, MultiTalkWav2VecEmbeds, LoadImage, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GetNode, ImageResizeKJv2, RH_Captioner, easy promptConcat, Text]
patterns: []
missing: []
---

# 视频生成/图生视频/视频人物替换 Wan Animate KJ V2 Infinite口型校对_1975168167381217282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975168167381217282.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（65 个）：
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `easy cleanGpuUsed`
- `AudioSeparation`
- `MultiTalkModelLoader`
- `SaveAudio`
- `Anything Everywhere`
- `GetNode`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `SimpleMath+`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `easy showAnything`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `Reroute`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `VHS_VideoCombine`
- `GrowMask`
- `BlockifyMask`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MaskToImage`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawViTPose`
- `DrawMaskOnImage`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `MultiTalkWav2VecEmbeds`
- `LoadImage`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `RH_Captioner`
- `easy promptConcat`
- `Text`

## 知识

覆盖率 **69%**（45/65）

**有卡**：`DownloadAndLoadWav2VecModel`、`easy cleanGpuUsed`、`AudioSeparation`、`MultiTalkModelLoader`、`SaveAudio`、`WanVideoBlockSwap`、`WanVideoDecode`、`SimpleMath+`、`INTConstant`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`VHS_LoadVideo`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`MaskToImage`、`WanVideoVAELoader`、`CLIPVisionLoader`、`DownloadAndLoadSAM2Model`、`DrawViTPose`、`DrawMaskOnImage`、`WanVideoTextEncodeCached`、`MultiTalkWav2VecEmbeds`、`LoadImage`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`RH_Captioner`、`easy promptConcat`、`Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
