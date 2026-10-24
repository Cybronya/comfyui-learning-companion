---
key: 图片生成/图生图/wan2.2洗图工作流_1968904972467359746.json
name: wan2.2洗图工作流_1968904972467359746
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2洗图工作流_1968904972467359746.json
hash: 7ff04455d6752108
coverage: 1
learned_at: 2026-10-23 11:46:08
nodes: [LayerUtility: ImageReel, CLIPTextEncode, LoraLoader, VAELoader, LayerUtility: ImageReelComposit, PathchSageAttentionKJ, VAEDecode, VAEEncode, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoader, LoraLoader, CLIPLoader, UNETLoader, LoadImage, CLIPTextEncode, SaveImage, SaveImage, KSampler]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1057147919958636, "steps": 20, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
---

# 图片生成/图生图/wan2.2洗图工作流_1968904972467359746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2洗图工作流_1968904972467359746.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `LayerUtility: ImageReel`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `VAELoader`
- `LayerUtility: ImageReelComposit`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `1057147919958636`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`LayerUtility: ImageReel`、`CLIPTextEncode`、`LoraLoader`、`VAELoader`、`LayerUtility: ImageReelComposit`、`PathchSageAttentionKJ`、`VAEDecode`、`VAEEncode`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStarAndInit
