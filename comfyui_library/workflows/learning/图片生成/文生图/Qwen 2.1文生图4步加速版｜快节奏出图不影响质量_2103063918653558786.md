---
key: 图片生成/文生图/Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786.json
name: Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786.json
hash: 2cc4e663c6eadfe1
coverage: 0.864407
learned_at: 2026-10-10 20:58:50
nodes: [TextEncodeQwenImage21, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, SaveImage, EmptyLatentImage, QwenImage21Cache, VAEDecode, easy cleanGpuUsed, CR Prompt Text, ResolutionSelector, QwenPERewriteT8, easy showAnything, ComfySwitchNode, KSampler, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [easy cleanGpuUsed, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786.json`

## 结构

**节点**（59 个）：
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `EmptyLatentImage`
- `QwenImage21Cache`
- `VAEDecode`
- `easy cleanGpuUsed`
- `CR Prompt Text`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `easy showAnything`
- `ComfySwitchNode`
- `KSampler`
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

覆盖率 **86%**（51/59）

**有卡**：`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`EmptyLatentImage`、`QwenImage21Cache`、`VAEDecode`、`easy cleanGpuUsed`、`CR Prompt Text`、`ResolutionSelector`、`QwenPERewriteT8`、`easy showAnything`、`ComfySwitchNode`、`KSampler`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
