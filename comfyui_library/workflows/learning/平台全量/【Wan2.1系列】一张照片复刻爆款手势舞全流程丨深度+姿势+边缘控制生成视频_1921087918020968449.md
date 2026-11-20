---
key: 平台全量/【Wan2.1系列】一张照片复刻爆款手势舞全流程丨深度+姿势+边缘控制生成视频_1921087918020968449.json
name: 【Wan2.1系列】一张照片复刻爆款手势舞全流程丨深度+姿势+边缘控制生成视频_1921087918020968449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【Wan2.1系列】一张照片复刻爆款手势舞全流程丨深度+姿势+边缘控制生成视频_1921087918020968449.json
hash: 2f23334e2650c901
coverage: 0.71875
learned_at: 2026-11-14 01:22:19
nodes: [CLIPVisionLoader, GetNode, WanVideoTeaCache, LoadWanVideoT5TextEncoder, SetNode, GetNode, ImageConcatMulti, WanVideoDecode, GetNode, VHS_VideoCombine, WanVideoExperimentalArgs, WanVideoSampler, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoVAELoader, ImageResizeKJ, Reroute, VHS_VideoCombine, VHS_LoadVideo, LoadImage, WanVideoTextEncode, WanVideoTorchCompileSettings, ImageResizeKJ, AIO_Preprocessor, SetNode, Note, GetImageSizeAndCount, WanVideoEncode, GetNode, WanVideoModelLoader, WanVideoControlEmbeds, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/【Wan2.1系列】一张照片复刻爆款手势舞全流程丨深度+姿势+边缘控制生成视频_1921087918020968449.json

> 来源文件 `comfyui_library/workflows/平台全量/【Wan2.1系列】一张照片复刻爆款手势舞全流程丨深度+姿势+边缘控制生成视频_1921087918020968449.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `ImageResizeKJ`
- `Reroute`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJ`
- `AIO_Preprocessor`
- `SetNode`
- `Note`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoControlEmbeds`
- `MarkdownNote`

## 知识

覆盖率 **72%**（23/32）

**有卡**：`CLIPVisionLoader`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`、`ImageConcatMulti`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`ImageResizeKJ`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`AIO_Preprocessor`、`GetImageSizeAndCount`、`WanVideoEncode`、`WanVideoModelLoader`、`WanVideoControlEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoImageToVideoEncode、WanVideoTextEncode
