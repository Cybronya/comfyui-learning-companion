---
name: unknown_workflow_upscale_clip_checkpoint_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.874
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, LoadImage, SaveImage, UltimateSDUpscale, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/图生图高清放大_1976293746537046018.json, 图片生成/图生图/画质修复_2071077359658299393.json, 平台全量/SUPIR-8K高清放大_1969066724542849025.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图生图高清放大_1976293746537046018.json、图片生成/图生图/画质修复_2071077359658299393.json、平台全量/SUPIR-8K高清放大_1969066724542849025.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `LoadImage`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `AV_VAELoader` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `SUPIR_Upscale` —— 1/3 个有
- `WD14Tagger|pysssss` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
