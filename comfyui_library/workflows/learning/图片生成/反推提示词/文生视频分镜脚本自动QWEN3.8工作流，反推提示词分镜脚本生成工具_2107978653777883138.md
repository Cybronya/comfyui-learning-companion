---
key: 图片生成/反推提示词/文生视频分镜脚本自动QWEN3.8工作流，反推提示词分镜脚本生成工具_2107978653777883138.json
name: 文生视频分镜脚本自动QWEN3.8工作流，反推提示词分镜脚本生成工具_2107978653777883138
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/文生视频分镜脚本自动QWEN3.8工作流，反推提示词分镜脚本生成工具_2107978653777883138.json
hash: 0992b0183345e51f
coverage: 0.868421
learned_at: 2026-10-26 01:48:18
nodes: [SaveImage, LoadImage, RH_Translator, LoadImage, easy saveText, CR Prompt Text, MiniMaxH3PromptEnhancerT8, CM_FloatToInt, PreviewAny, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/文生视频分镜脚本自动QWEN3.8工作流，反推提示词分镜脚本生成工具_2107978653777883138.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/文生视频分镜脚本自动QWEN3.8工作流，反推提示词分镜脚本生成工具_2107978653777883138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（38 个）：
- `SaveImage`
- `LoadImage`
- `RH_Translator`
- `LoadImage`
- `easy saveText`
- `CR Prompt Text`
- `MiniMaxH3PromptEnhancerT8`
- `CM_FloatToInt`
- `PreviewAny`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`SaveImage`、`LoadImage`、`RH_Translator`、`easy saveText`、`CR Prompt Text`、`MiniMaxH3PromptEnhancerT8`、`CM_FloatToInt`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
