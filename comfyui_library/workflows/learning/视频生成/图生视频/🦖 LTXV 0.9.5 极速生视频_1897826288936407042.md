---
key: 视频生成/图生视频/🦖 LTXV 0.9.5 极速生视频_1897826288936407042.json
name: 🦖 LTXV 0.9.5 极速生视频_1897826288936407042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1897826288936407042.json
hash: ae50d24d36e3f79b
coverage: 0.894737
learned_at: 2026-10-15 22:29:19
nodes: [LoadImage, Note, Note, CLIPTextEncode, CLIPTextEncode, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, Bjornulf_ShowStringText, ArgosTranslateTextNode, TextInput_, LTXVImgToVideo, VAEDecode, DeepTranslatorTextNode, CheckpointLoaderSimple, SamplerCustom, LTXVConditioning, VHS_VideoCombine, LTXVScheduler]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-video-2b-v0.9.5.safetensors"}
---

# 视频生成/图生视频/🦖 LTXV 0.9.5 极速生视频_1897826288936407042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1897826288936407042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `LoadImage`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `Bjornulf_ShowStringText`
- `ArgosTranslateTextNode`
- `TextInput_`
- `LTXVImgToVideo`
- `VAEDecode` ★核心
- `DeepTranslatorTextNode`
- `CheckpointLoaderSimple` ★核心
- `SamplerCustom` ★核心
- `LTXVConditioning`
- `VHS_VideoCombine`
- `LTXVScheduler`

## 关键参数

- `checkpoint` = `ltx-video-2b-v0.9.5.safetensors`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`LoadImage`、`CLIPTextEncode`、`KSamplerSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`Bjornulf_ShowStringText`、`ArgosTranslateTextNode`、`TextInput_`、`LTXVImgToVideo`、`VAEDecode`、`DeepTranslatorTextNode`、`CheckpointLoaderSimple`、`SamplerCustom`、`LTXVConditioning`、`VHS_VideoCombine`、`LTXVScheduler`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、LTXVConditioning
