---
key: 图片生成/文生图/Qwen Image Edit -  Pose Studio + Camera-RH工作流_2022300481946656770.json
name: Qwen Image Edit -  Pose Studio + Camera-RH工作流_2022300481946656770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image Edit -  Pose Studio + Camera-RH工作流_2022300481946656770.json
hash: 0a75791d9fbcc063
coverage: 0.785714
learned_at: 2026-10-19 22:29:47
nodes: [CLIPLoader, CFGNorm, TextEncodeQwenImageEditPlus, LoaderGGUF, ShowText|pysssss, Note, Any Switch (rgthree), TextEncodeQwenImageEditPlus, StringConcatenate, UNETLoader, Note, LoraLoaderModelOnly, ModelSamplingAuraFlow, LoraLoaderModelOnly, VAELoader, EmptySD3LatentImage, VAEDecode, LoadImage, PreviewImage, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, Note, KSampler, VNCCS_VisualPositionControl, VNCCS_PoseStudio, VNCCS_QWEN_Detailer, UltralyticsDetectorProvider, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 42, "steps": 12}
---

# 图片生成/文生图/Qwen Image Edit -  Pose Studio + Camera-RH工作流_2022300481946656770.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image Edit -  Pose Studio + Camera-RH工作流_2022300481946656770.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPLoader`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `LoaderGGUF`
- `ShowText|pysssss`
- `Note`
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `StringConcatenate`
- `UNETLoader` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `LoadImage`
- `PreviewImage`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `Note`
- `KSampler` ★核心
- `VNCCS_VisualPositionControl`
- `VNCCS_PoseStudio`
- `VNCCS_QWEN_Detailer`
- `UltralyticsDetectorProvider`
- `SaveImage`

## 关键参数

- `seed` = `42`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`CLIPLoader`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`LoaderGGUF`、`StringConcatenate`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`VAELoader`、`EmptySD3LatentImage`、`VAEDecode`、`LoadImage`、`FluxKontextMultiReferenceLatentMethod`、`KSampler`、`VNCCS_VisualPositionControl`、`VNCCS_PoseStudio`、`VNCCS_QWEN_Detailer`、`UltralyticsDetectorProvider`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
