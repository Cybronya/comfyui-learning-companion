---
key: comfyui-workflow-templates-json/video_wan_vace_14B_ref2v.json
name: video_wan_vace_14B_ref2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_vace_14B_ref2v.json
hash: 941f7b1d10674ab5
official: true
coverage: 0.692308
learned_at: 2026-10-10 22:50:48
nodes: [UNETLoader, LoraLoader, CLIPLoader, VAEDecode, CLIPLoader, SaveAnimatedWEBP, TrimVideoLatent, ModelSamplingSD3, SolidMask, ImageToMask, MaskToImage, PreviewImage, PreviewImage, PrimitiveNode, LoadImage, MarkdownNote, PrimitiveNode, PrimitiveNode, VAELoader, SaveVideo, KSampler, CreateVideo, WanVaceToVideo, UNETLoader, LoraLoader, CLIPTextEncode, CLIPTextEncode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, SolidMask, RepeatImageBatch, BatchImagesNode, MaskToImage, BatchImagesNode]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan21_CausVid_14B_T2V_lora_rank32.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 552837504311715, "steps": 4, "strength_clip": 1, "strength_model": 0.30000000000000004}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# comfyui-workflow-templates-json/video_wan_vace_14B_ref2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_vace_14B_ref2v.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPLoader`
- `SaveAnimatedWEBP`
- `TrimVideoLatent`
- `ModelSamplingSD3`
- `SolidMask`
- `ImageToMask`
- `MaskToImage`
- `PreviewImage`
- `PreviewImage`
- `PrimitiveNode`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAELoader`
- `SaveVideo`
- `KSampler` ★核心
- `CreateVideo`
- `WanVaceToVideo`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `SolidMask`
- `RepeatImageBatch`
- `BatchImagesNode`
- `MaskToImage`
- `BatchImagesNode`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Wan21_CausVid_14B_T2V_lora_rank32.safetensors`
- `strength_model` = `0.30000000000000004`
- `strength_clip` = `1`
- `seed` = `552837504311715`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（27/39）

**有卡**：`UNETLoader`、`LoraLoader`、`CLIPLoader`、`VAEDecode`、`SaveAnimatedWEBP`、`TrimVideoLatent`、`ModelSamplingSD3`、`SolidMask`、`ImageToMask`、`MaskToImage`、`LoadImage`、`VAELoader`、`SaveVideo`、`KSampler`、`CreateVideo`、`WanVaceToVideo`、`CLIPTextEncode`、`RepeatImageBatch`、`BatchImagesNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、TrimVideoLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
