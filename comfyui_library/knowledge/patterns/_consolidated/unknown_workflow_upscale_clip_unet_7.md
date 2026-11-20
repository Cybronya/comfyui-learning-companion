---
name: unknown_workflow_upscale_clip_unet_7
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.920667
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, LoadImage, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux图像放大清晰化增加细节 人物模特清晰化_1935210187508600834.json, 平台全量/FLUX高清放大+Lora_1942154468412780545.json, 平台全量/SD高清修复_1938174548967604225.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux图像放大清晰化增加细节 人物模特清晰化_1935210187508600834.json、平台全量/FLUX高清放大+Lora_1942154468412780545.json、平台全量/SD高清修复_1938174548967604225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.66 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
