---
key: 图片生成/文生图/Flex.2文生图(支持Lora)工作流_1916401423968305153.json
name: Flex.2文生图(支持Lora)工作流_1916401423968305153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flex.2文生图(支持Lora)工作流_1916401423968305153.json
hash: b9f96011b23cff67
coverage: 0.947368
learned_at: 2026-10-15 22:26:21
nodes: [CLIPTextEncode, Note, ConditioningZeroOut, Flex2Conditioner, EmptySD3LatentImage, ApplyFBCacheOnModel, KSampler, FlexGuidance, DualCLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, LayerUtility: PurgeVRAM, CR Prompt Text, ImpactInt, Note Plus (mtb), FlexLoraLoaderModelOnly, UNETLoader, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 25}
---

# 图片生成/文生图/Flex.2文生图(支持Lora)工作流_1916401423968305153.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flex.2文生图(支持Lora)工作流_1916401423968305153.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `ConditioningZeroOut`
- `Flex2Conditioner`
- `EmptySD3LatentImage`
- `ApplyFBCacheOnModel`
- `KSampler` ★核心
- `FlexGuidance`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `CR Prompt Text`
- `ImpactInt`
- `Note Plus (mtb)`
- `FlexLoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`

## 关键参数

- `seed` = `726210541184116`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`CLIPTextEncode`、`ConditioningZeroOut`、`Flex2Conditioner`、`EmptySD3LatentImage`、`ApplyFBCacheOnModel`、`KSampler`、`FlexGuidance`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`ImpactInt`、`Note Plus (mtb)`、`FlexLoraLoaderModelOnly`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、UNETLoader、FlexGuidance、FlexLoraLoaderModelOnly
