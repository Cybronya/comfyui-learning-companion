---
name: unknown_workflow_upscale_clip_checkpoint_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9445
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, LoadImage, SaveImage, UltimateSDUpscale, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/图生图高清放大_1976293746537046018.json, 图片生成/图生图/画质修复_2071077359658299393.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图生图高清放大_1976293746537046018.json、图片生成/图生图/画质修复_2071077359658299393.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `LoadImage`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `AV_VAELoader` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
