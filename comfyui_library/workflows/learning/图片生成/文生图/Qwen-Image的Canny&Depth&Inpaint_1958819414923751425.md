---
key: 图片生成/文生图/Qwen-Image的Canny&Depth&Inpaint_1958819414923751425.json
name: Qwen-Image的Canny&Depth&Inpaint_1958819414923751425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image的Canny&Depth&Inpaint_1958819414923751425.json
hash: 5795ec5c5eaaf67e
coverage: 0.839286
learned_at: 2026-10-10 20:59:04
nodes: [CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, SaveImage, VAEDecode, easy seed, ModelPatchLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, KSampler, LoadImage, ImageResizeKJv2, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, easy seed, QwenImageDiffsynthControlnet, LoraLoaderModelOnly, ModelSamplingAuraFlow, KSampler, EmptySD3LatentImage, ImageResizeKJv2, PreviewImage, ModelPatchLoader, AIO_Preprocessor, LoadImage, String Literal, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, easy seed, QwenImageDiffsynthControlnet, LoraLoaderModelOnly, ModelSamplingAuraFlow, KSampler, EmptySD3LatentImage, ImageResizeKJv2, ModelPatchLoader, String Literal, SaveImage, SaveImage, String Literal, PreviewImage, PreviewImage, EmptySD3LatentImage, LoadImage, AIO_Preprocessor, QwenImageDiffsynthControlnet]
patterns: []
missing: [String Literal, String Literal, String Literal, easy seed, easy seed, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 344619176881199, "steps": 8}
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image的Canny&Depth&Inpaint_1958819414923751425.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image的Canny&Depth&Inpaint_1958819414923751425.json`

## 结构

**节点**（56 个）：
- `CLIPTextEncode`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `SaveImage`
- `VAEDecode`
- `easy seed`
- `ModelPatchLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `KSampler`
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPTextEncode`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `VAEDecode`
- `easy seed`
- `QwenImageDiffsynthControlnet`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `KSampler`
- `EmptySD3LatentImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `ModelPatchLoader`
- `AIO_Preprocessor`
- `LoadImage`
- `String Literal`
- `CLIPTextEncode`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `VAEDecode`
- `easy seed`
- `QwenImageDiffsynthControlnet`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `KSampler`
- `EmptySD3LatentImage`
- `ImageResizeKJv2`
- `ModelPatchLoader`
- `String Literal`
- `SaveImage`
- `SaveImage`
- `String Literal`
- `PreviewImage`
- `PreviewImage`
- `EmptySD3LatentImage`
- `LoadImage`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `344619176881199`
- `steps` = `8`

## 知识

覆盖率 **84%**（47/56）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`VAEDecode`、`easy seed`、`ModelPatchLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`KSampler`、`LoadImage`、`ImageResizeKJv2`、`QwenImageDiffsynthControlnet`、`EmptySD3LatentImage`、`PreviewImage`、`AIO_Preprocessor`、`String Literal`

**缺卡**（6）：`String Literal`、`String Literal`、`String Literal`、`easy seed`、`easy seed`、`easy seed`

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
