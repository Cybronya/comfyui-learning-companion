---
name: unknown_workflow_video_upscale_24
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8015
common_nodes: [Free_Video_Memory, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, Video_Upscale_With_Model]
problems: []
missing: []
members: [平台全量/VideoUpscaleWithModel=视频高清放大_1977343820092317697.json, 平台全量/非扩散快速视频放大修复V2（模型可选版）_1930631973050449921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/VideoUpscaleWithModel=视频高清放大_1977343820092317697.json、平台全量/非扩散快速视频放大修复V2（模型可选版）_1930631973050449921.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `Free_Video_Memory`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `Video_Upscale_With_Model`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
