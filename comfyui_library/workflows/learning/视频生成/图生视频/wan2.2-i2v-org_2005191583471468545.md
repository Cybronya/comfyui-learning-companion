---
key: 视频生成/图生视频/wan2.2-i2v-org_2005191583471468545.json
name: wan2.2-i2v-org_2005191583471468545.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-i2v-org_2005191583471468545.json
hash: 40feef8cbe3a89b8
coverage: 1
learned_at: 2026-10-15 22:33:55
nodes: [CLIPTextEncode, CLIPTextEncode, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, WanFirstLastFrameToVideo, CLIPLoader, VAELoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecodeTiled, VHS_VideoCombine, CR Text, Int, Int, Int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2-i2v-org_2005191583471468545.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005191583471468545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanFirstLastFrameToVideo`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `Int`
- `Int`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CLIPTextEncode`、`LoadImage`、`LoraLoaderModelOnly`、`WanFirstLastFrameToVideo`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecodeTiled`、`VHS_VideoCombine`、`CR Text`、`Int`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、VAEDecodeTiled
