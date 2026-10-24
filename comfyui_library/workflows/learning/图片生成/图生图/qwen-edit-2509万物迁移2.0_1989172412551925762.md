---
key: 图片生成/图生图/qwen-edit-2509万物迁移2.0_1989172412551925762.json
name: qwen-edit-2509万物迁移2.0_1989172412551925762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-edit-2509万物迁移2.0_1989172412551925762.json
hash: e3a2482bbc51067d
coverage: 0.903226
learned_at: 2026-10-23 11:42:23
nodes: [UNETLoader, QwenEditConfigPreparer, MaskFillHoles, LoraLoaderModelOnly, SaveImage, SaveImage, KSampler, VAEDecode, ImageConcanate, 图像缩放V2_孤海, ImageConcanate, SaveImage, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), 图像缩放V2_孤海, LoraLoaderModelOnly, KSampler, LoadImage, LoadImage, CR Text, QwenEditConfigPreparer, CLIPLoader, ConditioningZeroOut, TextEncodeQwenImageEditPlusCustom_lrzjason, ImageConcanate, ImageConcanate, VAELoader, VAEDecode, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 365460837168391, "steps": 20}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-edit-2509万物迁移2.0_1989172412551925762.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-edit-2509万物迁移2.0_1989172412551925762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `QwenEditConfigPreparer`
- `MaskFillHoles`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageConcanate`
- `图像缩放V2_孤海`
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `图像缩放V2_孤海`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `CR Text`
- `QwenEditConfigPreparer`
- `CLIPLoader`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ImageConcanate`
- `ImageConcanate`
- `VAELoader`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `365460837168391`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`UNETLoader`、`QwenEditConfigPreparer`、`MaskFillHoles`、`LoraLoaderModelOnly`、`SaveImage`、`KSampler`、`VAEDecode`、`ImageConcanate`、`图像缩放V2_孤海`、`LoadImage`、`CR Text`、`CLIPLoader`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
