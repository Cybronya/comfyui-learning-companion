---
key: 平台全量/Wan2.2-电商带货工作流_2083946345920028673.json
name: Wan2.2-电商带货工作流_2083946345920028673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-电商带货工作流_2083946345920028673.json
hash: e40848a9637442ca
coverage: 0.779661
learned_at: 2026-11-14 01:06:08
nodes: [ModelSamplingSD3, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, SetNode, SetNode, VAELoader, SetNode, CLIPVisionEncode, MathExpression|pysssss, GetNode, GetNode, CLIPVisionLoader, Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), CLIPLoader, SetNode, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, RIFE VFI, easy getNode, easy getNode, CLIPTextEncode, easy positive, MultiTextConcatenate, Text, ttN concat, PainterI2V, easy cleanGpuUsed, VHS_VideoCombine, ImpactInt, LoadImage, RH_Utils, VHS_VideoCombine, GetNode, WanMoeKSampler, easy setNode, easy cleanGpuUsed, llama_cpp_model_loader, SeedGeneratorMira, SetNode, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, UNETLoader, easy cleanGpuUsed, ShowText|pysssss, MarkdownNote, VAEDecode, CLIPTextEncode, Int, Text, PathchSageAttentionKJ, ModelPatchTorchSettings, llama_cpp_parameters, llama_cpp_instruct_adv, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 平台全量/Wan2.2-电商带货工作流_2083946345920028673.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-电商带货工作流_2083946345920028673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（59 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPVisionEncode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `SetNode`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `RIFE VFI`
- `easy getNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy positive`
- `MultiTextConcatenate`
- `Text`
- `ttN concat`
- `PainterI2V`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `ImpactInt`
- `LoadImage`
- `RH_Utils`
- `VHS_VideoCombine`
- `GetNode`
- `WanMoeKSampler` ★核心
- `easy setNode`
- `easy cleanGpuUsed`
- `llama_cpp_model_loader`
- `SeedGeneratorMira`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `MarkdownNote`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `Text`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `easy showAnything`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **78%**（46/59）

**有卡**：`ModelSamplingSD3`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`VAELoader`、`CLIPVisionEncode`、`MathExpression|pysssss`、`CLIPVisionLoader`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`LoraLoaderModelOnly`、`RIFE VFI`、`easy getNode`、`CLIPTextEncode`、`easy positive`、`MultiTextConcatenate`、`Text`、`ttN concat`、`PainterI2V`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`ImpactInt`、`LoadImage`、`RH_Utils`、`WanMoeKSampler`、`easy setNode`、`llama_cpp_model_loader`、`SeedGeneratorMira`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`VAEDecode`、`Int`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、SeedGeneratorMira
