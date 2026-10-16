---
key: 视频生成/图生视频/图生视频 Wan2.2 Lightx2v-I2V Moe模型，速度质量高性价比_1978318259030253569.json
name: 图生视频 Wan2.2 Lightx2v-I2V Moe模型，速度质量高性价比_1978318259030253569.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1978318259030253569.json
hash: 88c4ffa82c30bbf6
coverage: 0.777778
learned_at: 2026-10-15 22:32:18
nodes: [VAELoader, CLIPLoader, KSamplerAdvanced, ModelSamplingSD3, VAEDecode, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, LoadImage, Int, Int, SetNode, SetNode, SetNode, Int, GetNode, GetNode, GetNode, SimpleMath+, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, MuyeTextEditOutput, VHS_VideoCombine, ModelSamplingSD3, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频 Wan2.2 Lightx2v-I2V Moe模型，速度质量高性价比_1978318259030253569.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978318259030253569.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（27 个）：
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `LoadImage`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MuyeTextEditOutput`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（21/27）

**有卡**：`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`WanImageToVideo`、`LoadImage`、`Int`、`SimpleMath+`、`UNETLoader`、`LoraLoaderModelOnly`、`MuyeTextEditOutput`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
