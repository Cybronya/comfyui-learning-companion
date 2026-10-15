---
key: 图片生成/文生图/Qwen Image 视频封面制作 + Qwen Edit Plus 添加人物_1970950894877609986.json
name: Qwen Image 视频封面制作 + Qwen Edit Plus 添加人物_1970950894877609986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 视频封面制作 + Qwen Edit Plus 添加人物_1970950894877609986.json
hash: 599a285238acba97
coverage: 0.608696
learned_at: 2026-10-10 20:58:55
nodes: [VAELoader, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, ModelSamplingAuraFlow, EmptySD3LatentImage, LimitNumber, EmptySD3LatentImage, ImpactSwitch, JjkText, TextCombinerTwo, Note, TextCombinerTwo, TextCombinerTwo, TextCombinerSix, JjkText, JjkText, EmptySD3LatentImage, PrimitiveInt, JjkText, JjkText, RH_LLMAPI_NODE, JjkText, KSampler, Note, JjkText, JjkText, CLIPLoader, VAELoader, ConditioningZeroOut, TextEncodeQwenImageEditPlus_lrzjason, LayerUtility: PurgeVRAM V2, UNETLoader, SaveImage, easy showAnything, KSampler, LoadImage, easy seed, SaveImage, Image Comparer (rgthree), JjkText, VAEDecode, JjkText, LoadImage, VAEDecode]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, easy seed]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 931852754142298, "steps": 20}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 视频封面制作 + Qwen Edit Plus 添加人物_1970950894877609986.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 视频封面制作 + Qwen Edit Plus 添加人物_1970950894877609986.json`

## 结构

**节点**（46 个）：
- `VAELoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `CLIPLoader`
- `UNETLoader`
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `LimitNumber`
- `EmptySD3LatentImage`
- `ImpactSwitch`
- `JjkText`
- `TextCombinerTwo`
- `Note`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `TextCombinerSix`
- `JjkText`
- `JjkText`
- `EmptySD3LatentImage`
- `PrimitiveInt`
- `JjkText`
- `JjkText`
- `RH_LLMAPI_NODE`
- `JjkText`
- `KSampler`
- `Note`
- `JjkText`
- `JjkText`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader`
- `SaveImage`
- `easy showAnything`
- `KSampler`
- `LoadImage`
- `easy seed`
- `SaveImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `VAEDecode`
- `JjkText`
- `LoadImage`
- `VAEDecode`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `seed` = `931852754142298`
- `steps` = `20`

## 知识

覆盖率 **61%**（28/46）

**有卡**：`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`LimitNumber`、`ImpactSwitch`、`JjkText`、`TextCombinerTwo`、`Note`、`TextCombinerSix`、`PrimitiveInt`、`RH_LLMAPI_NODE`、`KSampler`

**缺卡**（2）：`LayerUtility: PurgeVRAM V2`、`easy seed`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
