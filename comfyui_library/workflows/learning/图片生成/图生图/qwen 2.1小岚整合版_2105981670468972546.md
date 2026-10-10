---
key: 图片生成/图生图/qwen 2.1小岚整合版_2105981670468972546.json
name: qwen 2.1小岚整合版_2105981670468972546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen 2.1小岚整合版_2105981670468972546.json
hash: bde75f858549b7ad
coverage: 0.216867
learned_at: 2026-10-10 20:48:12
nodes: [GetNode, GetNode, Context (rgthree), SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, easy ifElse, LoraLoaderModelOnly, Context (rgthree), LoraLoaderModelOnly, Context (rgthree), GetNode, LoraLoaderModelOnly, GetNode, SetNode, GetNode, VAEDecode, GetNode, UNETLoader, SetNode, SetNode, easy ifElse, GetNode, easy ifElse, SetNode, CR Text, GetNode, CR Text, CR Text, SetNode, GetNode, Context (rgthree), Context (rgthree), easy ifElse, SetNode, SetNode, easy ifElse, GetNode, Context (rgthree), SetNode, GetNode, JoinStrings, SetNode, SetNode, easy ifElse, LoraLoaderModelOnly, CR Text, GetNode, Context (rgthree), GetNode, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, GetNode, EmptyLatentImage, GetNode, GetNode, SetNode, easy boolean, CR Text, SetNode, MarkdownNote, easy ifElse, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, MarkdownNote, easy ifElse, easy boolean, SetNode, GetNode, Context (rgthree), Context (rgthree), MarkdownNote, SetNode, QwenImage21Cache, GetNode, ComfySwitchNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), easy ifElse, GetNode, LoraLoaderModelOnly, SetNode, SetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, GetNode, QwenPERewriteT8, TextEncodeQwenImage21, LoraLoaderModelOnly, MarkdownNote, easy anythingIndexSwitch, LoadImage, LoadImage, SaveImage, CR Text, CR Text, SetNode, CR Prompt Text, ComfySwitchNode, GetNode, ComfySwitchNode, GetNode, GetNode, SetNode, SetNode, UNETLoader, CLIPLoader, UNETLoader, easy ifElse, GetNode, SetNode, SetNode, easy ifElse, GetNode, GetNode, GetNode, SetNode, easy boolean, CR Text, easy ifElse, CR Text, CR Text, GetNode, JoinStringMulti, GetNode, SetNode, SetNode, SetNode, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, ImpactSwitch, CR Text, CR Prompt Text, ResolutionSelector, easy boolean, easy showAnything, easy boolean, VAELoader, UNETLoader, easy float, easy ifElse]
patterns: []
missing: [CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), Context (rgthree), easy anythingIndexSwitch, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy boolean, easy float, CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 159019529997946, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Context (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/qwen 2.1小岚整合版_2105981670468972546.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen 2.1小岚整合版_2105981670468972546.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（166 个）：
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
- `MarkdownNote`
- `easy ifElse`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `MarkdownNote`
- `easy ifElse`
- `easy boolean`
- `SetNode`
- `GetNode`
- `Context (rgthree)`
- `Context (rgthree)`
- `MarkdownNote`
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
- `MarkdownNote`
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `159019529997946`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **22%**（36/166）

**有卡**：`LoraLoaderModelOnly`、`VAEDecode`、`UNETLoader`、`JoinStrings`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`EmptyLatentImage`、`QwenImage21Cache`、`LoadImage`、`KSampler`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`SaveImage`、`CLIPLoader`、`JoinStringMulti`、`ResolutionSelector`、`VAELoader`

**缺卡**（34）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`Context (rgthree)`、`easy anythingIndexSwitch`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy boolean`、`easy float`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

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
