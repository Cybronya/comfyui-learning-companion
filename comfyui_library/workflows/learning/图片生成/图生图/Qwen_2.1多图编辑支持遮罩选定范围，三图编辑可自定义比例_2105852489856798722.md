---
key: 图片生成/图生图/Qwen_2.1多图编辑支持遮罩选定范围，三图编辑可自定义比例_2105852489856798722.json
name: Qwen_2.1多图编辑支持遮罩选定范围，三图编辑可自定义比例_2105852489856798722.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_2.1多图编辑支持遮罩选定范围，三图编辑可自定义比例_2105852489856798722.json
hash: 5341117720304294
coverage: 0.842105
learned_at: 2026-10-09 22:09:17
nodes: [Image Comparer (rgthree), LoadImage, GoohaiUniversalSlider, LoadImage, ComfySwitchNode, ResolutionSelector, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ModelConfig_EditUtils, PathchSageAttentionKJ, QwenImage21EditApply_EditUtils, ConditioningZeroOut, VAEDecode, EmptyLatentImage, CropWithPadInfo_EditUtils, KSampler, CropWithPadInfo_EditUtils, Fast Bypasser (rgthree), 布尔孤海, SaveImage, UNETLoader, CLIPLoader, VAELoader, EditTextEncode_EditUtils, LoadImage, workflow>遮罩逻辑, QwenImage21ConfigPreparer_EditUtils, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: [Fast Bypasser (rgthree), workflow>遮罩逻辑, 布尔孤海]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>遮罩逻辑` 知识库中没有该节点类型的任何知识, 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_2.1多图编辑支持遮罩选定范围，三图编辑可自定义比例_2105852489856798722.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2105852489856798722.json`

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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **84%**（48/57）

**有卡**：`LoadImage`、`GoohaiUniversalSlider`、`ResolutionSelector`、`QwenImage21ConfigPreparer_EditUtils`、`QwenImage21ModelConfig_EditUtils`、`PathchSageAttentionKJ`、`QwenImage21EditApply_EditUtils`、`ConditioningZeroOut`、`VAEDecode`、`EmptyLatentImage`、`CropWithPadInfo_EditUtils`、`KSampler`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EditTextEncode_EditUtils`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**缺卡**（3）：`Fast Bypasser (rgthree)`、`workflow>遮罩逻辑`、`布尔孤海`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>遮罩逻辑` 知识库中没有该节点类型的任何知识
- 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
