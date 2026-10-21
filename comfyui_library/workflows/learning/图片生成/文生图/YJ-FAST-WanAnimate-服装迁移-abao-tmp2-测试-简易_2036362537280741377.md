---
key: 图片生成/文生图/YJ-FAST-WanAnimate-服装迁移-abao-tmp2-测试-简易_2036362537280741377.json
name: YJ-FAST-WanAnimate-服装迁移-abao-tmp2-测试-简易_2036362537280741377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/YJ-FAST-WanAnimate-服装迁移-abao-tmp2-测试-简易_2036362537280741377.json
hash: 66af7c5fc30c2c22
coverage: 0.604167
learned_at: 2026-10-21 02:55:28
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoSetLoRAs, Reroute, Reroute, WanVideoVAELoader, WanVideoTorchCompileSettings, Reroute, Reroute, WanVideoTextEncodeCached, WanVideoBlockSwap, WanVideoModelLoader, Reroute, WanVideoContextOptions, WanVideoSampler, Reroute, WanVideoDecode, Reroute, CLIPVisionLoader, WanVideoClipVisionEncode, Reroute, WanVideoSetBlockSwap, DrawMaskOnImage, PreviewImage, RMBG, ImageResizeKJv2, JjkText, WanVideoLoraSelectMulti, easy int, WujiCleaner, RIFE VFI, WanVideoAnimateEmbeds, VHS_LoadVideo, VHS_LoadVideo, ImageToMask, VHS_LoadVideo, LoadImage, INTConstant, INTConstant, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/文生图/YJ-FAST-WanAnimate-服装迁移-abao-tmp2-测试-简易_2036362537280741377.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/YJ-FAST-WanAnimate-服装迁移-abao-tmp2-测试-简易_2036362537280741377.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoSetLoRAs`
- `Reroute`
- `Reroute`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `Reroute`
- `Reroute`
- `WanVideoTextEncodeCached`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `Reroute`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `Reroute`
- `WanVideoDecode`
- `Reroute`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Reroute`
- `WanVideoSetBlockSwap`
- `DrawMaskOnImage`
- `PreviewImage`
- `RMBG`
- `ImageResizeKJv2`
- `JjkText`
- `WanVideoLoraSelectMulti`
- `easy int`
- `WujiCleaner`
- `RIFE VFI`
- `WanVideoAnimateEmbeds`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `ImageToMask`
- `VHS_LoadVideo`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **60%**（29/48）

**有卡**：`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncodeCached`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`DrawMaskOnImage`、`RMBG`、`ImageResizeKJv2`、`WanVideoLoraSelectMulti`、`easy int`、`WujiCleaner`、`RIFE VFI`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`ImageToMask`、`LoadImage`、`INTConstant`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
