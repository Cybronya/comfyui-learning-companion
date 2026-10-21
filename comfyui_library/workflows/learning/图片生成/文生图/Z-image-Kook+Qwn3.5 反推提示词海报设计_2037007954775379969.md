---
key: 图片生成/文生图/Z-image-Kook+Qwn3.5 反推提示词海报设计_2037007954775379969.json
name: Z-image-Kook+Qwn3.5 反推提示词海报设计_2037007954775379969
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-Kook+Qwn3.5 反推提示词海报设计_2037007954775379969.json
hash: 2a93847516144757
coverage: 0.904762
learned_at: 2026-10-21 02:56:13
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, KSampler, CLIPTextEncode, CLIPLoader, VAELoader, LoraLoaderModelOnly, VAEDecode, ShowText|pysssss, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, FastFilmGrain, LayerColor: BrightnessContrastV2, SaveImage, EmptyLatentImage, MarkdownNote, CR Text, CR Text, CR Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1472, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1234, "steps": 8, "width": 1104}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image-Kook+Qwn3.5 反推提示词海报设计_2037007954775379969.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-Kook+Qwn3.5 反推提示词海报设计_2037007954775379969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `FastFilmGrain`
- `LayerColor: BrightnessContrastV2`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `CR Text`
- `CR Text`
- `CR Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1234`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1104`
- `height` = `1472`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSampler`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`FastFilmGrain`、`LayerColor: BrightnessContrastV2`、`SaveImage`、`EmptyLatentImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
