---
key: 图片生成/图生图/Flex.2图片反推洗图工作流_1916314155664740353.json
name: Flex.2图片反推洗图工作流_1916314155664740353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flex.2图片反推洗图工作流_1916314155664740353.json
hash: 5ced36107683798b
coverage: 0.875
learned_at: 2026-10-23 10:56:03
nodes: [CLIPTextEncode, Note, ConditioningZeroOut, Flex2Conditioner, EmptySD3LatentImage, easy showAnything, ApplyFBCacheOnModel, JWImageResizeByLongerSide, FlexGuidance, DualCLIPLoader, easy showAnything, CLIPTextEncode, SaveImage, VAELoader, LoadImage, RH_Captioner, GoogleTranslateTextNode, CR Prompt Text, KSampler, Note Plus (mtb), ImpactInt, LayerUtility: PurgeVRAM, VAEDecode, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 25}
---

# 图片生成/图生图/Flex.2图片反推洗图工作流_1916314155664740353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flex.2图片反推洗图工作流_1916314155664740353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `ConditioningZeroOut`
- `Flex2Conditioner`
- `EmptySD3LatentImage`
- `easy showAnything`
- `ApplyFBCacheOnModel`
- `JWImageResizeByLongerSide`
- `FlexGuidance`
- `DualCLIPLoader`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAELoader`
- `LoadImage`
- `RH_Captioner`
- `GoogleTranslateTextNode`
- `CR Prompt Text`
- `KSampler` ★核心
- `Note Plus (mtb)`
- `ImpactInt`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `726210541184116`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPTextEncode`、`ConditioningZeroOut`、`Flex2Conditioner`、`EmptySD3LatentImage`、`ApplyFBCacheOnModel`、`JWImageResizeByLongerSide`、`FlexGuidance`、`DualCLIPLoader`、`SaveImage`、`VAELoader`、`LoadImage`、`RH_Captioner`、`GoogleTranslateTextNode`、`CR Prompt Text`、`KSampler`、`Note Plus (mtb)`、`ImpactInt`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、FlexGuidance
