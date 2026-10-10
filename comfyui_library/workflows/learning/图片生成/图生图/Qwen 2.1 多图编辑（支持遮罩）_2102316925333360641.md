---
key: 图片生成/图生图/Qwen 2.1 多图编辑（支持遮罩）_2102316925333360641.json
name: Qwen 2.1 多图编辑（支持遮罩）_2102316925333360641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 2.1 多图编辑（支持遮罩）_2102316925333360641.json
hash: a00463fd04841900
coverage: 0.628571
learned_at: 2026-10-10 20:48:04
nodes: [Image Comparer (rgthree), LoadImage, GoohaiUniversalSlider, LoadImage, ComfySwitchNode, ResolutionSelector, QwenImage21ConfigPreparer_EditUtils, QwenImage21ConfigPreparer_EditUtils, QwenImage21ModelConfig_EditUtils, PathchSageAttentionKJ, QwenImage21EditApply_EditUtils, ConditioningZeroOut, VAEDecode, EmptyLatentImage, CropWithPadInfo_EditUtils, KSampler, CropWithPadInfo_EditUtils, Fast Bypasser (rgthree), 布尔孤海, SaveImage, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, VAELoader, EditTextEncode_EditUtils, LoadImage, workflow>遮罩逻辑, QwenImage21ConfigPreparer_EditUtils, PrimitiveStringMultiline, 孤海注释]
patterns: []
missing: [Fast Bypasser (rgthree), workflow>遮罩逻辑, 布尔孤海]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 392705312548116, "steps": 25, "width": 1024}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>遮罩逻辑` 知识库中没有该节点类型的任何知识, 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen 2.1 多图编辑（支持遮罩）_2102316925333360641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 2.1 多图编辑（支持遮罩）_2102316925333360641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
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
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EditTextEncode_EditUtils`
- `LoadImage`
- `workflow>遮罩逻辑`
- `QwenImage21ConfigPreparer_EditUtils`
- `PrimitiveStringMultiline`
- `孤海注释`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `392705312548116`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（22/35）

**有卡**：`LoadImage`、`GoohaiUniversalSlider`、`ResolutionSelector`、`QwenImage21ConfigPreparer_EditUtils`、`QwenImage21ModelConfig_EditUtils`、`PathchSageAttentionKJ`、`QwenImage21EditApply_EditUtils`、`ConditioningZeroOut`、`VAEDecode`、`EmptyLatentImage`、`CropWithPadInfo_EditUtils`、`KSampler`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EditTextEncode_EditUtils`

**缺卡**（3）：`Fast Bypasser (rgthree)`、`workflow>遮罩逻辑`、`布尔孤海`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>遮罩逻辑` 知识库中没有该节点类型的任何知识
- 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识
