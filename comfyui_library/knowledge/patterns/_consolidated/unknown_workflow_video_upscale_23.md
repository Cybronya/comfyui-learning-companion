---
name: unknown_workflow_video_upscale_23
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [ImageUpscaleWithModelCUDAspeedFixed, JWInteger, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Upscale-CUDAspeed极速视频高清修复放大V1_1980937507103789058.json, 平台全量/（全能视频S 25S）Upscale-CUDAspeed极速视频高清修复放大V1_1981357960754536450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Upscale-CUDAspeed极速视频高清修复放大V1_1980937507103789058.json、平台全量/（全能视频S 25S）Upscale-CUDAspeed极速视频高清修复放大V1_1981357960754536450.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageUpscaleWithModelCUDAspeedFixed`
- `JWInteger`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
