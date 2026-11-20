---
name: unknown_workflow_upscale_vae_49
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5425
common_nodes: [Any Switch (rgthree), Bookmark (rgthree), Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PlaySound|pysssss, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RHHiddenNodes, RH_Captioner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, StringLength, Switch any [Crystools], easy compare, easy int]
problems: []
missing: []
members: [图片生成/图生图/图片高清修复_2032779228466384897.json, 数字人/数字人/图片重绘高清放大-阿浩_2026840504096268290.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_49

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图片高清修复_2032779228466384897.json、数字人/数字人/图片重绘高清放大-阿浩_2026840504096268290.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Bookmark (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PlaySound|pysssss`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `RH_Captioner`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `StringLength`
- `Switch any [Crystools]`
- `easy compare`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderVanilla` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
