---
key: 图片生成/图生图/Qwen3VL反推wan2.2I2V_2002507539789037570.json
name: Qwen3VL反推wan2.2I2V_2002507539789037570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen3VL反推wan2.2I2V_2002507539789037570.json
hash: c0313a6e46b452cc
coverage: 0.44
learned_at: 2026-10-23 11:19:56
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Note, CLIPLoader, Note, wanBlockSwap, Reroute, wanBlockSwap, Reroute, Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VHS_VideoCombine, VAEDecode, Note, KSamplerAdvanced, INTConstant, INTConstant, Int, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, Note, Fast Groups Bypasser (rgthree), MultiplePathsInput, KSamplerAdvanced, Reroute, Reroute, UNETLoader, UNETLoader, VAELoader, Qwen3_VQA, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, easy showAnything, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, VHS_VideoCombine, ImageLoader, RIFE VFI, Int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/Qwen3VL反推wan2.2I2V_2002507539789037570.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen3VL反推wan2.2I2V_2002507539789037570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `CLIPLoader`
- `Note`
- `wanBlockSwap`
- `Reroute`
- `wanBlockSwap`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `Int`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `MultiplePathsInput`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `Qwen3_VQA`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `ImageLoader`
- `RIFE VFI`
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **44%**（33/75）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`CLIPLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`MultiplePathsInput`、`UNETLoader`、`VAELoader`、`Qwen3_VQA`、`LoraLoaderModelOnly`、`ImageLoader`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Int
