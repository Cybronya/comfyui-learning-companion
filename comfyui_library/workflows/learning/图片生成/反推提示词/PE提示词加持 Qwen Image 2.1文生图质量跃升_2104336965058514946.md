---
key: 图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json
name: PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json
hash: 72940452f190f44a
coverage: 0.818182
learned_at: 2026-10-07 02:40:58
nodes: [CLIPLoader, UNETLoader, VAELoader, QwenImage21Cache, KSampler, VAEDecode, easy cleanGpuUsed, EmptyLatentImage, SaveImage, easy showAnything, QwenPERewriteT8, CR Prompt Text, TextEncodeQwenImage21, ComfySwitchNode, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [easy cleanGpuUsed, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/PE提示词加持 Qwen Image 2.1文生图质量跃升_2104336965058514946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `easy showAnything`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ResolutionSelector`
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

覆盖率 **82%**（36/44）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
