---
key: 图片生成/文生图/qwen2.1小岚整合版｜文生图反推提示词图生图三合一全套_2106208856383778817.json
name: qwen2.1小岚整合版｜文生图反推提示词图生图三合一全套_2106208856383778817
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen2.1小岚整合版｜文生图反推提示词图生图三合一全套_2106208856383778817.json
hash: 4e1daae9ca568f4f
coverage: 0.365854
learned_at: 2026-10-10 23:16:50
nodes: [GetNode, GetNode, Context (rgthree), SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, easy ifElse, LoraLoaderModelOnly, Context (rgthree), LoraLoaderModelOnly, Context (rgthree), GetNode, LoraLoaderModelOnly, GetNode, SetNode, GetNode, VAEDecode, GetNode, UNETLoader, SetNode, SetNode, easy ifElse, GetNode, easy ifElse, SetNode, CR Text, GetNode, CR Text, CR Text, SetNode, GetNode, Context (rgthree), Context (rgthree), easy ifElse, SetNode, SetNode, easy ifElse, GetNode, Context (rgthree), SetNode, GetNode, JoinStrings, SetNode, SetNode, easy ifElse, LoraLoaderModelOnly, CR Text, GetNode, Context (rgthree), GetNode, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, GetNode, EmptyLatentImage, GetNode, GetNode, SetNode, easy boolean, CR Text, SetNode, easy ifElse, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, easy ifElse, easy boolean, SetNode, GetNode, Context (rgthree), Context (rgthree), SetNode, QwenImage21Cache, GetNode, ComfySwitchNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), easy ifElse, GetNode, LoraLoaderModelOnly, SetNode, SetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, GetNode, QwenPERewriteT8, TextEncodeQwenImage21, LoraLoaderModelOnly, easy anythingIndexSwitch, LoadImage, LoadImage, SaveImage, CR Text, CR Text, SetNode, CR Prompt Text, ComfySwitchNode, GetNode, ComfySwitchNode, GetNode, GetNode, SetNode, SetNode, UNETLoader, CLIPLoader, UNETLoader, easy ifElse, GetNode, SetNode, SetNode, easy ifElse, GetNode, GetNode, GetNode, SetNode, easy boolean, CR Text, easy ifElse, CR Text, CR Text, GetNode, JoinStringMulti, GetNode, SetNode, SetNode, SetNode, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, ImpactSwitch, CR Text, CR Prompt Text, ResolutionSelector, easy boolean, easy showAnything, easy boolean, VAELoader, UNETLoader, easy float, easy ifElse, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), easy anythingIndexSwitch, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy float, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen2.1小岚整合版｜文生图反推提示词图生图三合一全套_2106208856383778817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen2.1小岚整合版｜文生图反推提示词图生图三合一全套_2106208856383778817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（205 个）：
- `GetNode`
- `GetNode`
- `Context (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `easy ifElse`
- `LoraLoaderModelOnly` ★核心
- `Context (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Context (rgthree)`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `easy ifElse`
- `GetNode`
- `easy ifElse`
- `SetNode`
- `CR Text`
- `GetNode`
- `CR Text`
- `CR Text`
- `SetNode`
- `GetNode`
- `Context (rgthree)`
- `Context (rgthree)`
- `easy ifElse`
- `SetNode`
- `SetNode`
- `easy ifElse`
- `GetNode`
- `Context (rgthree)`
- `SetNode`
- `GetNode`
- `JoinStrings`
- `SetNode`
- `SetNode`
- `easy ifElse`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `GetNode`
- `Context (rgthree)`
- `GetNode`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `GetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `easy boolean`
- `CR Text`
- `SetNode`
- `easy ifElse`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `easy ifElse`
- `easy boolean`
- `SetNode`
- `GetNode`
- `Context (rgthree)`
- `Context (rgthree)`
- `SetNode`
- `QwenImage21Cache`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `easy ifElse`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `GetNode`
- `QwenPERewriteT8`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `easy anythingIndexSwitch`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `CR Text`
- `CR Text`
- `SetNode`
- `CR Prompt Text`
- `ComfySwitchNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `easy ifElse`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy ifElse`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy boolean`
- `CR Text`
- `easy ifElse`
- `CR Text`
- `CR Text`
- `GetNode`
- `JoinStringMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy boolean`
- `easy boolean`
- `easy boolean`
- `easy boolean`
- `easy boolean`
- `ImpactSwitch`
- `CR Text`
- `CR Prompt Text`
- `ResolutionSelector`
- `easy boolean`
- `easy showAnything`
- `easy boolean`
- `VAELoader`
- `UNETLoader` ★核心
- `easy float`
- `easy ifElse`
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

覆盖率 **37%**（75/205）

**有卡**：`LoraLoaderModelOnly`、`VAEDecode`、`UNETLoader`、`JoinStrings`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`EmptyLatentImage`、`QwenImage21Cache`、`LoadImage`、`KSampler`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`SaveImage`、`CLIPLoader`、`JoinStringMulti`、`ResolutionSelector`、`VAELoader`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（34）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`easy anythingIndexSwitch`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy float`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
