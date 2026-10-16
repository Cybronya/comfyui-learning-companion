---
key: 视频生成/图生视频/Wan2.1-FusionX图生视频_1933737212456390657.json
name: Wan2.1-FusionX图生视频_1933737212456390657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1933737212456390657.json
hash: c08f8b8d4e7ab8f1
coverage: 1
learned_at: 2026-10-15 22:30:14
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoTeaCache, WanVideoTextEncode, WanVideoExperimentalArgs, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, CLIPVisionLoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoEnhanceAVideo, Text Multiline, WanVideoSLG, LoadImage, Primitive integer [Crystools], ImageResizeKJv2, JWInteger, JWInteger, Primitive integer [Crystools]]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-FusionX图生视频_1933737212456390657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1933737212456390657.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `Text Multiline`
- `WanVideoSLG`
- `LoadImage`
- `Primitive integer [Crystools]`
- `ImageResizeKJv2`
- `JWInteger`
- `JWInteger`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoTextEncode`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`Text Multiline`、`WanVideoSLG`、`LoadImage`、`Primitive integer [Crystools]`、`ImageResizeKJv2`、`JWInteger`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
