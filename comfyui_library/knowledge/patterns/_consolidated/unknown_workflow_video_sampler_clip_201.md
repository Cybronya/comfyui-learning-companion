---
name: unknown_workflow_video_sampler_clip_201
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.658
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetImageRangeFromBatch, GetImageSize+, GetNode, ImageResizeKJv2, ImageScaleBy, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression_UTK, ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, SaveImage, Seed (rgthree), SetNode, TT_img_enc, TT_img_enc_v2, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, easy imageListToImageBatch, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2044131826918236162.json, 视频生成/图生视频/1987211259793838082.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_201

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2044131826918236162.json、视频生成/图生视频/1987211259793838082.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSize+`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression_UTK`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `TT_img_enc`
- `TT_img_enc_v2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `easy imageListToImageBatch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `ImageListToImageBatch` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
