---
key: 图片生成/图生图/图像编辑by Qwen image 2.1 自动优化提示词_2102274359825100801.json
name: 图像编辑by Qwen image 2.1 自动优化提示词_2102274359825100801.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像编辑by Qwen image 2.1 自动优化提示词_2102274359825100801.json
hash: 3fe93bd97f3159da
coverage: 0.340659
learned_at: 2026-10-09 22:27:10
nodes: [MarkdownNote, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, VAEEncode, GetNode, GetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, CLIPLoader, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, 忽略多组孤海, TextEncodeQwenImage21, LoadImage, UNETLoader, QwenImage21Cache, LayerUtility: ImageScaleByAspectRatio V2, GetNode, ImpactNeg, GetNode, DapaoMakeImageBatchNode, llama_cpp_parameters, GetNode, CM_BoolToInt, JsonExtractString, PrimitiveFloat, CR Text Replace, LayerUtility: PurgeVRAM, SetNode, GetNode, VAEDecode, SaveImage, 孤海注释, 孤海注释, 孤海注释, 孤海注释, ComfySwitchNode, ExecutionBlocker, SaveImageAdvanced, MarkdownNote, easy anythingIndexSwitch, PrimitiveInt, llama_cpp_model_loader, ExecutionBlocker, KSampler, JjkText, PrimitiveBoolean, llama_cpp_instruct_adv, easy seed]
patterns: [image_to_image]
missing: [CR Text Replace, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, easy anythingIndexSwitch, 忽略多组孤海, easy seed]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 736553675410799, "steps": 50}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/图像编辑by Qwen image 2.1 自动优化提示词_2102274359825100801.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102274359825100801.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
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
- `LoadImage`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `ImpactNeg`
- `GetNode`
- `DapaoMakeImageBatchNode`
- `llama_cpp_parameters`
- `GetNode`
- `CM_BoolToInt`
- `JsonExtractString`
- `PrimitiveFloat`
- `CR Text Replace`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `ComfySwitchNode`
- `ExecutionBlocker`
- `SaveImageAdvanced`
- `MarkdownNote`
- `easy anythingIndexSwitch`
- `PrimitiveInt`
- `llama_cpp_model_loader`
- `ExecutionBlocker`
- `KSampler` ★核心
- `JjkText`
- `PrimitiveBoolean`
- `llama_cpp_instruct_adv`
- `easy seed`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `736553675410799`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **34%**（31/91）

**有卡**：`ImageScaleToTotalPixels`、`VAEEncode`、`LoadImage`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`UNETLoader`、`QwenImage21Cache`、`ImpactNeg`、`DapaoMakeImageBatchNode`、`llama_cpp_parameters`、`CM_BoolToInt`、`JsonExtractString`、`VAEDecode`、`SaveImage`、`ExecutionBlocker`、`SaveImageAdvanced`、`llama_cpp_model_loader`、`KSampler`、`PrimitiveBoolean`、`llama_cpp_instruct_adv`

**缺卡**（6）：`CR Text Replace`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`easy anythingIndexSwitch`、`忽略多组孤海`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
