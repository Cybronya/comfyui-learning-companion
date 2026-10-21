---
key: 图片生成/文生图/【Supermate】Zimage双采图像生成Zimage Dual-Capture_2036602147382497281.json
name: 【Supermate】Zimage双采图像生成Zimage Dual-Capture_2036602147382497281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Supermate】Zimage双采图像生成Zimage Dual-Capture_2036602147382497281.json
hash: 43d4c6679fed4f9f
coverage: 1
learned_at: 2026-10-21 02:58:00
nodes: [VAEDecode, ModelSamplingAuraFlow, EmptyLatentImage, ConditioningZeroOut, Int, Int, VAELoader, UNETLoader, UNETLoader, CLIPTextEncode, ModelSamplingAuraFlow, KSamplerAdvanced, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, KSamplerAdvanced, SaveImage, CR Text, CLIPLoader, INTConstant, Label (rgthree), Label (rgthree), INTConstant, Label (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 1024}
---

# 图片生成/文生图/【Supermate】Zimage双采图像生成Zimage Dual-Capture_2036602147382497281.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Supermate】Zimage双采图像生成Zimage Dual-Capture_2036602147382497281.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `Int`
- `Int`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `CR Text`
- `CLIPLoader`
- `INTConstant`
- `Label (rgthree)`
- `Label (rgthree)`
- `INTConstant`
- `Label (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`VAEDecode`、`ModelSamplingAuraFlow`、`EmptyLatentImage`、`ConditioningZeroOut`、`Int`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`SaveImage`、`CR Text`、`CLIPLoader`、`INTConstant`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
