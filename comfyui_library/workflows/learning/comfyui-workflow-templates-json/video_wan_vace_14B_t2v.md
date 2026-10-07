---
key: comfyui-workflow-templates-json/video_wan_vace_14B_t2v.json
name: video_wan_vace_14B_t2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_vace_14B_t2v.json
hash: 5618e4122802ff07
official: true
coverage: 0.772727
learned_at: 2026-10-07 21:37:21
nodes: [CreateVideo, KSampler, WanVaceToVideo, ModelSamplingSD3, VAELoader, MarkdownNote, TrimVideoLatent, VAEDecode, SaveAnimatedWEBP, UNETLoader, LoraLoader, CLIPLoader, CLIPLoader, LoraLoader, MarkdownNote, CLIPTextEncode, CLIPTextEncode, SaveVideo, UNETLoader, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan21_CausVid_14B_T2V_lora_rank32.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 675909971186865, "steps": 4, "strength_clip": 1, "strength_model": 0.7000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# comfyui-workflow-templates-json/video_wan_vace_14B_t2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan_vace_14B_t2v.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `CreateVideo`
- `KSampler` ★核心
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `VAELoader`
- `MarkdownNote`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `SaveAnimatedWEBP`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `LoraLoader` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `UNETLoader` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：lora

## 关键参数

- `seed` = `675909971186865`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Wan21_CausVid_14B_T2V_lora_rank32.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `1`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`CreateVideo`、`KSampler`、`WanVaceToVideo`、`ModelSamplingSD3`、`VAELoader`、`TrimVideoLatent`、`VAEDecode`、`SaveAnimatedWEBP`、`UNETLoader`、`LoraLoader`、`CLIPLoader`、`CLIPTextEncode`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、TrimVideoLatent、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
