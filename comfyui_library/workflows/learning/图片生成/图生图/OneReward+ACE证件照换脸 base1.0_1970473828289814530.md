---
key: 图片生成/图生图/OneReward+ACE证件照换脸 base1.0_1970473828289814530.json
name: OneReward+ACE证件照换脸 base1.0_1970473828289814530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OneReward+ACE证件照换脸 base1.0_1970473828289814530.json
hash: 8ecea25c68a4251e
coverage: 0.9
learned_at: 2026-10-23 11:10:26
nodes: [UNETLoader, LoraLoaderModelOnly, DifferentialDiffusion, GrowMaskWithBlur, CLIPTextEncode, ACEPlusLoraConditioning, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, RandomNoise, KSamplerSelect, VAELoader, DualCLIPLoader, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, BasicScheduler, SamplerCustomAdvanced, preview_mask, ImageCrop, SaveImage, ACEPlusLoraProcessor, LoadImage, LoadImage, Text, SaveImage, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: []
---

# 图片生成/图生图/OneReward+ACE证件照换脸 base1.0_1970473828289814530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OneReward+ACE证件照换脸 base1.0_1970473828289814530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DifferentialDiffusion`
- `GrowMaskWithBlur`
- `CLIPTextEncode` ★核心
- `ACEPlusLoraConditioning`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `preview_mask`
- `ImageCrop`
- `SaveImage`
- `ACEPlusLoraProcessor`
- `LoadImage`
- `LoadImage`
- `Text`
- `SaveImage`
- `Note Plus (mtb)`
- `LoadImageFromUrl`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`DifferentialDiffusion`、`GrowMaskWithBlur`、`CLIPTextEncode`、`ACEPlusLoraConditioning`、`BasicGuider`、`VAEDecode`、`RandomNoise`、`KSamplerSelect`、`VAELoader`、`DualCLIPLoader`、`FluxGuidance`、`ConditioningZeroOut`、`BasicScheduler`、`SamplerCustomAdvanced`、`preview_mask`、`ImageCrop`、`SaveImage`、`ACEPlusLoraProcessor`、`LoadImage`、`Text`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
