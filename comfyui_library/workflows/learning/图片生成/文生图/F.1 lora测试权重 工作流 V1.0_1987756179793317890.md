---
key: 图片生成/文生图/F.1 lora测试权重 工作流 V1.0_1987756179793317890.json
name: F.1 lora测试权重 工作流 V1.0_1987756179793317890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1 lora测试权重 工作流 V1.0_1987756179793317890.json
hash: 3b1fa31aa033a3cd
coverage: 0.986726
learned_at: 2026-10-15 22:26:16
nodes: [ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, SaveImage, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, SaveImage, SaveImage, SaveImage, LoraLoader, LoraLoader, LoraLoader, CR Text, easy getNode, easy getNode, easy getNode, easy getNode, CLIPTextEncode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, DualCLIPLoader, easy getNode, CLIPTextEncode, easy getNode, CLIPTextEncode, CLIPTextEncode, easy getNode, CLIPTextEncode, easy getNode, CLIPTextEncode, easy getNode, CLIPTextEncode, easy getNode, CLIPTextEncode, easy getNode, CLIPTextEncode, easy getNode, CLIPTextEncode, easy getNode, easy getNode, CLIPTextEncode, easy getNode, VAELoader, VAEDecode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, Anything Everywhere, easy setNode, easy setNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, SaveImage, CR Text, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, CLIPTextEncode, easy getNode, easy getNode, CLIPTextEncode, easy getNode, CLIPTextEncode, easy getNode, easy getNode, CLIPTextEncode, easy getNode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, easy getNode, easy getNode, easy getNode, LoraLoader, LoraLoader, LoraLoader, LoraLoader, SaveImage, SaveImage, LoraLoader, LoraLoader, LoraLoader, LoraLoader, LoraLoader, LoraLoader, easy getNode, easy getNode, LoraLoader, easy getNode, easy getNode, EmptySD3LatentImage, KSampler, KSampler, KSampler, KSampler, KSampler, KSampler, KSampler, KSampler, KSampler, KSampler, SaveImage, KSampler, KSampler, KSampler, KSampler, Anything Everywhere, KSampler, easy setNode, easy setNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, SaveImage, ttN float, UNETLoader, easy getNode, SaveImage, SaveImage, easy getNode, easy getNode, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, CLIPTextEncode, easy seed, ShowText|pysssss, easy setNode, BaiduTranslateNode, SaveImage, SaveImage, SaveImage, SaveImage, CR Text, LoraLoader, easy setNode, LoraLoader, LoraNames_]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "zi-jm-flux-lora-000008.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 261318560279650, "steps": 30, "strength_clip": 0.10000000000000002, "strength_model": 0.10000000000000002}
---

# 图片生成/文生图/F.1 lora测试权重 工作流 V1.0_1987756179793317890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1 lora测试权重 工作流 V1.0_1987756179793317890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（226 个）：
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CR Text`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `DualCLIPLoader`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Anything Everywhere`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `CR Text`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `SaveImage`
- `SaveImage`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `easy getNode`
- `easy getNode`
- `LoraLoader` ★核心
- `easy getNode`
- `easy getNode`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `Anything Everywhere`
- `KSampler` ★核心
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `SaveImage`
- `ttN float`
- `UNETLoader` ★核心
- `easy getNode`
- `SaveImage`
- `SaveImage`
- `easy getNode`
- `easy getNode`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `easy seed`
- `ShowText|pysssss`
- `easy setNode`
- `BaiduTranslateNode`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `CR Text`
- `LoraLoader` ★核心
- `easy setNode`
- `LoraLoader` ★核心
- `LoraNames_`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `zi-jm-flux-lora-000008.safetensors`
- `strength_model` = `0.10000000000000002`
- `strength_clip` = `0.10000000000000002`
- `seed` = `261318560279650`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **99%**（223/226）

**有卡**：`ConditioningZeroOut`、`FluxGuidance`、`CLIPTextEncode`、`SaveImage`、`LoraLoader`、`CR Text`、`easy getNode`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`easy setNode`、`EmptySD3LatentImage`、`KSampler`、`ttN float`、`UNETLoader`、`easy seed`、`BaiduTranslateNode`、`LoraNames_`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、FluxGuidance、easy seed
