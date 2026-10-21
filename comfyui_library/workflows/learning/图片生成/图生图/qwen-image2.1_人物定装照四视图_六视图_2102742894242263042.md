---
key: 图片生成/图生图/qwen-image2.1_人物定装照四视图_六视图_2102742894242263042.json
name: qwen-image2.1_人物定装照四视图_六视图_2102742894242263042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image2.1_人物定装照四视图_六视图_2102742894242263042.json
hash: 0f59c36592caedc7
coverage: 0.448276
learned_at: 2026-10-21 00:46:09
nodes: [LayerUtility: ImageScaleByAspectRatio V2, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, PreviewAny, TextEncodeQwenImage21, PrimitiveInt, PrimitiveInt, easy seed, VAEDecode, GetNode, GetNode, UNETLoader, QwenImage21Cache, CLIPLoader, SetNode, SetNode, SetNode, SaveImage, PrimitiveBoolean, KSampler, GetNode, VAELoader, ComfySwitchNode, EmptyLatentImage, PrimitiveInt, ComfySwitchNode, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 875063224334553, "steps": 40, "width": 2048}
---

# 图片生成/图生图/qwen-image2.1_人物定装照四视图_六视图_2102742894242263042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image2.1_人物定装照四视图_六视图_2102742894242263042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy seed`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SaveImage`
- `PrimitiveBoolean`
- `KSampler` ★核心
- `GetNode`
- `VAELoader`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `PrimitiveInt`
- `ComfySwitchNode`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `875063224334553`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `2048`
- `height` = `1152`
- `batch_size` = `1`

## 知识

覆盖率 **45%**（13/29）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`easy seed`、`VAEDecode`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`SaveImage`、`PrimitiveBoolean`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
