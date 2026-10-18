---
key: 视频生成/图生视频/Radial加速+Lightx2v-Rank128 V2.0增强细节视频生成_2021501136443805698.json
name: Radial加速+Lightx2v-Rank128 V2.0增强细节视频生成_2021501136443805698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Radial加速+Lightx2v-Rank128 V2.0增强细节视频生成_2021501136443805698.json
hash: c734bba59bc9ebd2
coverage: 0.83871
learned_at: 2026-10-15 22:35:08
nodes: [WanVideoTorchCompileSettings, WanVideoEnhanceAVideo, ShowText, WanVideoDecode, WanVideoTextEncode, Primitive integer [Crystools], Note, Note, Note, WanVideoSampler, WanVideoFreeInitArgs, Text Multiline, WanVideoLoraSelect, CLIPVisionLoader, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, WanVideoSetRadialAttention, ImageResizeKJv2, Primitive integer [Crystools], Primitive integer [Crystools], Fast Groups Bypasser (rgthree), LoadImage, WanVideoClipVisionEncode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoExperimentalArgs, VHS_VideoCombine, Primitive integer [Crystools], Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Radial加速+Lightx2v-Rank128 V2.0增强细节视频生成_2021501136443805698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021501136443805698.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoEnhanceAVideo`
- `ShowText`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `Primitive integer [Crystools]`
- `Note`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoFreeInitArgs`
- `Text Multiline`
- `WanVideoLoraSelect`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSetRadialAttention`
- `ImageResizeKJv2`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `WanVideoClipVisionEncode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `Note`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoEnhanceAVideo`、`ShowText`、`WanVideoDecode`、`WanVideoTextEncode`、`Primitive integer [Crystools]`、`WanVideoSampler`、`WanVideoFreeInitArgs`、`Text Multiline`、`WanVideoLoraSelect`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSetRadialAttention`、`ImageResizeKJv2`、`LoadImage`、`WanVideoClipVisionEncode`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
