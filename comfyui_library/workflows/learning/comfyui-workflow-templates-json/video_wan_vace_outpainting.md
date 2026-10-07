---
key: comfyui-workflow-templates-json/video_wan_vace_outpainting.json
name: video_wan_vace_outpainting
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_vace_outpainting.json
hash: 4f76d56c3f6f4912
official: true
coverage: 0.647059
learned_at: 2026-10-07 21:37:23
nodes: [CreateVideo, ModelSamplingSD3, UNETLoader, LoraLoader, WanVaceToVideo, MarkdownNote, TrimVideoLatent, VAEDecode, MaskToImage, RepeatImageBatch, ImageToMask, LoadVideo, PrimitiveInt, CLIPLoader, VAELoader, ImagePadForOutpaint, GetVideoComponents, UNETLoader, CLIPLoader, PrimitiveInt, MarkdownNote, PrimitiveInt, CLIPTextEncode, CLIPTextEncode, PreviewImage, SaveVideo, LoraLoader, KSampler, PreviewImage, Note, Note, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan21_CausVid_14B_T2V_lora_rank32.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 776767434080331, "steps": 3, "strength_clip": 1, "strength_model": 0.4000000000000001}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# comfyui-workflow-templates-json/video_wan_vace_outpainting.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_vace_outpainting.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CreateVideo`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `WanVaceToVideo`
- `MarkdownNote`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `MaskToImage`
- `RepeatImageBatch`
- `ImageToMask`
- `LoadVideo`
- `PrimitiveInt`
- `CLIPLoader`
- `VAELoader`
- `ImagePadForOutpaint`
- `GetVideoComponents`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveInt`
- `MarkdownNote`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `SaveVideo`
- `LoraLoader` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `Note`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Wan21_CausVid_14B_T2V_lora_rank32.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `1`
- `seed` = `776767434080331`
- `steps` = `3`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（22/34）

**有卡**：`CreateVideo`、`ModelSamplingSD3`、`UNETLoader`、`LoraLoader`、`WanVaceToVideo`、`TrimVideoLatent`、`VAEDecode`、`MaskToImage`、`RepeatImageBatch`、`ImageToMask`、`LoadVideo`、`CLIPLoader`、`VAELoader`、`ImagePadForOutpaint`、`GetVideoComponents`、`CLIPTextEncode`、`SaveVideo`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、TrimVideoLatent、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
