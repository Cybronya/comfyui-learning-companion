---
key: 图片生成/图生图/edit-2509-lightningv2.0-8steps 单图编辑 一致性 便宜 图生图_1989150846225100801.json
name: edit-2509-lightningv2.0-8steps 单图编辑 一致性 便宜 图生图_1989150846225100801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/edit-2509-lightningv2.0-8steps 单图编辑 一致性 便宜 图生图_1989150846225100801.json
hash: 336143823401d167
coverage: 0.52
learned_at: 2026-10-23 11:34:40
nodes: [MarkdownNote, NunchakuQwenImageDiTLoader, ModelSamplingAuraFlow, CFGNorm, PreviewImage, ImageStitch, SetNode, GetNode, SetNode, GetNode, ConditioningZeroOut, LayerFilter: HDREffects, GetNode, PreviewImage, Image Comparer (rgthree), GetNode, GetNode, MarkdownNote, LoadImage, NunchakuQwenImageLoraLoader, TextEncodeQwenImageEditPlus_lrzjason, CLIPLoader, VAELoader, KSampler (Efficient), SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 357429993967450, "steps": 8}
---

# 图片生成/图生图/edit-2509-lightningv2.0-8steps 单图编辑 一致性 便宜 图生图_1989150846225100801.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/edit-2509-lightningv2.0-8steps 单图编辑 一致性 便宜 图生图_1989150846225100801.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（25 个）：
- `MarkdownNote`
- `NunchakuQwenImageDiTLoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PreviewImage`
- `ImageStitch`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ConditioningZeroOut`
- `LayerFilter: HDREffects`
- `GetNode`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `LoadImage`
- `NunchakuQwenImageLoraLoader` ★核心
- `TextEncodeQwenImageEditPlus_lrzjason`
- `CLIPLoader`
- `VAELoader`
- `KSampler (Efficient)` ★核心
- `SaveImage`

## 关键参数

- `seed` = `357429993967450`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（13/25）

**有卡**：`NunchakuQwenImageDiTLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`ImageStitch`、`ConditioningZeroOut`、`LayerFilter: HDREffects`、`LoadImage`、`NunchakuQwenImageLoraLoader`、`TextEncodeQwenImageEditPlus_lrzjason`、`CLIPLoader`、`VAELoader`、`KSampler (Efficient)`、`SaveImage`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGNorm、KSampler (Efficient)、TextEncodeQwenImageEditPlus_lrzjason、NunchakuQwenImageLoraLoader
