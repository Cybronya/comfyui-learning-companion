---
key: 图片生成/反推提示词/Qwen image 2.1图像编辑(8)4步加速版_2103517980582834177.json
name: Qwen image 2.1图像编辑(8)4步加速版_2103517980582834177
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen image 2.1图像编辑(8)4步加速版_2103517980582834177.json
hash: 788b78795775e82c
coverage: 0.39
learned_at: 2026-10-10 20:48:00
nodes: [MarkdownNote, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, VAEEncode, GetNode, GetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, CLIPLoader, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, 忽略多组孤海, TextEncodeQwenImage21, GetNode, ImpactNeg, GetNode, DapaoMakeImageBatchNode, llama_cpp_parameters, GetNode, CM_BoolToInt, PrimitiveFloat, CR Text Replace, LayerUtility: PurgeVRAM, SetNode, 孤海注释, 孤海注释, 孤海注释, 孤海注释, ComfySwitchNode, MarkdownNote, easy anythingIndexSwitch, PrimitiveInt, ExecutionBlocker, llama_cpp_instruct_adv, easy seed, KSampler, GetNode, LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, UNETLoader, LoadImage, QwenImage21Cache, ImageRGBA2RGB, ImpactNeg, VAELoader, VAEEncode, JsonExtractString, JjkText, SaveLatent, PrimitiveBoolean, PrimitiveBoolean, ExecutionBlocker, VAEDecode, ExecutionBlocker, ExecutionBlocker, SaveImage, SaveImageAdvanced, llama_cpp_model_loader]
patterns: [image_to_image]
missing: [CR Text Replace, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, easy anythingIndexSwitch, 忽略多组孤海, easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 523714167721647, "steps": 8}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/Qwen image 2.1图像编辑(8)4步加速版_2103517980582834177.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen image 2.1图像编辑(8)4步加速版_2103517980582834177.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
- `MarkdownNote`
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
- `忽略多组孤海`
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
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `ComfySwitchNode`
- `MarkdownNote`
- `easy anythingIndexSwitch`
- `PrimitiveInt`
- `ExecutionBlocker`
- `llama_cpp_instruct_adv`
- `easy seed`
- `KSampler` ★核心
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
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

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `523714167721647`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **39%**（39/100）

**有卡**：`ImageScaleToTotalPixels`、`VAEEncode`、`LoadImage`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`ImpactNeg`、`DapaoMakeImageBatchNode`、`llama_cpp_parameters`、`CM_BoolToInt`、`ExecutionBlocker`、`llama_cpp_instruct_adv`、`KSampler`、`UNETLoader`、`QwenImage21Cache`、`ImageRGBA2RGB`、`JsonExtractString`、`SaveLatent`、`PrimitiveBoolean`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`、`llama_cpp_model_loader`

**缺卡**（6）：`CR Text Replace`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`easy anythingIndexSwitch`、`忽略多组孤海`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
