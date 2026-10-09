---
key: 图片生成/文生图/🈚️qwen canny_depth + z-image 深度_线稿参考 图生图重绘_1958960960541241345.json
name: 🈚️qwen canny_depth + z-image 深度_线稿参考 图生图重绘_1958960960541241345.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/🈚️qwen canny_depth + z-image 深度_线稿参考 图生图重绘_1958960960541241345.json
hash: d30b5fab3081710b
coverage: 0.546512
learned_at: 2026-10-07 23:31:46
nodes: [VAELoader, SetNode, SetNode, AIO_Preprocessor, AIO_Preprocessor, LayerUtility: ImageScaleByAspectRatio V2, RepeatLatentBatch, ModelPatchLoader, ModelPatchLoader, GetNode, RH_Translator, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, PreviewImage, RH_LLMAPI_NODE, RH_LLMAPI_NODE, easy imageRemBg, ShowText|pysssss, CLIPTextEncode, GetNode, SetNode, LoadImage, ImpactSwitch, ImpactSwitch, LoadImage, CLIPTextEncode, ConditioningZeroOut, VAEDecode, CLIPLoader, VAELoader, VAEEncode, RebatchLatents, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, RepeatLatentBatch, KSampler, SetNode, GetNode, LoraLoaderModelOnly, SetNode, GetNode, SetNode, JWInteger, SetNode, easy seed, SetNode, JWInteger, SetNode, GetNode, GetNode, GetNode, Note, RebatchLatents, QwenImageDiffsynthControlnet, GetNode, EmptyLatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGNorm, ModelSamplingAuraFlow, UNETLoader, ImpactSwitch, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, GetNode, GetNode, Anything Everywhere3, CLIPLoader, CFGZeroStar, ModelPassThrough, CLIPTextEncode, ConditioningZeroOut, LoraLoaderModelOnly, GetNode, Int, PreviewImage, SaveImage, KSamplerSelect, DetailDaemonSamplerNode, BasicScheduler, SamplerCustom]
patterns: [text_to_image, image_to_image]
missing: [CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, easy cleanGpuUsed, easy imageRemBg, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.3500000000000001, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 1030454734910631, "steps": 4, "width": 512}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/🈚️qwen canny_depth + z-image 深度_线稿参考 图生图重绘_1958960960541241345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1958960960541241345.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `VAELoader`
- `SetNode`
- `SetNode`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatLatentBatch`
- `ModelPatchLoader`
- `ModelPatchLoader`
- `GetNode`
- `RH_Translator`
- `CR Text Concatenate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `easy imageRemBg`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `LoadImage`
- `ImpactSwitch`
- `ImpactSwitch`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `RebatchLatents`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatLatentBatch`
- `KSampler` ★核心
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `JWInteger`
- `SetNode`
- `easy seed`
- `SetNode`
- `JWInteger`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `RebatchLatents`
- `QwenImageDiffsynthControlnet`
- `GetNode`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `ImpactSwitch`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `Anything Everywhere3`
- `CLIPLoader`
- `CFGZeroStar`
- `ModelPassThrough`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `Int`
- `PreviewImage`
- `SaveImage`
- `KSamplerSelect` ★核心
- `DetailDaemonSamplerNode` ★核心
- `BasicScheduler`
- `SamplerCustom` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `1030454734910631`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.3500000000000001`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（47/86）

**有卡**：`VAELoader`、`AIO_Preprocessor`、`RepeatLatentBatch`、`ModelPatchLoader`、`RH_Translator`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`LoadImage`、`ConditioningZeroOut`、`VAEDecode`、`CLIPLoader`、`VAEEncode`、`RebatchLatents`、`UNETLoader`、`KSampler`、`LoraLoaderModelOnly`、`JWInteger`、`QwenImageDiffsynthControlnet`、`EmptyLatentImage`、`CFGNorm`、`ModelSamplingAuraFlow`、`CFGZeroStar`、`ModelPassThrough`、`Int`、`SaveImage`、`KSamplerSelect`、`DetailDaemonSamplerNode`、`BasicScheduler`、`SamplerCustom`

**缺卡**（9）：`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageRemBg`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageRemBg` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
