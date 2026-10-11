---
key: 视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json
name: Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json
hash: ef3ce1906a983e15
coverage: 0.809524
learned_at: 2026-10-11 20:38:42
nodes: [LayerUtility: PurgeVRAM, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, CLIPLoader, Note, VHS_VideoCombine, CR Prompt Text, UNETLoader, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, VAELoader, JWInteger, JWInteger, JWInteger, WanImageToVideo, PrimitiveNode, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: [LayerUtility: PurgeVRAM, CR Prompt Text]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPLoader`
- `Note`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanImageToVideo`
- `PrimitiveNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`CLIPLoader`、`VHS_VideoCombine`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`JWInteger`、`WanImageToVideo`、`LoraLoaderModelOnly`

**缺卡**（2）：`LayerUtility: PurgeVRAM`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、ModelSamplingSD3

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
