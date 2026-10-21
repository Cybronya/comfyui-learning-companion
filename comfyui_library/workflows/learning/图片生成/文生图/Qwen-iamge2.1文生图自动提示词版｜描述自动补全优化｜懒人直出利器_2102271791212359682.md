---
key: 图片生成/文生图/Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682.json
name: Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682.json
hash: 977dd9ab7275131a
coverage: 0.887097
learned_at: 2026-10-20 01:51:18
nodes: [UNETLoader, SaveImage, QwenImage21Cache, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, ConditioningZeroOut, KSampler, CLIPTextEncode, llama_cpp_instruct_adv, ResolutionSelector, llama_cpp_model_loader, ShowText|pysssss, CR Prompt Text, CLIPLoader, ShowText|pysssss, TextGenerateLTX2Prompt, PreviewImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-iamge2.1文生图自动提示词版｜描述自动补全优化｜懒人直出利器_2102271791212359682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（62 个）：
- `UNETLoader` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `ResolutionSelector`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `CR Prompt Text`
- `CLIPLoader`
- `ShowText|pysssss`
- `TextGenerateLTX2Prompt`
- `PreviewImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（55/62）

**有卡**：`UNETLoader`、`SaveImage`、`QwenImage21Cache`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`ConditioningZeroOut`、`KSampler`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`ResolutionSelector`、`llama_cpp_model_loader`、`CR Prompt Text`、`TextGenerateLTX2Prompt`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
