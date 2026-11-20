---
name: unknown_workflow_upscale_clip_checkpoint_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ImageResizeKJ, LoadImage, SEGSPreview, SaveImage, UltimateSDUpscale, UpscaleModelLoader, workflow>参数设置, workflow>面部参考]
problems: []
missing: []
members: [图片生成/图生图/全能图片G4o-皮克斯风格转绘  可爱手办3D_1916382300597059585.json, 图片生成/图生图/全能图片G4o-皮克斯风格转绘 面部参考 可爱手办3D虚拟数字人-StarAI_1910489911601102850.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能图片G4o-皮克斯风格转绘  可爱手办3D_1916382300597059585.json、图片生成/图生图/全能图片G4o-皮克斯风格转绘 面部参考 可爱手办3D虚拟数字人-StarAI_1910489911601102850.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageResizeKJ`
- `LoadImage`
- `SEGSPreview`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `workflow>参数设置`
- `workflow>面部参考`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
