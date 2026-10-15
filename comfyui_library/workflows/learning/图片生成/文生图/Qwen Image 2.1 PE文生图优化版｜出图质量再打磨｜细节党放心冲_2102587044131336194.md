---
key: 图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json
name: Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json
hash: 31dc8441c7c09264
coverage: 0.875
learned_at: 2026-10-10 20:58:51
nodes: [TextEncodeQwenImage21, KSampler, VAEDecode, PreviewAny, PreviewAny, PreviewAny, CLIPLoader, UNETLoader, VAELoader, QwenPECanvasT8, QwenPERewriteT8, QwenImage21Cache, SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json`

## 结构

**节点**（56 个）：
- `TextEncodeQwenImage21`
- `KSampler`
- `VAEDecode`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `CLIPLoader`
- `UNETLoader`
- `VAELoader`
- `QwenPECanvasT8`
- `QwenPERewriteT8`
- `QwenImage21Cache`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **88%**（49/56）

**有卡**：`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`PreviewAny`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`QwenPECanvasT8`、`QwenPERewriteT8`、`QwenImage21Cache`、`SaveImage`、`孤海注释`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`JjkText`、`LoraLoaderModelOnly`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
