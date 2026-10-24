---
name: unknown_workflow_upscale_lora_clip_6
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83125
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, ColorMatch, GetImageSize+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, SaveImage, SimpleMathDual+, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/zimage高清放大工作流_2059201384171528193.json, 图片生成/图生图/▶▶F2K图片高清放大_2082501091522080769.json, 图片生成/图生图/高清放大_2058961643857596418.json, 图片生成/文生图/图片高清放大_2060392283224231937.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/zimage高清放大工作流_2059201384171528193.json、图片生成/图生图/▶▶F2K图片高清放大_2082501091522080769.json、图片生成/图生图/高清放大_2058961643857596418.json、图片生成/文生图/图片高清放大_2060392283224231937.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `ColorMatch`
- `GetImageSize+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `SaveImage`
- `SimpleMathDual+`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LayerColor: BrightnessContrastV2` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `WD14Tagger|pysssss` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
