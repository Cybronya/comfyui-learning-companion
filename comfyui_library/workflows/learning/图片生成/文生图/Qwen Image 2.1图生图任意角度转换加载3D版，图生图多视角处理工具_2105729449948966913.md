---
key: 图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json
name: Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json
hash: 5a97a558b0144677
coverage: 0.912281
learned_at: 2026-10-10 20:58:52
nodes: [LoadImage, LoadBackgroundRemovalModel, RemoveBackground, InvertMask, ComfySwitchNode, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, TripoSplatConditioning, KSampler, VAEDecodeTripoSplat, SplatToFile3D, SaveGLB, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SaveImage, Load3D, SaveImage, TripoSplatPreprocessImage, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json`

## 结构

**节点**（57 个）：
- `LoadImage`
- `LoadBackgroundRemovalModel`
- `RemoveBackground`
- `InvertMask`
- `ComfySwitchNode`
- `UNETLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `TripoSplatConditioning`
- `KSampler`
- `VAEDecodeTripoSplat`
- `SplatToFile3D`
- `SaveGLB`
- `LoadImage`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `Load3D`
- `SaveImage`
- `TripoSplatPreprocessImage`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
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
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **91%**（52/57）

**有卡**：`LoadImage`、`LoadBackgroundRemovalModel`、`RemoveBackground`、`InvertMask`、`ComfySwitchNode`、`UNETLoader`、`CLIPVisionLoader`、`VAELoader`、`TripoSplatConditioning`、`KSampler`、`VAEDecodeTripoSplat`、`SplatToFile3D`、`SaveGLB`、`CLIPLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`Load3D`、`TripoSplatPreprocessImage`、`孤海注释`、`EmptyLatentImage`、`JjkText`、`CLIPTextEncode`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
