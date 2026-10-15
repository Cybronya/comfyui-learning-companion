---
key: 图片生成/文生图/（贞贞版3方式）Qwen Image InstantX Controlnet线稿控制V1_1960723959954247682.json
name: （贞贞版3方式）Qwen Image InstantX Controlnet线稿控制V1_1960723959954247682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（贞贞版3方式）Qwen Image InstantX Controlnet线稿控制V1_1960723959954247682.json
hash: 29dba279a9c41ef7
coverage: 0.789474
learned_at: 2026-10-10 21:00:01
nodes: [CLIPTextEncode, EmptySD3LatentImage, CLIPLoader, VAELoader, UNETLoader, ControlNetApplySD3, AIO_Preprocessor, PreviewImage, SeedVR2BlockSwap, PreviewImage, SaveImage, PreviewImage, KSampler, PreviewImage, KSampler, PreviewImage, ModelSamplingAuraFlow, ControlNetLoader, VAEDecode, VAEDecode, SeedVR2GGUF, Image Compare (mtb), PreviewImage, SetUnionControlNetType, SaveLatent, ImageConcanate, LoraLoaderModelOnly, KSampler, SaveImage, LoraLoaderModelOnly, CLIPTextEncode, PreviewImage, CFGNorm, LoraLoaderModelOnly, ImageConcatMulti, ModelSamplingAuraFlow, VAEDecode, LoadImage]
patterns: []
missing: [Image Compare (mtb)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 0.75, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 397623419622816, "steps": 12}
discoveries: [次要节点 `Image Compare (mtb)` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/（贞贞版3方式）Qwen Image InstantX Controlnet线稿控制V1_1960723959954247682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（贞贞版3方式）Qwen Image InstantX Controlnet线稿控制V1_1960723959954247682.json`

## 结构

**节点**（38 个）：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `ControlNetApplySD3`
- `AIO_Preprocessor`
- `PreviewImage`
- `SeedVR2BlockSwap`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `KSampler`
- `PreviewImage`
- `KSampler`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `ControlNetLoader`
- `VAEDecode`
- `VAEDecode`
- `SeedVR2GGUF`
- `Image Compare (mtb)`
- `PreviewImage`
- `SetUnionControlNetType`
- `SaveLatent`
- `ImageConcanate`
- `LoraLoaderModelOnly`
- `KSampler`
- `SaveImage`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `PreviewImage`
- `CFGNorm`
- `LoraLoaderModelOnly`
- `ImageConcatMulti`
- `ModelSamplingAuraFlow`
- `VAEDecode`
- `LoadImage`

## 关键参数

- `cfg` = `1`
- `controlnet_strength` = `0.75`
- `denoise` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `seed` = `397623419622816`
- `steps` = `12`

## 知识

覆盖率 **79%**（30/38）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ControlNetApplySD3`、`AIO_Preprocessor`、`PreviewImage`、`SeedVR2BlockSwap`、`SaveImage`、`KSampler`、`ModelSamplingAuraFlow`、`ControlNetLoader`、`VAEDecode`、`SeedVR2GGUF`、`Image Compare (mtb)`、`SetUnionControlNetType`、`SaveLatent`、`ImageConcanate`、`LoraLoaderModelOnly`

**缺卡**（1）：`Image Compare (mtb)`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Image Compare (mtb)` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
