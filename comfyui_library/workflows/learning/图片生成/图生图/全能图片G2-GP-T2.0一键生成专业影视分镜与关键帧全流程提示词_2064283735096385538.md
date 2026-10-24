---
key: 图片生成/图生图/全能图片G2-GP-T2.0一键生成专业影视分镜与关键帧全流程提示词_2064283735096385538.json
name: 全能图片G2-GP-T2.0一键生成专业影视分镜与关键帧全流程提示词_2064283735096385538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全能图片G2-GP-T2.0一键生成专业影视分镜与关键帧全流程提示词_2064283735096385538.json
hash: 3e6d308252b6bf57
coverage: 0.709677
learned_at: 2026-10-23 12:15:39
nodes: [PrimitiveInt, ttN concat, ttN concat, Any To String (mtb), Any To String (mtb), ttN concat, RTXVideoSuperResolution, PreviewImage, SaveImage, ttN concat, ttN concat, Fast Groups Bypasser (rgthree), PrimitiveFloat, llama_cpp_instruct_adv, easy saveText, RH_RhartImageG2OfficialImageToImage, MultiTextConcatenate, PrimitiveStringMultiline, llama_cpp_model_loader, RH_RhartImageG2ImageToImage, PrimitiveInt, ImageLoader, PrimitiveStringMultiline, CR String To Combo, RTXVideoSuperResolution, PreviewImage, SaveImage, PreviewAny, llama_cpp_parameters, RHHiddenNodes, PDRatioSelector]
patterns: []
missing: []
---

# 图片生成/图生图/全能图片G2-GP-T2.0一键生成专业影视分镜与关键帧全流程提示词_2064283735096385538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/全能图片G2-GP-T2.0一键生成专业影视分镜与关键帧全流程提示词_2064283735096385538.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（31 个）：
- `PrimitiveInt`
- `ttN concat`
- `ttN concat`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `ttN concat`
- `RTXVideoSuperResolution`
- `PreviewImage`
- `SaveImage`
- `ttN concat`
- `ttN concat`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveFloat`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `RH_RhartImageG2OfficialImageToImage`
- `MultiTextConcatenate`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `RH_RhartImageG2ImageToImage`
- `PrimitiveInt`
- `ImageLoader`
- `PrimitiveStringMultiline`
- `CR String To Combo`
- `RTXVideoSuperResolution`
- `PreviewImage`
- `SaveImage`
- `PreviewAny`
- `llama_cpp_parameters`
- `RHHiddenNodes`
- `PDRatioSelector`

## 知识

覆盖率 **71%**（22/31）

**有卡**：`ttN concat`、`Any To String (mtb)`、`RTXVideoSuperResolution`、`SaveImage`、`llama_cpp_instruct_adv`、`easy saveText`、`RH_RhartImageG2OfficialImageToImage`、`MultiTextConcatenate`、`llama_cpp_model_loader`、`RH_RhartImageG2ImageToImage`、`ImageLoader`、`CR String To Combo`、`llama_cpp_parameters`、`RHHiddenNodes`、`PDRatioSelector`

**用到的条目**：RTXVideoSuperResolution、SaveImage、easy saveText、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、MultiTextConcatenate、RH_RhartImageG2ImageToImage
