---
name: unknown_workflow_inpaint_clip_checkpoint
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.828667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Image Comparer (rgthree), InpaintCropImproved, InpaintStitchImproved, Int, LoadImage, RH_Translator, SAM3_Detect, SaveImage, Text]
problems: []
missing: []
members: [图片生成/图生图/image2模型根据参考车图改KV车色_2071485906858627074.json, 图片生成/图生图/根据汽车参考图改KV车漆颜色_2064160972738228225.json, 图片生成/图生图/车牌替换_2088155400439947265.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/image2模型根据参考车图改KV车色_2071485906858627074.json、图片生成/图生图/根据汽车参考图改KV车漆颜色_2064160972738228225.json、图片生成/图生图/车牌替换_2088155400439947265.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `Int`
- `LoadImage`
- `RH_Translator`
- `SAM3_Detect`
- `SaveImage`
- `Text`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `LayerColor: ColorAdapter` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/3 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
