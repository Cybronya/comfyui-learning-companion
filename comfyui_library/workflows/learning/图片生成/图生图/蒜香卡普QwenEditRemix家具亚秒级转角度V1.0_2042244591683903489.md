---
key: 图片生成/图生图/蒜香卡普QwenEditRemix家具亚秒级转角度V1.0_2042244591683903489.json
name: 蒜香卡普QwenEditRemix家具亚秒级转角度V1.0_2042244591683903489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/蒜香卡普QwenEditRemix家具亚秒级转角度V1.0_2042244591683903489.json
hash: 5992ee0839b2b9bd
coverage: 0.870968
learned_at: 2026-10-23 13:25:00
nodes: [Any Switch (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Text, Text, Text, Text, Text, PreviewImage, PreviewAny, Text, Text, Text, VAEDecode, ConditioningZeroOut, SaveImage, CheckpointLoaderSimple, CLIPMergeSimple, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, CustomAddLabel, LoraLoader, SaveImage, Int, Text, QwenMultiangleCameraNode, LoadImage, Image Comparer (rgthree), LoadImage]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 1, "lora_name": "万能视角转换一致性家居产品应用_Q.Edit万能家居视角转换.safetensors", "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 65734077512344, "steps": 4, "strength_clip": 1.0000000000000002, "strength_model": 0.4000000000000001}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/蒜香卡普QwenEditRemix家具亚秒级转角度V1.0_2042244591683903489.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/蒜香卡普QwenEditRemix家具亚秒级转角度V1.0_2042244591683903489.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `Any Switch (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Text`
- `Text`
- `Text`
- `Text`
- `Text`
- `PreviewImage`
- `PreviewAny`
- `Text`
- `Text`
- `Text`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPMergeSimple`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `CustomAddLabel`
- `LoraLoader` ★核心
- `SaveImage`
- `Int`
- `Text`
- `QwenMultiangleCameraNode`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`
- `seed` = `65734077512344`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `lora_name` = `万能视角转换一致性家居产品应用_Q.Edit万能家居视角转换.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Text`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`CheckpointLoaderSimple`、`CLIPMergeSimple`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`KSampler`、`CustomAddLabel`、`LoraLoader`、`Int`、`QwenMultiangleCameraNode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、TextEncodeQwenImageEditPlusAdvance_lrzjason、LoraLoader、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
