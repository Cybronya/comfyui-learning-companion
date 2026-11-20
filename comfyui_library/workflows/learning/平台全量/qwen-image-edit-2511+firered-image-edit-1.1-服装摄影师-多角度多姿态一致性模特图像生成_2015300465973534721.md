---
key: 平台全量/qwen-image-edit-2511+firered-image-edit-1.1-服装摄影师-多角度多姿态一致性模特图像生成_2015300465973534721.json
name: qwen-image-edit-2511+firered-image-edit-1.1-服装摄影师-多角度多姿态一致性模特图像生成_2015300465973534721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image-edit-2511+firered-image-edit-1.1-服装摄影师-多角度多姿态一致性模特图像生成_2015300465973534721.json
hash: 571b8a4d04425625
coverage: 0.804878
learned_at: 2026-11-14 01:16:17
nodes: [ModelSamplingAuraFlow, CFGNorm, TextEncodeQwenImageEditPlus, CLIPLoader, TextEncodeQwenImageEditPlus, SeedVR2LoadVAEModel, VAEEncode, VAELoader, SeedVR2LoadDiTModel, DetailDaemonSamplerNode, ProcessString, ProcessString, JDCN_StringToList, ImageScaleToTotalPixelsX, ImageScaleToTotalPixelsX, BasicScheduler, LoraLoaderModelOnly, easy int, CheckpointLoaderSimple, UNETLoader, easy int, easy ifElse, easy cleanGpuUsed, KSamplerSelect, SeedVR2VideoUpscaler, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, easy ifElse, easy cleanGpuUsed, Note, SamplerCustom, LoadImage, PrimitiveNode, SaveImage, PrimitiveNode, Note, easy promptReplace, AILab_QwenVL, ShowText|pysssss, CR Text, PreviewImage]
patterns: []
missing: []
parameters: {"checkpoint": "Qwen-Rapid-AIO-NSFW-v20.safetensors"}
---

# 平台全量/qwen-image-edit-2511+firered-image-edit-1.1-服装摄影师-多角度多姿态一致性模特图像生成_2015300465973534721.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image-edit-2511+firered-image-edit-1.1-服装摄影师-多角度多姿态一致性模特图像生成_2015300465973534721.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
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
- `ImageScaleToTotalPixelsX`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `easy int`
- `easy ifElse`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `SeedVR2VideoUpscaler`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy ifElse`
- `easy cleanGpuUsed`
- `Note`
- `SamplerCustom` ★核心
- `LoadImage`
- `PrimitiveNode`
- `SaveImage`
- `PrimitiveNode`
- `Note`
- `easy promptReplace`
- `AILab_QwenVL`
- `ShowText|pysssss`
- `CR Text`
- `PreviewImage`

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v20.safetensors`

## 知识

覆盖率 **80%**（33/41）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`SeedVR2LoadVAEModel`、`VAEEncode`、`VAELoader`、`SeedVR2LoadDiTModel`、`DetailDaemonSamplerNode`、`ProcessString`、`JDCN_StringToList`、`ImageScaleToTotalPixelsX`、`BasicScheduler`、`LoraLoaderModelOnly`、`easy int`、`CheckpointLoaderSimple`、`UNETLoader`、`easy cleanGpuUsed`、`KSamplerSelect`、`SeedVR2VideoUpscaler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustom`、`LoadImage`、`SaveImage`、`easy promptReplace`、`AILab_QwenVL`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、LoadImage、CFGNorm
