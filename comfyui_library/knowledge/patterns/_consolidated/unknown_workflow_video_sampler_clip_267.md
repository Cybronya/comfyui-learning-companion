---
name: unknown_workflow_video_sampler_clip_267
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9455
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageRangeFromBatch, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/最新高动效wan2.2官方图生视频工作流_1991017760861921282.json, 视频生成/图生视频/真王炸！wan2.2一键核爆_1955241155534340098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_267

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/最新高动效wan2.2官方图生视频工作流_1991017760861921282.json、视频生成/图生视频/真王炸！wan2.2一键核爆_1955241155534340098.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CR Text Replace` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PainterI2V` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
