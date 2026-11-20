---
name: unknown_workflow_sampler_vae_76
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9705
common_nodes: [DiffusersMVModelMakeup, DiffusersMVPipelineLoader, DiffusersMVSampler, DiffusersMVSchedulerLoader, DiffusersMVVaeLoader, ImageRGBA2RGB, ImageResizeAdvanced, LoadImage, RH_Captioner, SaveImage, easy cleanGpuUsed, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/MVAdapter多视角图生图工作流_1927686144085868546.json, 平台全量/MVAdapter多视角图生图工作流_1879538907237834754.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_76

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/MVAdapter多视角图生图工作流_1927686144085868546.json、平台全量/MVAdapter多视角图生图工作流_1879538907237834754.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `DiffusersMVModelMakeup`
- `DiffusersMVPipelineLoader`
- `DiffusersMVSampler`
- `DiffusersMVSchedulerLoader`
- `DiffusersMVVaeLoader`
- `ImageRGBA2RGB`
- `ImageResizeAdvanced`
- `LoadImage`
- `RH_Captioner`
- `SaveImage`
- `easy cleanGpuUsed`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageBatchToList` —— 1/2 个有
- `MaxNode` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
