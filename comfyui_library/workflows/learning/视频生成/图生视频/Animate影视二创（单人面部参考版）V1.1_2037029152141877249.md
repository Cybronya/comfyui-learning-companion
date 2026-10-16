---
key: 视频生成/图生视频/Animate影视二创（单人面部参考版）V1.1_2037029152141877249.json
name: Animate影视二创（单人面部参考版）V1.1_2037029152141877249.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037029152141877249.json
hash: bdfbf002a7f24cea
coverage: 0.517857
learned_at: 2026-10-15 22:35:54
nodes: [Bookmark (rgthree), VHS_VideoCombine, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, PoseAndFaceDetection, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, WanVideoSampler, WanVideoDecode, SetNode, PlaySound|pysssss, OnnxDetectionModelLoader, GetNode, GetNode, SetNode, INTConstant, ImageResizeKJv2, easy imageSizeBySide, DWPreprocessor, SetNode, GetNode, GetNode, ResizeImageMaskNode, GetNode, VHS_VideoCombine, SetNode, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoModelLoader, GetNode, WanVideoSetBlockSwap, WanVideoTextEncodeCached, CLIPVisionLoader, SetNode, WanVideoVAELoader, GetNode, INTConstant, INTConstant, GetNode, GetNode, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Animate影视二创（单人面部参考版）V1.1_2037029152141877249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037029152141877249.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（56 个）：
- `Bookmark (rgthree)`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SetNode`
- `PlaySound|pysssss`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `easy imageSizeBySide`
- `DWPreprocessor`
- `SetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **52%**（29/56）

**有卡**：`Bookmark (rgthree)`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoDecode`、`PlaySound|pysssss`、`OnnxDetectionModelLoader`、`INTConstant`、`ImageResizeKJv2`、`easy imageSizeBySide`、`DWPreprocessor`、`ResizeImageMaskNode`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
