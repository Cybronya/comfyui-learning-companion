---
key: 视频生成/图生视频/Qwen Image 2.1参考人物姿势，图生视频姿势参考生成方案_2103578331991068673.json
name: Qwen Image 2.1参考人物姿势，图生视频姿势参考生成方案_2103578331991068673
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1参考人物姿势，图生视频姿势参考生成方案_2103578331991068673.json
hash: 8e2b6ecdbceb1556
coverage: 0.857143
learned_at: 2026-10-17 02:29:16
nodes: [QwenImage21Cache, UNETLoader, CLIPLoader, CR Prompt Text, VAEDecode, easy cleanGpuUsed, KSampler, SaveImage, QwenPERewriteT8, easy showAnything, TextEncodeQwenImage21, ComfySwitchNode, EmptyLatentImage, LoadImage, ResolutionSelector, LoadImage, VAELoader, AIO_Preprocessor, EmptyImage, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen Image 2.1参考人物姿势，图生视频姿势参考生成方案_2103578331991068673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1参考人物姿势，图生视频姿势参考生成方案_2103578331991068673.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `SaveImage`
- `QwenPERewriteT8`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `VAELoader`
- `AIO_Preprocessor`
- `EmptyImage`
- `PreviewImage`
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

覆盖率 **86%**（42/49）

**有卡**：`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`CR Prompt Text`、`VAEDecode`、`easy cleanGpuUsed`、`KSampler`、`SaveImage`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`LoadImage`、`ResolutionSelector`、`VAELoader`、`AIO_Preprocessor`、`EmptyImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
