---
key: 平台全量/Wan2.2 animate 动作迁移KJ版_1976818662579621890.json
name: Wan2.2 animate 动作迁移KJ版_1976818662579621890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 animate 动作迁移KJ版_1976818662579621890.json
hash: 12236ba1501bc131
coverage: 0.956522
learned_at: 2026-11-14 01:05:37
nodes: [Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSampler, CLIPVisionLoader, ImageResizeKJv2, INTConstant, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoSetBlockSwap, INTConstant, INTConstant, WanVideoDecode, VHS_VideoCombine, WanVideoClipVisionEncode, SimpleMath+, PixelPerfectResolution, WanVideoVAELoader, WanVideoAnimateEmbeds, DWPreprocessor, VHS_LoadVideo, LoadImage, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 平台全量/Wan2.2 animate 动作迁移KJ版_1976818662579621890.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 animate 动作迁移KJ版_1976818662579621890.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（23 个）：
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `INTConstant`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `SimpleMath+`
- `PixelPerfectResolution`
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSampler`、`CLIPVisionLoader`、`ImageResizeKJv2`、`INTConstant`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`SimpleMath+`、`PixelPerfectResolution`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`DWPreprocessor`、`VHS_LoadVideo`、`LoadImage`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、CLIPVisionLoader
