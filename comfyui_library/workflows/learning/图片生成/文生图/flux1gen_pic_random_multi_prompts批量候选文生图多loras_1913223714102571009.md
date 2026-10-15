---
key: 图片生成/文生图/flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009.json
name: flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009.json
hash: 1915b6b1010a544a
coverage: 0.675
learned_at: 2026-10-10 20:59:19
nodes: [VAEDecode, Note, FluxLoraLoader, LoraLoader, BasicGuider, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, BasicScheduler, LoraLoader, FluxGuidance, FluxGuidance, EmptySD3LatentImage, CLIPTextEncode, CR Text Input Switch (4 way), ShowText|pysssss, CLIPTextEncode, RandomInt, RandomInt, ShowText|pysssss, ShowText|pysssss, FluxLoraLoader, CR Text Input Switch (4 way), CR Text Input Switch (4 way), ShowText|pysssss, CR Text, CR Text, CR Text, CR Text, CR Text, RandomInt, LoraLoader, VAELoader, DualCLIPLoader, SaveImage, UNETLoader, LoraLoader, LoraLoader, LoraLoader, KSampler]
patterns: [lora]
missing: [CR Text, CR Text, CR Text, CR Text, CR Text, CR Text Input Switch (4 way), CR Text Input Switch (4 way), CR Text Input Switch (4 way)]
parameters: {"cfg": 3.5, "denoise": 1, "lora_name": "粉蓝色调主义_商业创意插画_v1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 30, "strength_clip": 1, "strength_model": 0.8}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009.json`

## 结构

**节点**（40 个）：
- `VAEDecode`
- `Note`
- `FluxLoraLoader`
- `LoraLoader`
- `BasicGuider`
- `SamplerCustomAdvanced`
- `RandomNoise`
- `KSamplerSelect`
- `BasicScheduler`
- `LoraLoader`
- `FluxGuidance`
- `FluxGuidance`
- `EmptySD3LatentImage`
- `CLIPTextEncode`
- `CR Text Input Switch (4 way)`
- `ShowText|pysssss`
- `CLIPTextEncode`
- `RandomInt`
- `RandomInt`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `FluxLoraLoader`
- `CR Text Input Switch (4 way)`
- `CR Text Input Switch (4 way)`
- `ShowText|pysssss`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `RandomInt`
- `LoraLoader`
- `VAELoader`
- `DualCLIPLoader`
- `SaveImage`
- `UNETLoader`
- `LoraLoader`
- `LoraLoader`
- `LoraLoader`
- `KSampler`

**识别到的模式**：lora

## 关键参数

- `cfg` = `3.5`
- `denoise` = `1`
- `lora_name` = `粉蓝色调主义_商业创意插画_v1.0.safetensors`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `0`
- `steps` = `30`
- `strength_clip` = `1`
- `strength_model` = `0.8`

## 知识

覆盖率 **68%**（27/40）

**有卡**：`VAEDecode`、`Note`、`FluxLoraLoader`、`LoraLoader`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`FluxGuidance`、`EmptySD3LatentImage`、`CLIPTextEncode`、`CR Text Input Switch (4 way)`、`ShowText|pysssss`、`RandomInt`、`CR Text`

**缺卡**（8）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Input Switch (4 way)`、`CR Text Input Switch (4 way)`、`CR Text Input Switch (4 way)`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识
