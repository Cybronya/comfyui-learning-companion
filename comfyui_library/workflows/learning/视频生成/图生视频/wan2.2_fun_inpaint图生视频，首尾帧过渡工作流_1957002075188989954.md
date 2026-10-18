---
key: 视频生成/图生视频/wan2.2_fun_inpaint图生视频，首尾帧过渡工作流_1957002075188989954.json
name: wan2.2_fun_inpaint图生视频，首尾帧过渡工作流_1957002075188989954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2_fun_inpaint图生视频，首尾帧过渡工作流_1957002075188989954.json
hash: dfed22df6fe0142b
coverage: 0.857143
learned_at: 2026-10-15 22:31:15
nodes: [CLIPTextEncode, VAELoader, VAEDecode, CLIPTextEncode, VHS_VideoCombine, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, WanFunInpaintToVideo, UNETLoader, VHS_VideoCombine, KSamplerAdvanced, CLIPVisionLoader, KSamplerAdvanced, UNETLoader, UNETLoader, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, WanFunInpaintToVideo, CLIPTextEncode, UNETLoader, CLIPVisionEncode, CLIPLoader, LayerUtility: ImageScaleByAspectRatio, Int, Int, Note, Note, LoadImage, Note, LoadImage, Note, LoadImage, Int, Note, Note, Note, Int, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2_fun_inpaint图生视频，首尾帧过渡工作流_1957002075188989954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957002075188989954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFunInpaintToVideo`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanFunInpaintToVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio`
- `Int`
- `Int`
- `Note`
- `Note`
- `LoadImage`
- `Note`
- `LoadImage`
- `Note`
- `LoadImage`
- `Int`
- `Note`
- `Note`
- `Note`
- `Int`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（42/49）

**有卡**：`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`VHS_VideoCombine`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanFunInpaintToVideo`、`UNETLoader`、`KSamplerAdvanced`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio`、`Int`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
