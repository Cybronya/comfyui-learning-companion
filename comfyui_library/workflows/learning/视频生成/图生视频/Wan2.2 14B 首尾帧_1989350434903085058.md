---
key: 视频生成/图生视频/Wan2.2 14B 首尾帧_1989350434903085058.json
name: Wan2.2 14B 首尾帧_1989350434903085058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1989350434903085058.json
hash: 5528cdc2782d8428
coverage: 0.954545
learned_at: 2026-10-15 22:33:06
nodes: [UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, CLIPTextEncode, VAELoader, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VAEDecode, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, easy imageConcat, ShowText|pysssss, CLIPTextEncode, LoadImage, LoadImage, RH_LLMAPI_NODE, WanFirstLastFrameToVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B 首尾帧_1989350434903085058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989350434903085058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy imageConcat`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `WanFirstLastFrameToVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`easy imageConcat`、`LoadImage`、`RH_LLMAPI_NODE`、`WanFirstLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
