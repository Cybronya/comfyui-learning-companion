---
key: 视频生成/图生视频/wan2.2图生视频_1957436481176530945.json
name: wan2.2图生视频_1957436481176530945.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频_1957436481176530945.json
hash: 8ee56929a966708f
coverage: 0.58
learned_at: 2026-10-15 22:31:16
nodes: [Anything Everywhere, Anything Everywhere, Anything Everywhere, PlaySound|pysssss, Anything Everywhere, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, Divide [DVB], SetNode, Anything Everywhere, GetNode, GetNode, GetNode, JWInteger, DownloadAndLoadFlorence2Model, Florence2Run, GetNode, VHS_VideoCombine, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoImageToVideoEncode, mxSlider, mxSlider, WanVideoDecode, WanVideoSampler, WanVideoBlockSwap, WanVideoTorchCompileSettings, GetNode, WanVideoSampler, GetNode, SetNode, SetNode, GetNode, ImageResize+, SetNode, SetNode, GetNode, WanVideoSetBlockSwap, GetNode, WanVideoSetBlockSwap, GetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Textbox, WanVideoEnhanceAVideo, LoadImage, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频_1957436481176530945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957436481176530945.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（50 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `PlaySound|pysssss`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `Divide [DVB]`
- `SetNode`
- `Anything Everywhere`
- `GetNode`
- `GetNode`
- `GetNode`
- `JWInteger`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `mxSlider`
- `mxSlider`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResize+`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `Textbox`
- `WanVideoEnhanceAVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **58%**（29/50）

**有卡**：`PlaySound|pysssss`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`Divide [DVB]`、`JWInteger`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`mxSlider`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`ImageResize+`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`Textbox`、`WanVideoEnhanceAVideo`、`LoadImage`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoSetLoRAs
