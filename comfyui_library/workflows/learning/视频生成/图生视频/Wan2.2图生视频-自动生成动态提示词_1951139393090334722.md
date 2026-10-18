---
key: 视频生成/图生视频/Wan2.2图生视频-自动生成动态提示词_1951139393090334722.json
name: Wan2.2图生视频-自动生成动态提示词_1951139393090334722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频-自动生成动态提示词_1951139393090334722.json
hash: 13da263c01109c65
coverage: 0.857143
learned_at: 2026-10-15 22:30:57
nodes: [WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoSetLoRAs, SimpleMath+, MarkdownNote, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, Note, easy showAnything, Text Concatenate, LoadWanVideoT5TextEncoder, WanVideoTextEncode, Int, Int, WanVideoLoraSelect, WanVideoLoraSelect, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, RH_Captioner, Wan22PromptSelector, VHS_VideoCombine, easy showAnything, RH_LLMAPI_NODE, easy int, LoadImage, Text Multiline, WanVideoSampler, WanVideoSampler, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频-自动生成动态提示词_1951139393090334722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951139393090334722.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `SimpleMath+`
- `MarkdownNote`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `Note`
- `easy showAnything`
- `Text Concatenate`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `Int`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Captioner`
- `Wan22PromptSelector`
- `VHS_VideoCombine`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `easy int`
- `LoadImage`
- `Text Multiline`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Int`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`SimpleMath+`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`Text Concatenate`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`Int`、`WanVideoLoraSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Captioner`、`Wan22PromptSelector`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`、`easy int`、`LoadImage`、`Text Multiline`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
