---
key: 图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json
name: Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json
hash: 5a97a558b0144677
coverage: 0.859649
learned_at: 2026-10-06 22:37:16
nodes: [LoadImage, LoadBackgroundRemovalModel, RemoveBackground, InvertMask, ComfySwitchNode, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, TripoSplatConditioning, KSampler, VAEDecodeTripoSplat, SplatToFile3D, SaveGLB, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SaveImage, Load3D, SaveImage, TripoSplatPreprocessImage, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Load3D, SplatToFile3D, SaveGLB]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Load3D` 知识库中没有该节点类型的任何知识, 次要节点 `SplatToFile3D` 知识库中没有该节点类型的任何知识, 次要节点 `SaveGLB` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
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
- `TripoSplatPreprocessImage`
- `SaveImage`
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

覆盖率 **86%**（49/57）

**有卡**：`LoadImage`、`LoadBackgroundRemovalModel`、`RemoveBackground`、`InvertMask`、`UNETLoader`、`CLIPVisionLoader`、`VAELoader`、`TripoSplatConditioning`、`KSampler`、`VAEDecodeTripoSplat`、`CLIPLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`TripoSplatPreprocessImage`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（3）：`Load3D`、`SplatToFile3D`、`SaveGLB`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Load3D` 知识库中没有该节点类型的任何知识
- 次要节点 `SplatToFile3D` 知识库中没有该节点类型的任何知识
- 次要节点 `SaveGLB` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
