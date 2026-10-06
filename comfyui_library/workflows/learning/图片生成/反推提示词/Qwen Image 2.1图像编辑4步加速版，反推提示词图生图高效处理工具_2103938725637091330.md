---
key: 图片生成/反推提示词/Qwen Image 2.1图像编辑4步加速版，反推提示词图生图高效处理工具_2103938725637091330.json
name: Qwen Image 2.1图像编辑4步加速版，反推提示词图生图高效处理工具_2103938725637091330
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1图像编辑4步加速版，反推提示词图生图高效处理工具_2103938725637091330.json
hash: 8cc7513b9b95bc04
coverage: 0.355372
learned_at: 2026-10-06 21:36:37
nodes: [SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, VAEEncode, GetNode, GetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, CLIPLoader, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, TextEncodeQwenImage21, GetNode, ImpactNeg, GetNode, DapaoMakeImageBatchNode, llama_cpp_parameters, GetNode, CM_BoolToInt, PrimitiveFloat, CR Text Replace, LayerUtility: PurgeVRAM, SetNode, ComfySwitchNode, easy anythingIndexSwitch, PrimitiveInt, ExecutionBlocker, llama_cpp_instruct_adv, easy seed, KSampler, GetNode, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoadImage, QwenImage21Cache, ImageRGBA2RGB, ImpactNeg, VAELoader, VAEEncode, JsonExtractString, JjkText, SaveLatent, PrimitiveBoolean, PrimitiveBoolean, ExecutionBlocker, VAEDecode, ExecutionBlocker, ExecutionBlocker, SaveImage, SaveImageAdvanced, llama_cpp_model_loader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: [CM_BoolToInt, CR Text Replace, DapaoMakeImageBatchNode, ExecutionBlocker, ExecutionBlocker, ExecutionBlocker, ExecutionBlocker, ImageRGBA2RGB, ImageScaleToTotalPixels, ImpactNeg, ImpactNeg, JsonExtractString, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, PrimitiveBoolean, PrimitiveBoolean, easy anythingIndexSwitch, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, SaveImageAdvanced, SaveLatent, easy seed, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CM_BoolToInt` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `DapaoMakeImageBatchNode` 知识库中没有该节点类型的任何知识, 次要节点 `ExecutionBlocker` 知识库中没有该节点类型的任何知识, 次要节点 `ExecutionBlocker` 知识库中没有该节点类型的任何知识, 次要节点 `ExecutionBlocker` 知识库中没有该节点类型的任何知识, 次要节点 `ExecutionBlocker` 知识库中没有该节点类型的任何知识, 次要节点 `ImageRGBA2RGB` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImpactNeg` 知识库中没有该节点类型的任何知识, 次要节点 `ImpactNeg` 知识库中没有该节点类型的任何知识, 次要节点 `JsonExtractString` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveLatent` 仅有 VAE/SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/Qwen Image 2.1图像编辑4步加速版，反推提示词图生图高效处理工具_2103938725637091330.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1图像编辑4步加速版，反推提示词图生图高效处理工具_2103938725637091330.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（121 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `ImpactNeg`
- `GetNode`
- `DapaoMakeImageBatchNode`
- `llama_cpp_parameters`
- `GetNode`
- `CM_BoolToInt`
- `PrimitiveFloat`
- `CR Text Replace`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `ComfySwitchNode`
- `easy anythingIndexSwitch`
- `PrimitiveInt`
- `ExecutionBlocker`
- `llama_cpp_instruct_adv`
- `easy seed`
- `KSampler` ★核心
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoadImage`
- `QwenImage21Cache`
- `ImageRGBA2RGB`
- `ImpactNeg`
- `VAELoader`
- `VAEEncode` ★核心
- `JsonExtractString`
- `JjkText`
- `SaveLatent`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `ExecutionBlocker`
- `VAEDecode` ★核心
- `ExecutionBlocker`
- `ExecutionBlocker`
- `SaveImage`
- `SaveImageAdvanced`
- `llama_cpp_model_loader`
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

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **36%**（43/121）

**有卡**：`LoadImage`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`KSampler`、`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`

**缺卡**（24）：`CM_BoolToInt`、`CR Text Replace`、`DapaoMakeImageBatchNode`、`ExecutionBlocker`、`ExecutionBlocker`、`ExecutionBlocker`、`ExecutionBlocker`、`ImageRGBA2RGB`、`ImageScaleToTotalPixels`、`ImpactNeg`、`ImpactNeg`、`JsonExtractString`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`PrimitiveBoolean`、`PrimitiveBoolean`、`easy anythingIndexSwitch`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`SaveImageAdvanced`、`SaveLatent`、`easy seed`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CM_BoolToInt` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `DapaoMakeImageBatchNode` 知识库中没有该节点类型的任何知识
- 次要节点 `ExecutionBlocker` 知识库中没有该节点类型的任何知识
- 次要节点 `ExecutionBlocker` 知识库中没有该节点类型的任何知识
- 次要节点 `ExecutionBlocker` 知识库中没有该节点类型的任何知识
- 次要节点 `ExecutionBlocker` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageRGBA2RGB` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `ImpactNeg` 知识库中没有该节点类型的任何知识
- 次要节点 `ImpactNeg` 知识库中没有该节点类型的任何知识
- 次要节点 `JsonExtractString` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveLatent` 仅有 VAE/SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
