---
key: comfyui-workflow-templates-json/video_wan_vace_14B_v2v.json
name: video_wan_vace_14B_v2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_vace_14B_v2v.json
hash: c190961990c76696
official: true
coverage: 0.75
learned_at: 2026-10-07 21:37:22
nodes: [CreateVideo, KSampler, ModelSamplingSD3, UNETLoader, VAELoader, MarkdownNote, TrimVideoLatent, VAEDecode, SaveAnimatedWEBP, UNETLoader, LoraLoader, CLIPLoader, CLIPLoader, WanVaceToVideo, SaveVideo, PreviewImage, GetVideoComponents, Canny, MarkdownNote, LoraLoader, CLIPTextEncode, CLIPTextEncode, MarkdownNote, MarkdownNote, MarkdownNote, LoadVideo, LoadImage, MarkdownNote]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan21_CausVid_14B_T2V_lora_rank32.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 654654950714624, "steps": 4, "strength_clip": 1, "strength_model": 0.30000000000000004}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# comfyui-workflow-templates-json/video_wan_vace_14B_v2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_vace_14B_v2v.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（28 个）：
- `CreateVideo`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `VAELoader`
- `MarkdownNote`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `SaveAnimatedWEBP`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `WanVaceToVideo`
- `SaveVideo`
- `PreviewImage`
- `GetVideoComponents`
- `Canny`
- `MarkdownNote`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadVideo`
- `LoadImage`
- `MarkdownNote`

**识别到的模式**：lora

## 关键参数

- `seed` = `654654950714624`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Wan21_CausVid_14B_T2V_lora_rank32.safetensors`
- `strength_model` = `0.30000000000000004`
- `strength_clip` = `1`

## 知识

覆盖率 **75%**（21/28）

**有卡**：`CreateVideo`、`KSampler`、`ModelSamplingSD3`、`UNETLoader`、`VAELoader`、`TrimVideoLatent`、`VAEDecode`、`SaveAnimatedWEBP`、`LoraLoader`、`CLIPLoader`、`WanVaceToVideo`、`SaveVideo`、`GetVideoComponents`、`Canny`、`CLIPTextEncode`、`LoadVideo`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Canny

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
