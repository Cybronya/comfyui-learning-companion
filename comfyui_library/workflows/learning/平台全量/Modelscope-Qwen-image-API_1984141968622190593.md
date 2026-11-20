---
key: 平台全量/Modelscope-Qwen-image-API_1984141968622190593.json
name: Modelscope-Qwen-image-API_1984141968622190593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Modelscope-Qwen-image-API_1984141968622190593.json
hash: 90936cdff65c3196
coverage: 0.863636
learned_at: 2026-11-14 00:46:29
nodes: [SaveImage, GetImageSize+, ImageConcanate, SaveImage, QwenVisionNode, ShowText|pysssss, QwenImageNode, easy string, MarkdownNote, WanVideoSetLoRAs, WanVideoSetBlockSwap, MathExpression|pysssss, ttN int, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, ttN int, ttN int, WanVideoEmptyEmbeds, WanVideoDecode, LayerColor: Brightness & Contrast, WanVideoBlockSwap, CreateCFGScheduleFloatList, ttN int, ttN int, WanVideoTorchCompileSettings, WanVideoVAELoader, ShowText|pysssss, QwenVideoNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, easy cleanGpuUsed, easy cleanGpuUsed, PrimitiveNode, Note, LoadWanVideoT5TextEncoder, WanVideoTextEncode, VHS_VideoCombine, LoadImage, Fast Groups Bypasser (rgthree), LoadVideo, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 平台全量/Modelscope-Qwen-image-API_1984141968622190593.json

> 来源文件 `comfyui_library/workflows/平台全量/Modelscope-Qwen-image-API_1984141968622190593.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `SaveImage`
- `GetImageSize+`
- `ImageConcanate`
- `SaveImage`
- `QwenVisionNode`
- `ShowText|pysssss`
- `QwenImageNode`
- `easy string`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `MathExpression|pysssss`
- `ttN int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `ttN int`
- `ttN int`
- `WanVideoEmptyEmbeds`
- `WanVideoDecode`
- `LayerColor: Brightness & Contrast`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `ttN int`
- `ttN int`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `ShowText|pysssss`
- `QwenVideoNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PrimitiveNode`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadVideo`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **86%**（38/44）

**有卡**：`SaveImage`、`GetImageSize+`、`ImageConcanate`、`QwenVisionNode`、`QwenImageNode`、`easy string`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`MathExpression|pysssss`、`ttN int`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`WanVideoDecode`、`LayerColor: Brightness & Contrast`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`QwenVideoNode`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`VHS_VideoCombine`、`LoadImage`、`LoadVideo`、`WanVideoModelLoader`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
