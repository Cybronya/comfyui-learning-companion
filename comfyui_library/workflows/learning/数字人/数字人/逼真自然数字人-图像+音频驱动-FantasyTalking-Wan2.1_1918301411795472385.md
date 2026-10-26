---
key: 数字人/数字人/逼真自然数字人-图像+音频驱动-FantasyTalking-Wan2.1_1918301411795472385.json
name: 逼真自然数字人-图像+音频驱动-FantasyTalking-Wan2.1_1918301411795472385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/逼真自然数字人-图像+音频驱动-FantasyTalking-Wan2.1_1918301411795472385.json
hash: 2911aa219563731a
coverage: 0.962963
learned_at: 2026-10-26 02:05:48
nodes: [WanVideoClipVisionEncode, PreviewImage, FantasyTalkingWav2VecEmbeds, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, CLIPVisionLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTorchCompileSettings, INTConstant, WanVideoDecode, VHS_VideoCombine, WanVideoVAELoader, LoadAudio, WanVideoModelLoader, LoadWanVideoT5TextEncoder, ImageResizeKJ, LoadImage, WanVideoBlockSwap, INTConstant, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, WanVideoContextOptions, WanVideoTextEncode]
patterns: []
missing: []
---

# 数字人/数字人/逼真自然数字人-图像+音频驱动-FantasyTalking-Wan2.1_1918301411795472385.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/逼真自然数字人-图像+音频驱动-FantasyTalking-Wan2.1_1918301411795472385.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（27 个）：
- `WanVideoClipVisionEncode`
- `PreviewImage`
- `FantasyTalkingWav2VecEmbeds`
- `CreateCFGScheduleFloatList`
- `WanVideoImageToVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `LoadAudio`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJ`
- `LoadImage`
- `WanVideoBlockSwap`
- `INTConstant`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `WanVideoContextOptions`
- `WanVideoTextEncode`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoClipVisionEncode`、`FantasyTalkingWav2VecEmbeds`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`CLIPVisionLoader`、`WanVideoSampler`、`WanVideoTeaCache`、`WanVideoTorchCompileSettings`、`INTConstant`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`LoadAudio`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJ`、`LoadImage`、`WanVideoBlockSwap`、`DownloadAndLoadWav2VecModel`、`FantasyTalkingModelLoader`、`WanVideoContextOptions`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
