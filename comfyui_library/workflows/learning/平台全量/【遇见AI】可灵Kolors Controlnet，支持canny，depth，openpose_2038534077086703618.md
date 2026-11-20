---
key: 平台全量/【遇见AI】可灵Kolors Controlnet，支持canny，depth，openpose_2038534077086703618.json
name: 【遇见AI】可灵Kolors Controlnet，支持canny，depth，openpose_2038534077086703618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【遇见AI】可灵Kolors Controlnet，支持canny，depth，openpose_2038534077086703618.json
hash: 347366f11dc7042c
coverage: 0.928571
learned_at: 2026-11-14 01:25:38
nodes: [CannyEdgePreprocessor, PreviewImage, EmptyLatentImage, KSampler, VAEDecode, SaveImage, MZ_ChatGLM3_V2, MZ_ChatGLM3_V2, ControlNetApplySD3, MZ_KolorsUNETLoaderV2, MZ_ChatGLM3Loader, VAELoader, MZ_KolorsControlNetLoader, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "karras", "seed": 335514688138251, "steps": 20, "width": 768}
---

# 平台全量/【遇见AI】可灵Kolors Controlnet，支持canny，depth，openpose_2038534077086703618.json

> 来源文件 `comfyui_library/workflows/平台全量/【遇见AI】可灵Kolors Controlnet，支持canny，depth，openpose_2038534077086703618.json`

## 结构

**生成流程**：Model → Latent → Control → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CannyEdgePreprocessor`
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `MZ_ChatGLM3_V2`
- `MZ_ChatGLM3_V2`
- `ControlNetApplySD3` ★核心
- `MZ_KolorsUNETLoaderV2` ★核心
- `MZ_ChatGLM3Loader`
- `VAELoader`
- `MZ_KolorsControlNetLoader`
- `LoadImage`

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `335514688138251`
- `steps` = `20`
- `cfg` = `4.5`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CannyEdgePreprocessor`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`MZ_ChatGLM3_V2`、`ControlNetApplySD3`、`MZ_KolorsUNETLoaderV2`、`MZ_ChatGLM3Loader`、`VAELoader`、`MZ_KolorsControlNetLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、EmptyLatentImage、LoadImage、CannyEdgePreprocessor、ControlNetApplySD3、MZ_KolorsControlNetLoader
