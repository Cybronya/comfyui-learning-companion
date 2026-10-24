---
key: 图片生成/图生图/wan_2.2_lora测试_1987912331852230657.json
name: wan_2.2_lora测试_1987912331852230657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan_2.2_lora测试_1987912331852230657.json
hash: dc9fae8e7f1ae67f
coverage: 0.78
learned_at: 2026-10-23 11:46:15
nodes: [VAELoader, CLIPTextEncode, ModelSamplingSD3, CLIPLoader, LayerUtility: TextJoin, Reroute, easy getNode, easy ifElse, easy getNode, VAEDecode, Reroute, ImageConcanate, EmptyHunyuanLatentVideo, ImpactSwitch, KSamplerAdvanced, easy forLoopEnd, LoraLoaderModelOnly, easy isNone, Reroute, CLIPTextEncode, KSamplerAdvanced, AddLabel, ImpactSwitch, SimpleMath+, easy forLoopStart, ImpactSwitch, CR Text, CR Text, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, Reroute, easy setNode, SaveImage, LoadImage, Qwen3_VQA, CR Text, CR Text, easy showAnything, PrimitiveInt, easy setNode, Note]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/wan_2.2_lora测试_1987912331852230657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan_2.2_lora测试_1987912331852230657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `LayerUtility: TextJoin`
- `Reroute`
- `easy getNode`
- `easy ifElse`
- `easy getNode`
- `VAEDecode` ★核心
- `Reroute`
- `ImageConcanate`
- `EmptyHunyuanLatentVideo`
- `ImpactSwitch`
- `KSamplerAdvanced` ★核心
- `easy forLoopEnd`
- `LoraLoaderModelOnly` ★核心
- `easy isNone`
- `Reroute`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `AddLabel`
- `ImpactSwitch`
- `SimpleMath+`
- `easy forLoopStart`
- `ImpactSwitch`
- `CR Text`
- `CR Text`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Reroute`
- `easy setNode`
- `SaveImage`
- `LoadImage`
- `Qwen3_VQA`
- `CR Text`
- `CR Text`
- `easy showAnything`
- `PrimitiveInt`
- `easy setNode`
- `Note`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（39/50）

**有卡**：`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`CLIPLoader`、`LayerUtility: TextJoin`、`easy getNode`、`VAEDecode`、`ImageConcanate`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`easy forLoopEnd`、`LoraLoaderModelOnly`、`easy isNone`、`AddLabel`、`SimpleMath+`、`easy forLoopStart`、`CR Text`、`UNETLoader`、`easy setNode`、`SaveImage`、`LoadImage`、`Qwen3_VQA`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
