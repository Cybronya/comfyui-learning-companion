---
key: 图片生成/图生图/超写实 8K 高清摄影 Qwe edit-2511+firered edit-1.1 服装摄影 多角_2043143536920502274.json
name: 超写实 8K 高清摄影 Qwe edit-2511+firered edit-1.1 服装摄影 多角_2043143536920502274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/超写实 8K 高清摄影 Qwe edit-2511+firered edit-1.1 服装摄影 多角_2043143536920502274.json
hash: c05e9d8c678607f4
coverage: 0.825
learned_at: 2026-10-23 13:28:30
nodes: [ModelSamplingAuraFlow, CFGNorm, TextEncodeQwenImageEditPlus, CLIPLoader, TextEncodeQwenImageEditPlus, SeedVR2LoadVAEModel, VAEEncode, VAELoader, SeedVR2LoadDiTModel, DetailDaemonSamplerNode, ProcessString, ProcessString, JDCN_StringToList, ImageScaleToTotalPixelsX, CR Text, ImageScaleToTotalPixelsX, BasicScheduler, easy int, UNETLoader, easy int, easy cleanGpuUsed, KSamplerSelect, SeedVR2VideoUpscaler, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, AILab_QwenVL, SamplerCustom, ShowText|pysssss, PreviewImage, SaveImage, easy ifElse, LoraLoaderModelOnly, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), LoadImage, PrimitiveNode, PrimitiveNode, easy promptReplace, easy ifElse]
patterns: []
missing: []
parameters: {"checkpoint": "Qwen-Rapid-AIO-NSFW-v20.safetensors"}
---

# 图片生成/图生图/超写实 8K 高清摄影 Qwe edit-2511+firered edit-1.1 服装摄影 多角_2043143536920502274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/超写实 8K 高清摄影 Qwe edit-2511+firered edit-1.1 服装摄影 多角_2043143536920502274.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `SeedVR2LoadVAEModel`
- `VAEEncode` ★核心
- `VAELoader`
- `SeedVR2LoadDiTModel`
- `DetailDaemonSamplerNode` ★核心
- `ProcessString`
- `ProcessString`
- `JDCN_StringToList`
- `ImageScaleToTotalPixelsX`
- `CR Text`
- `ImageScaleToTotalPixelsX`
- `BasicScheduler`
- `easy int`
- `UNETLoader` ★核心
- `easy int`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `SeedVR2VideoUpscaler`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `AILab_QwenVL`
- `SamplerCustom` ★核心
- `ShowText|pysssss`
- `PreviewImage`
- `SaveImage`
- `easy ifElse`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `easy promptReplace`
- `easy ifElse`

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v20.safetensors`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`SeedVR2LoadVAEModel`、`VAEEncode`、`VAELoader`、`SeedVR2LoadDiTModel`、`DetailDaemonSamplerNode`、`ProcessString`、`JDCN_StringToList`、`ImageScaleToTotalPixelsX`、`CR Text`、`BasicScheduler`、`easy int`、`UNETLoader`、`easy cleanGpuUsed`、`KSamplerSelect`、`SeedVR2VideoUpscaler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_QwenVL`、`SamplerCustom`、`SaveImage`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LoadImage`、`easy promptReplace`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、LoadImage、CFGNorm
