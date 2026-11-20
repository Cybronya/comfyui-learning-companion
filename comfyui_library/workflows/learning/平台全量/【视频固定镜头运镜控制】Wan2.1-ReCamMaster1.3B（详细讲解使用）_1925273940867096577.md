---
key: 平台全量/【视频固定镜头运镜控制】Wan2.1-ReCamMaster1.3B（详细讲解使用）_1925273940867096577.json
name: 【视频固定镜头运镜控制】Wan2.1-ReCamMaster1.3B（详细讲解使用）_1925273940867096577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【视频固定镜头运镜控制】Wan2.1-ReCamMaster1.3B（详细讲解使用）_1925273940867096577.json
hash: 55e88d110805f01a
coverage: 0.772727
learned_at: 2026-11-14 01:25:09
nodes: [Anything Everywhere, WanVideoVAELoader, Anything Everywhere, Anything Everywhere, LoadWanVideoT5TextEncoder, VHS_LoadVideo, WanVideoSampler, WanVideoDecode, WanVideoExperimentalArgs, CogVideoEnhanceAVideo, WanVideoSLG, RH_Captioner, ShowText|pysssss, WanVideoBlockSwap, WanVideoTorchCompileSettings, ImageResize+, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTeaCache, Note, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, PreviewImage, Note, WanVideoReCamMasterDefaultCamera, WanVideoReCamMasterDefaultCamera, WanVideoReCamMasterDefaultCamera, WanVideoReCamMasterDefaultCamera, WanVideoReCamMasterDefaultCamera, WanVideoReCamMasterDefaultCamera, WanVideoReCamMasterDefaultCamera, WanVideoReCamMasterDefaultCamera, WanVideoReCamMasterDefaultCamera, WanVideoReCamMasterDefaultCamera, WanVideoModelLoader, ImpactSwitch, ReCamMasterPoseVisualizer, WanVideoVACEEncode, WanVideoEncode, WanVideoReCamMasterCameraEmbed, VHS_VideoCombine, Note, Int, Note]
patterns: []
missing: []
---

# 平台全量/【视频固定镜头运镜控制】Wan2.1-ReCamMaster1.3B（详细讲解使用）_1925273940867096577.json

> 来源文件 `comfyui_library/workflows/平台全量/【视频固定镜头运镜控制】Wan2.1-ReCamMaster1.3B（详细讲解使用）_1925273940867096577.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `Anything Everywhere`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `RH_Captioner`
- `ShowText|pysssss`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `ImageResize+`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `Note`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`
- `Note`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoModelLoader`
- `ImpactSwitch`
- `ReCamMasterPoseVisualizer`
- `WanVideoVACEEncode`
- `WanVideoEncode`
- `WanVideoReCamMasterCameraEmbed`
- `VHS_VideoCombine`
- `Note`
- `Int`
- `Note`

## 知识

覆盖率 **77%**（34/44）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`VHS_LoadVideo`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`RH_Captioner`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`ImageResize+`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoVACEModelSelect`、`WanVideoVACEStartToEndFrame`、`WanVideoReCamMasterDefaultCamera`、`WanVideoModelLoader`、`ReCamMasterPoseVisualizer`、`WanVideoVACEEncode`、`WanVideoEncode`、`WanVideoReCamMasterCameraEmbed`、`VHS_VideoCombine`、`Int`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、ImageResize+
