---
key: 图片生成/文生图/wan2.2超真实+批量文生图（自动提示词）V4_2033193785663954945.json
name: wan2.2超真实+批量文生图（自动提示词）V4_2033193785663954945
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2超真实+批量文生图（自动提示词）V4_2033193785663954945.json
hash: e820f0dfffef427b
coverage: 0.875
learned_at: 2026-10-21 02:57:40
nodes: [LoraLoader, CLIPTextEncode, CLIPLoader, VAELoader, CFGZeroStarAndInit, CR Text Concatenate, EmptyLatentImage, KSampler, VAEDecode, RH_LLMAPI_NODE, ShowText|pysssss, UNETLoader, ShowText|pysssss, LoraLoader, CLIPTextEncode, LoraLoader, Wan_video_prompt_generator, RHHiddenNodes, JWInteger, JWInteger, RHHiddenNodes, Note, SaveImage, Text Multiline]
patterns: [text_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 512, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 616582925091353, "steps": 8, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.2超真实+批量文生图（自动提示词）V4_2033193785663954945.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2超真实+批量文生图（自动提示词）V4_2033193785663954945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGZeroStarAndInit`
- `CR Text Concatenate`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `Wan_video_prompt_generator`
- `RHHiddenNodes`
- `JWInteger`
- `JWInteger`
- `RHHiddenNodes`
- `Note`
- `SaveImage`
- `Text Multiline`

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `width` = `512`
- `height` = `512`
- `batch_size` = `4`
- `seed` = `616582925091353`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`LoraLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`CFGZeroStarAndInit`、`CR Text Concatenate`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`RH_LLMAPI_NODE`、`UNETLoader`、`Wan_video_prompt_generator`、`RHHiddenNodes`、`JWInteger`、`SaveImage`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CFGZeroStarAndInit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
