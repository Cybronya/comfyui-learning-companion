---
name: unknown_workflow_video_upscale_26
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.821
common_nodes: [CM_IntToBool, ImageUpscaleWithModel, InversionDemoLazySwitch, LoadImage, MathExpression|pysssss, Primitive integer [Crystools], UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/第3代视频高清放大工作流 - Transformer_ViT_UDVAE架构_1980105609007763458.json, 平台全量/第4代视频高清放大工作流 - Diffusion扩散式架构_1980606736723787777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/第3代视频高清放大工作流 - Transformer_ViT_UDVAE架构_1980105609007763458.json、平台全量/第4代视频高清放大工作流 - Diffusion扩散式架构_1980606736723787777.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CM_IntToBool`
- `ImageUpscaleWithModel`
- `InversionDemoLazySwitch`
- `LoadImage`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
