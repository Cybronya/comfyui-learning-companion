---
key: 图片生成/图生图/Qwen 2.1多图编辑支持遮罩选定范围，三图编辑可自定义比例_2102849234457423874.json
name: Qwen 2.1多图编辑支持遮罩选定范围，三图编辑可自定义比例_2102849234457423874
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 2.1多图编辑支持遮罩选定范围，三图编辑可自定义比例_2102849234457423874.json
hash: 34a9dd5e404f038c
coverage: 0.877193
learned_at: 2026-10-21 00:42:00
nodes: [Image Comparer (rgthree), LoadImage, GoohaiUniversalSlider, LoadImage, ComfySwitchNode, ResolutionSelector, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ModelConfig_EditUtils, PathchSageAttentionKJ, QwenImage21EditApply_EditUtils, ConditioningZeroOut, VAEDecode, EmptyLatentImage, CropWithPadInfo_EditUtils, KSampler, CropWithPadInfo_EditUtils, Fast Bypasser (rgthree), 布尔孤海, SaveImage, UNETLoader, CLIPLoader, VAELoader, EditTextEncode_EditUtils, LoadImage, workflow>遮罩逻辑, QwenImage21ConfigPreparer_EditUtils, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen 2.1多图编辑支持遮罩选定范围，三图编辑可自定义比例_2102849234457423874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 2.1多图编辑支持遮罩选定范围，三图编辑可自定义比例_2102849234457423874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `Image Comparer (rgthree)`
- `LoadImage`
- `GoohaiUniversalSlider`
- `LoadImage`
- `ComfySwitchNode`
- `ResolutionSelector`
- `QwenImage21ConfigPreparer_EditUtils`
- `QwenImage21ConfigPreparer_EditUtils`
- `QwenImage21ModelConfig_EditUtils`
- `PathchSageAttentionKJ`
- `QwenImage21EditApply_EditUtils`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CropWithPadInfo_EditUtils`
- `KSampler` ★核心
- `CropWithPadInfo_EditUtils`
- `Fast Bypasser (rgthree)`
- `布尔孤海`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EditTextEncode_EditUtils`
- `LoadImage`
- `workflow>遮罩逻辑`
- `QwenImage21ConfigPreparer_EditUtils`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（50/57）

**有卡**：`LoadImage`、`GoohaiUniversalSlider`、`ResolutionSelector`、`QwenImage21ConfigPreparer_EditUtils`、`QwenImage21ModelConfig_EditUtils`、`PathchSageAttentionKJ`、`QwenImage21EditApply_EditUtils`、`ConditioningZeroOut`、`VAEDecode`、`EmptyLatentImage`、`CropWithPadInfo_EditUtils`、`KSampler`、`Fast Bypasser (rgthree)`、`布尔孤海`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EditTextEncode_EditUtils`、`workflow>遮罩逻辑`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
