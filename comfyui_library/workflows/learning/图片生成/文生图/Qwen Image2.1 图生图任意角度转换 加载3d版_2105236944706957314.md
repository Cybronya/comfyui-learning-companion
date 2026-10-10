---
key: Qwen Image2.1 图生图任意角度转换 加载3d版_2105236944706957314.json
name: Qwen Image2.1 图生图任意角度转换 加载3d版_2105236944706957314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图生图任意角度转换 加载3d版_2105236944706957314.json
hash: b53e212a4de0da6c
coverage: 0.9
learned_at: 2026-10-10 20:58:55
nodes: [LoadImage, LoadBackgroundRemovalModel, RemoveBackground, InvertMask, ComfySwitchNode, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, TripoSplatConditioning, KSampler, VAEDecodeTripoSplat, SplatToFile3D, SaveGLB, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SaveImage, Load3D, SaveImage, MarkdownNote, MarkdownNote, TripoSplatPreprocessImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20260930, "steps": 24}
---

# Qwen Image2.1 图生图任意角度转换 加载3d版_2105236944706957314.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图生图任意角度转换 加载3d版_2105236944706957314.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `LoadImage`
- `LoadBackgroundRemovalModel`
- `RemoveBackground`
- `InvertMask`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `TripoSplatConditioning`
- `KSampler` ★核心
- `VAEDecodeTripoSplat` ★核心
- `SplatToFile3D`
- `SaveGLB`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Load3D`
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `TripoSplatPreprocessImage`
- `SaveImage`

## 关键参数

- `seed` = `20260930`
- `steps` = `24`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`LoadImage`、`LoadBackgroundRemovalModel`、`RemoveBackground`、`InvertMask`、`UNETLoader`、`CLIPVisionLoader`、`VAELoader`、`TripoSplatConditioning`、`KSampler`、`VAEDecodeTripoSplat`、`SplatToFile3D`、`SaveGLB`、`CLIPLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`Load3D`、`TripoSplatPreprocessImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
