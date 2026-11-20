---
name: unknown_workflow_upscale_clip_unet_2
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.87725
common_nodes: [CLIPTextEncode, DualCLIPLoader, LoadImage, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/18.tonnie-flux-sd放大_1995849520225345537.json, 图片生成/图生图/1FINAL- 宫格图拆分单图高清放大_2057650385833259010.json, 图片生成/图生图/1FINAL- 宫格图拆分放大_2057284561985425409.json, 图片生成/图生图/tonnie-flux重绘放大_2_1995868550608957441.json, 图片生成/图生图/九宫格拆分&放大_2017772946860810242.json, 图片生成/图生图/宫格图拆分放大_2058361243999760385.json, 图片生成/图生图/宫格图拆分放大_2058378371293343746.json, 图片生成/图生图/石头--高清_1955252690000363521.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/18.tonnie-flux-sd放大_1995849520225345537.json、图片生成/图生图/1FINAL- 宫格图拆分单图高清放大_2057650385833259010.json、图片生成/图生图/1FINAL- 宫格图拆分放大_2057284561985425409.json、图片生成/图生图/tonnie-flux重绘放大_2_1995868550608957441.json、图片生成/图生图/九宫格拆分&放大_2017772946860810242.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/8 个有
- `easy imageSplitGrid` —— 5/8 个有
- `FluxGuidance` —— 3/8 个有
- `ModelSamplingFlux` —— 2/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `Int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
