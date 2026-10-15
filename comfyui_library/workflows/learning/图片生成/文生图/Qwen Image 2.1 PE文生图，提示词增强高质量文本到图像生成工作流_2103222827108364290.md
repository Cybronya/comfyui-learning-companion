---
key: 图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json
name: Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json
hash: 4fbdd33c83fed329
coverage: 0.818182
learned_at: 2026-10-10 20:58:51
nodes: [VAELoader, QwenImage21Cache, QwenPERewriteT8, UNETLoader, CLIPLoader, easy showAnything, ResolutionSelector, VAEDecode, ComfySwitchNode, EmptyLatentImage, CR Prompt Text, KSampler, easy cleanGpuUsed, SaveImage, TextEncodeQwenImage21, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [easy cleanGpuUsed, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json`

## 结构

**节点**（44 个）：
- `VAELoader`
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `UNETLoader`
- `CLIPLoader`
- `easy showAnything`
- `ResolutionSelector`
- `VAEDecode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `CR Prompt Text`
- `KSampler`
- `easy cleanGpuUsed`
- `SaveImage`
- `TextEncodeQwenImage21`
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

覆盖率 **82%**（36/44）

**有卡**：`VAELoader`、`QwenImage21Cache`、`QwenPERewriteT8`、`UNETLoader`、`CLIPLoader`、`easy showAnything`、`ResolutionSelector`、`VAEDecode`、`ComfySwitchNode`、`EmptyLatentImage`、`CR Prompt Text`、`KSampler`、`easy cleanGpuUsed`、`SaveImage`、`TextEncodeQwenImage21`、`孤海注释`、`LoraLoaderModelOnly`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
