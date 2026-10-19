---
name: unknown_workflow_video_upscale_vae_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [CR Text, Float, GetVideoComponents, INTConstant, ImageResizeKJv2, ImageScaleToTotalPixels, JWInteger, LoadImage, PreviewAny, PreviewImage, RH_LLMAPI_Pro_Node, RunningHubHeliosI2V, RunningHubHeliosModelLoader, SaveVideo, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, Text, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2039889782293139458.json, 视频生成/图生视频/2031717752821522434.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2039889782293139458.json、视频生成/图生视频/2031717752821522434.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `Float`
- `GetVideoComponents`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `RunningHubHeliosI2V`
- `RunningHubHeliosModelLoader`
- `SaveVideo`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `Text`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
