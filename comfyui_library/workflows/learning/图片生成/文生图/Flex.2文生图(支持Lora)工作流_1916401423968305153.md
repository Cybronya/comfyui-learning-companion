---
key: 图片生成/文生图/Flex.2文生图(支持Lora)工作流_1916401423968305153.json
name: Flex.2文生图(支持Lora)工作流_1916401423968305153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flex.2文生图(支持Lora)工作流_1916401423968305153.json
hash: b9f96011b23cff67
coverage: 0.789474
learned_at: 2026-10-10 20:58:33
nodes: [CLIPTextEncode, Note, ConditioningZeroOut, Flex2Conditioner, EmptySD3LatentImage, ApplyFBCacheOnModel, KSampler, FlexGuidance, DualCLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, LayerUtility: PurgeVRAM, CR Prompt Text, ImpactInt, Note Plus (mtb), FlexLoraLoaderModelOnly, UNETLoader, SaveImage]
patterns: []
missing: [LayerUtility: PurgeVRAM, Note Plus (mtb), CR Prompt Text]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 25}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flex.2文生图(支持Lora)工作流_1916401423968305153.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flex.2文生图(支持Lora)工作流_1916401423968305153.json`

## 结构

**节点**（19 个）：
- `CLIPTextEncode`
- `Note`
- `ConditioningZeroOut`
- `Flex2Conditioner`
- `EmptySD3LatentImage`
- `ApplyFBCacheOnModel`
- `KSampler`
- `FlexGuidance`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `VAEDecode`
- `LayerUtility: PurgeVRAM`
- `CR Prompt Text`
- `ImpactInt`
- `Note Plus (mtb)`
- `FlexLoraLoaderModelOnly`
- `UNETLoader`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `seed` = `726210541184116`
- `steps` = `25`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`CLIPTextEncode`、`Note`、`ConditioningZeroOut`、`Flex2Conditioner`、`EmptySD3LatentImage`、`ApplyFBCacheOnModel`、`KSampler`、`FlexGuidance`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`ImpactInt`

**缺卡**（3）：`LayerUtility: PurgeVRAM`、`Note Plus (mtb)`、`CR Prompt Text`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
