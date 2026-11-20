---
name: unknown_workflow_upscale_clip_checkpoint_9
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, LoadImage, SaveImage, UltimateSDUpscale, UpscaleModelLoader]
problems: []
missing: []
members: [平台全量/图片一键高清放大_2033138332913377281.json, 平台全量/普通放大_2013440445044494338.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/图片一键高清放大_2033138332913377281.json、平台全量/普通放大_2013440445044494338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `LoadImage`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
