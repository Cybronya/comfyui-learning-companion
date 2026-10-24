---
name: unknown_workflow_clip_unet_vae_23
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.835
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImpactSwitch, PreviewAny, RHHiddenNodes, RH_LLMAPI_NODE, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/文生图 Z-Image，AI 视觉生成新选择_2018922072969318402.json, 图片生成/文生图/Z-Image + 文生图 + qwen3 + 图片高清放大_2037536709897887745.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/文生图 Z-Image，AI 视觉生成新选择_2018922072969318402.json、图片生成/文生图/Z-Image + 文生图 + qwen3 + 图片高清放大_2037536709897887745.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactSwitch`
- `PreviewAny`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
