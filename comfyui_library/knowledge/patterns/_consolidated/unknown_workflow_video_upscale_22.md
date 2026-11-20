---
name: unknown_workflow_video_upscale_22
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [ImageScaleBy, ImageUpscaleWithModel, JWImageResizeByLongerSide, LoadImage, PreviewImage, RHBatchImages:, RebatchImages, RunningHub_FramePack, SeargePromptText, UpscaleModelLoader, VHS_VideoCombine, easy int]
problems: []
missing: []
members: [平台全量/FramePack 最新首尾帧1080p版_1914167379557871618.json, 视频生成/图生视频/FramePack 最新图生视_首尾帧视频1080p版【自动优化词】_1932958502274957313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/FramePack 最新首尾帧1080p版_1914167379557871618.json、视频生成/图生视频/FramePack 最新图生视_首尾帧视频1080p版【自动优化词】_1932958502274957313.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `JWImageResizeByLongerSide`
- `LoadImage`
- `PreviewImage`
- `RHBatchImages:`
- `RebatchImages`
- `RunningHub_FramePack`
- `SeargePromptText`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 1/2 个有
- `ConcatTextOfUtils` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
