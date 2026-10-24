---
key: 图片生成/图生图/sd1.5 极简的更换背景及扩图_1924455780525723649.json
name: sd1.5 极简的更换背景及扩图_1924455780525723649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/sd1.5 极简的更换背景及扩图_1924455780525723649.json
hash: f0b5b1679724cd09
coverage: 0.894737
learned_at: 2026-10-23 11:44:52
nodes: [InvertMask, easy imageRemBg, easy imageInterrogator, easy preSampling, easy a1111Loader, easy preSampling, easy loadImageBase64, easy a1111Loader, RH_Translator, easy kSamplerInpainting, LoadImage, easy kSamplerInpainting, ImagePadForOutpaint, SaveImage, easy imageConcat, SaveImage, easy imageConcat, PreviewImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/sd1.5 极简的更换背景及扩图_1924455780525723649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/sd1.5 极简的更换背景及扩图_1924455780525723649.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `InvertMask`
- `easy imageRemBg`
- `easy imageInterrogator`
- `easy preSampling`
- `easy a1111Loader`
- `easy preSampling`
- `easy loadImageBase64`
- `easy a1111Loader`
- `RH_Translator`
- `easy kSamplerInpainting` ★核心
- `LoadImage`
- `easy kSamplerInpainting` ★核心
- `ImagePadForOutpaint`
- `SaveImage`
- `easy imageConcat`
- `SaveImage`
- `easy imageConcat`
- `PreviewImage`
- `PreviewImage`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`InvertMask`、`easy imageRemBg`、`easy imageInterrogator`、`easy preSampling`、`easy a1111Loader`、`easy loadImageBase64`、`RH_Translator`、`easy kSamplerInpainting`、`LoadImage`、`ImagePadForOutpaint`、`SaveImage`、`easy imageConcat`

**用到的条目**：LoadImage、easy kSamplerInpainting、SaveImage、ImagePadForOutpaint、InvertMask、RH_Translator、easy imageConcat、easy imageRemBg
