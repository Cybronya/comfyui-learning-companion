---
name: unknown_workflow_upscale_clip_unet_3
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92125
common_nodes: [CLIPTextEncode, LoadImage, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX1 动漫画质修复放大_2016701427971792897.json, 图片生成/图生图/SD放大（Flux版）_1984982029756416002.json, 图片生成/图生图/放大_1956860937392066561.json, 图片生成/图生图/🚀老许Gary：Z+SD图像修复放大_2037198846140354562.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX1 动漫画质修复放大_2016701427971792897.json、图片生成/图生图/SD放大（Flux版）_1984982029756416002.json、图片生成/图生图/放大_1956860937392066561.json、图片生成/图生图/🚀老许Gary：Z+SD图像修复放大_2037198846140354562.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `DualCLIPLoader` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `CLIPLoader` —— 1/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `Joy_caption` —— 1/4 个有
- `Joy_caption_load` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
