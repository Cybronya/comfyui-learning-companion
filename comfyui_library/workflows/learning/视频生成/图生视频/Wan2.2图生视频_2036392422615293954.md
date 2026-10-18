---
key: 视频生成/图生视频/Wan2.2图生视频_2036392422615293954.json
name: Wan2.2图生视频_2036392422615293954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频_2036392422615293954.json
hash: f6f4bdcd00e22bf1
coverage: 0.805556
learned_at: 2026-10-15 22:35:52
nodes: [UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, INTConstant, INTConstant, Seed (rgthree), KSamplerAdvanced, KSamplerAdvanced, INTConstant, WanImageToVideo, INTConstant, INTConstant, LoadImage, ImageResize+, SetNode, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, VAEDecode, GetNode, PainterVRAM, RH_LLMAPI_NODE, TextInput_, ShowText|pysssss, SetNode, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LayerUtility: PurgeVRAM V2, SetNode, TextInput_, CR Text, LayerUtility: PurgeVRAM V2, GetNode]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2图生视频_2036392422615293954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036392422615293954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `INTConstant`
- `INTConstant`
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `WanImageToVideo`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `ImageResize+`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `GetNode`
- `PainterVRAM`
- `RH_LLMAPI_NODE`
- `TextInput_`
- `ShowText|pysssss`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `TextInput_`
- `CR Text`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（29/36）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`INTConstant`、`Seed (rgthree)`、`KSamplerAdvanced`、`WanImageToVideo`、`LoadImage`、`ImageResize+`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`PainterVRAM`、`RH_LLMAPI_NODE`、`TextInput_`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
