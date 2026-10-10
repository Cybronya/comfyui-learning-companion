---
key: 图片生成/图生图/Qwen image 2.1提示词强化｜反推提示词自动扩写｜文生图效果翻倍_2102233840218632193.json
name: Qwen image 2.1提示词强化｜反推提示词自动扩写｜文生图效果翻倍_2102233840218632193
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1提示词强化｜反推提示词自动扩写｜文生图效果翻倍_2102233840218632193.json
hash: 49c167bb28aee775
coverage: 0.676768
learned_at: 2026-10-10 20:48:08
nodes: [SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, JsonExtractString, llama_cpp_model_loader, llama_cpp_parameters, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveBoolean, PrimitiveBoolean, GetNode, GetNode, GetNode, ExecutionBlocker, PrimitiveInt, ImpactNeg, ImpactNeg, ExecutionBlocker, ExecutionBlocker, CR Text Replace, PrimitiveBoolean, PrimitiveBoolean, MathExpression_UTK, llama_cpp_instruct_adv, RHLLMChatNode, easy anythingIndexSwitch, DapaoMakeImageBatchNode, llama_cpp_instruct_adv, RHLLMChatNode, 1hew_SaveTxt, easy anythingIndexSwitch, easy anythingIndexSwitch, JjkText, SetNode, PrimitiveInt, ExecutionBlocker, SaveImage, ExecutionBlocker, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Text Replace, easy anythingIndexSwitch, easy anythingIndexSwitch, easy anythingIndexSwitch]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1提示词强化｜反推提示词自动扩写｜文生图效果翻倍_2102233840218632193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1提示词强化｜反推提示词自动扩写｜文生图效果翻倍_2102233840218632193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `SetNode`
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
- `JsonExtractString`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `GetNode`
- `GetNode`
- `GetNode`
- `ExecutionBlocker`
- `PrimitiveInt`
- `ImpactNeg`
- `ImpactNeg`
- `ExecutionBlocker`
- `ExecutionBlocker`
- `CR Text Replace`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `MathExpression_UTK`
- `llama_cpp_instruct_adv`
- `RHLLMChatNode`
- `easy anythingIndexSwitch`
- `DapaoMakeImageBatchNode`
- `llama_cpp_instruct_adv`
- `RHLLMChatNode`
- `1hew_SaveTxt`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `JjkText`
- `SetNode`
- `PrimitiveInt`
- `ExecutionBlocker`
- `SaveImage`
- `ExecutionBlocker`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **68%**（67/99）

**有卡**：`LoadImage`、`JsonExtractString`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`PrimitiveBoolean`、`ExecutionBlocker`、`ImpactNeg`、`MathExpression_UTK`、`llama_cpp_instruct_adv`、`RHLLMChatNode`、`DapaoMakeImageBatchNode`、`1hew_SaveTxt`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（4）：`CR Text Replace`、`easy anythingIndexSwitch`、`easy anythingIndexSwitch`、`easy anythingIndexSwitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
