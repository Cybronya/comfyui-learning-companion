---
key: 图片生成/图生图/图片换装-超强一致lora2.0_2022331929244213249.json
name: 图片换装-超强一致lora2.0_2022331929244213249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片换装-超强一致lora2.0_2022331929244213249.json
hash: 493b6ed198107b3b
coverage: 0.909091
learned_at: 2026-10-23 12:41:06
nodes: [TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, ConditioningZeroOut, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditConfigPreparer, SaveImage, PrimitiveStringMultiline, easy cleanGpuUsed, KSampler, VAELoader, CLIPLoader, LoraLoaderModelOnly, VAEDecode, easy cleanGpuUsed, ImageStitch, ImageStitch, PreviewImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Int, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1091359629774735, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图片换装-超强一致lora2.0_2022331929244213249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片换装-超强一致lora2.0_2022331929244213249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `SaveImage`
- `PrimitiveStringMultiline`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ImageStitch`
- `ImageStitch`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `LoadImage`

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`TextEncodeQwenImageEditPlusCustom_lrzjason`、`UNETLoader`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`QwenEditConfigPreparer`、`SaveImage`、`easy cleanGpuUsed`、`KSampler`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`ImageStitch`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
