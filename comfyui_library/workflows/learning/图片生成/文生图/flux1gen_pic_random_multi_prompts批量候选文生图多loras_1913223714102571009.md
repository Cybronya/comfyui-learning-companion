---
key: 图片生成/文生图/flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009.json
name: flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009.json
hash: 1915b6b1010a544a
coverage: 0.875
learned_at: 2026-10-15 22:27:45
nodes: [VAEDecode, Note, FluxLoraLoader, LoraLoader, BasicGuider, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, BasicScheduler, LoraLoader, FluxGuidance, FluxGuidance, EmptySD3LatentImage, CLIPTextEncode, CR Text Input Switch (4 way), ShowText|pysssss, CLIPTextEncode, RandomInt, RandomInt, ShowText|pysssss, ShowText|pysssss, FluxLoraLoader, CR Text Input Switch (4 way), CR Text Input Switch (4 way), ShowText|pysssss, CR Text, CR Text, CR Text, CR Text, CR Text, RandomInt, LoraLoader, VAELoader, DualCLIPLoader, SaveImage, UNETLoader, LoraLoader, LoraLoader, LoraLoader, KSampler]
patterns: [lora]
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "lora_name": "粉蓝色调主义_商业创意插画_v1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 30, "strength_clip": 1, "strength_model": 0.8}
---

# 图片生成/文生图/flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux1gen_pic_random_multi_prompts批量候选文生图多loras_1913223714102571009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `VAEDecode` ★核心
- `Note`
- `FluxLoraLoader` ★核心
- `LoraLoader` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LoraLoader` ★核心
- `FluxGuidance`
- `FluxGuidance`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `CR Text Input Switch (4 way)`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `RandomInt`
- `RandomInt`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `FluxLoraLoader` ★核心
- `CR Text Input Switch (4 way)`
- `CR Text Input Switch (4 way)`
- `ShowText|pysssss`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `RandomInt`
- `LoraLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `KSampler` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `粉蓝色调主义_商业创意插画_v1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `seed` = `0`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`VAEDecode`、`FluxLoraLoader`、`LoraLoader`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`FluxGuidance`、`EmptySD3LatentImage`、`CLIPTextEncode`、`CR Text Input Switch (4 way)`、`RandomInt`、`CR Text`、`VAELoader`、`DualCLIPLoader`、`SaveImage`、`UNETLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
