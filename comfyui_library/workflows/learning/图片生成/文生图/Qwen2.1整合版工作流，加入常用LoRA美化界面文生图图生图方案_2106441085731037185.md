---
key: 图片生成/文生图/Qwen2.1整合版工作流，加入常用LoRA美化界面文生图图生图方案_2106441085731037185.json
name: Qwen2.1整合版工作流，加入常用LoRA美化界面文生图图生图方案_2106441085731037185
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1整合版工作流，加入常用LoRA美化界面文生图图生图方案_2106441085731037185.json
hash: 21553d087c33cf4d
coverage: 0.282723
learned_at: 2026-10-06 21:50:24
nodes: [GetNode, GetNode, Context (rgthree), SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, easy ifElse, LoraLoaderModelOnly, Context (rgthree), LoraLoaderModelOnly, Context (rgthree), GetNode, LoraLoaderModelOnly, GetNode, SetNode, GetNode, VAEDecode, GetNode, UNETLoader, SetNode, SetNode, easy ifElse, GetNode, easy ifElse, SetNode, CR Text, GetNode, CR Text, CR Text, SetNode, GetNode, Context (rgthree), Context (rgthree), easy ifElse, SetNode, SetNode, easy ifElse, GetNode, Context (rgthree), SetNode, GetNode, JoinStrings, SetNode, SetNode, easy ifElse, LoraLoaderModelOnly, CR Text, GetNode, Context (rgthree), GetNode, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, GetNode, EmptyLatentImage, GetNode, GetNode, SetNode, easy boolean, CR Text, SetNode, easy ifElse, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, easy ifElse, easy boolean, SetNode, GetNode, Context (rgthree), Context (rgthree), SetNode, QwenImage21Cache, GetNode, ComfySwitchNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), easy ifElse, GetNode, LoraLoaderModelOnly, SetNode, SetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, GetNode, QwenPERewriteT8, TextEncodeQwenImage21, LoraLoaderModelOnly, easy anythingIndexSwitch, LoadImage, LoadImage, SaveImage, CR Text, CR Text, SetNode, CR Prompt Text, ComfySwitchNode, GetNode, ComfySwitchNode, GetNode, GetNode, SetNode, SetNode, UNETLoader, CLIPLoader, UNETLoader, easy ifElse, GetNode, SetNode, SetNode, easy ifElse, GetNode, GetNode, GetNode, SetNode, easy boolean, CR Text, easy ifElse, CR Text, CR Text, GetNode, JoinStringMulti, GetNode, SetNode, SetNode, SetNode, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, ImpactSwitch, CR Text, CR Prompt Text, ResolutionSelector, easy boolean, easy showAnything, easy boolean, VAELoader, UNETLoader, easy float, easy ifElse, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Fast Groups Bypasser (rgthree), JoinStringMulti, JoinStrings, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenPERewriteT8, easy anythingIndexSwitch, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy float, CR Prompt Text, CR Prompt Text, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `JoinStringMulti` 知识库中没有该节点类型的任何知识, 次要节点 `JoinStrings` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1整合版工作流，加入常用LoRA美化界面文生图图生图方案_2106441085731037185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1整合版工作流，加入常用LoRA美化界面文生图图生图方案_2106441085731037185.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（191 个）：
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

覆盖率 **28%**（54/191）

**有卡**：`LoraLoaderModelOnly`、`VAEDecode`、`UNETLoader`、`EmptyLatentImage`、`QwenImage21Cache`、`LoadImage`、`KSampler`、`TextEncodeQwenImage21`、`SaveImage`、`CLIPLoader`、`ResolutionSelector`、`VAELoader`、`CLIPTextEncode`

**缺卡**（42）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Fast Groups Bypasser (rgthree)`、`JoinStringMulti`、`JoinStrings`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`QwenPERewriteT8`、`easy anythingIndexSwitch`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy float`、`CR Prompt Text`、`CR Prompt Text`、`solarL_SaveImagesToZip`

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
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `JoinStringMulti` 知识库中没有该节点类型的任何知识
- 次要节点 `JoinStrings` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
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
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
