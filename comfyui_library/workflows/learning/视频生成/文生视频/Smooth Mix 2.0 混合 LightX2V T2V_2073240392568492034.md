---
key: 视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json
name: Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json
hash: ef3ce1906a983e15
coverage: 0.904762
learned_at: 2026-10-15 22:47:00
nodes: [LayerUtility: PurgeVRAM, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, CLIPLoader, Note, VHS_VideoCombine, CR Prompt Text, UNETLoader, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, VAELoader, JWInteger, JWInteger, JWInteger, WanImageToVideo, PrimitiveNode, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
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

覆盖率 **90%**（19/21）

**有卡**：`LayerUtility: PurgeVRAM`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`CLIPLoader`、`VHS_VideoCombine`、`CR Prompt Text`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`JWInteger`、`WanImageToVideo`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CR Prompt Text
