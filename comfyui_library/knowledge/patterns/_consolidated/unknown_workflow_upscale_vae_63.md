---
name: unknown_workflow_upscale_vae_63
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.573667
common_nodes: [Any Switch (rgthree), Bookmark (rgthree), Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PlaySound|pysssss, PrimitiveFloat, PrimitiveStringMultiline, RHHiddenNodes, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, easy int]
problems: []
missing: []
members: [图片生成/图生图/图片高清修复_2032779228466384897.json, 平台全量/图片超清重绘放大V1_2012862147813974018.json, 数字人/数字人/图片重绘高清放大-阿浩_2026840504096268290.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_63

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图片高清修复_2032779228466384897.json、平台全量/图片超清重绘放大V1_2012862147813974018.json、数字人/数字人/图片重绘高清放大-阿浩_2026840504096268290.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 3 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `StringLength` —— 2/3 个有
- `Switch any [Crystools]` —— 2/3 个有
- `easy compare` —— 2/3 个有
- `IntToText` —— 1/3 个有
- `LoraLoaderVanilla` —— 1/3 个有
- `SeedVR2TorchCompileSettings` —— 1/3 个有
- `StringToInt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
