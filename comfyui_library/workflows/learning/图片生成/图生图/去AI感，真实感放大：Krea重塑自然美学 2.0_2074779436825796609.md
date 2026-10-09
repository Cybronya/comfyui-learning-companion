---
key: 图片生成/图生图/去AI感，真实感放大：Krea重塑自然美学 2.0_2074779436825796609.json
name: 去AI感，真实感放大：Krea重塑自然美学 2.0_2074779436825796609.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/去AI感，真实感放大：Krea重塑自然美学 2.0_2074779436825796609.json
hash: 29db156649052a53
coverage: 0.5
learned_at: 2026-10-09 22:36:21
nodes: [Image Comparer (rgthree), Note, Note, Note, Note, Note, Note, VAELoader, SaveImage, PrimitiveFloat, PrimitiveFloat, Int, UNETLoader_Any, KSampler, SaveImage, PreviewImage, PreviewImage, PreviewImage, SaveImage, PreviewImage, SaveImage, easy boolean, Int, PrimitiveFloat, RHHiddenNodes, easy ifElse, RHHiddenNodes, Int, Int, PrimitiveFloat, VAEEncode, CLIPTextEncode, VAEDecode, KuwaharaBlur, VAEDecode, easy cleanGpuUsed, CLIPLoader, easy cleanGpuUsed, DisTorchPurgeVRAMV2, llama_cpp_instruct_adv, easy showAnything, llama_cpp_model_loader, GroupExecutor, CR Text, CLIPTextEncode, LoraLoaderModelOnly, ImageResize+, LoadImage, KSamplerAdvanced, easy imageColorMatch, LayerColor: RGB, LayerColor: Color of Shadow & Highlight, LayerColor: Color of Shadow & Highlight, easy imageColorMatch]
patterns: [image_to_image]
missing: [CR Text, LayerColor: Color of Shadow & Highlight, LayerColor: Color of Shadow & Highlight, LayerColor: RGB, easy boolean, easy cleanGpuUsed, easy cleanGpuUsed, easy imageColorMatch, easy imageColorMatch, ImageResize+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 8, "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: Color of Shadow & Highlight` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: Color of Shadow & Highlight` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: RGB` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/去AI感，真实感放大：Krea重塑自然美学 2.0_2074779436825796609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2074779436825796609.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `VAELoader`
- `SaveImage`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `Int`
- `UNETLoader_Any` ★核心
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `easy boolean`
- `Int`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `easy ifElse`
- `RHHiddenNodes`
- `Int`
- `Int`
- `PrimitiveFloat`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KuwaharaBlur`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `DisTorchPurgeVRAMV2`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `llama_cpp_model_loader`
- `GroupExecutor`
- `CR Text`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResize+`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `easy imageColorMatch`
- `LayerColor: RGB`
- `LayerColor: Color of Shadow & Highlight`
- `LayerColor: Color of Shadow & Highlight`
- `easy imageColorMatch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **50%**（27/54）

**有卡**：`VAELoader`、`SaveImage`、`Int`、`UNETLoader_Any`、`KSampler`、`RHHiddenNodes`、`VAEEncode`、`CLIPTextEncode`、`VAEDecode`、`KuwaharaBlur`、`CLIPLoader`、`DisTorchPurgeVRAMV2`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`GroupExecutor`、`LoraLoaderModelOnly`、`LoadImage`、`KSamplerAdvanced`

**缺卡**（10）：`CR Text`、`LayerColor: Color of Shadow & Highlight`、`LayerColor: Color of Shadow & Highlight`、`LayerColor: RGB`、`easy boolean`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageColorMatch`、`easy imageColorMatch`、`ImageResize+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: Color of Shadow & Highlight` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: Color of Shadow & Highlight` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: RGB` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
