---
name: unknown_workflow_video_sampler_clip_85
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.618429
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2012914151470927874.json, 视频生成/图生视频/2012826950003331074.json, 视频生成/图生视频/2042865188126334978.json, 视频生成/图生视频/2011676327186796545.json, 视频生成/图生视频/2016912682649128961.json, 视频生成/图生视频/2001566408855154689.json, 视频生成/图生视频/1991786549960601602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2012914151470927874.json、视频生成/图生视频/2012826950003331074.json、视频生成/图生视频/2042865188126334978.json、视频生成/图生视频/2011676327186796545.json、视频生成/图生视频/2016912682649128961.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 6/7 个有
- `ModelSamplingSD3` —— 6/7 个有
- `RIFE VFI` —— 6/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `WanFirstLastFrameToVideo` —— 5/7 个有
- `ImageBatchMulti` —— 3/7 个有
- `Int` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `WanMultiFrameRefToVideo` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `GetImagesFromBatchIndexed` —— 2/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `LoadImageFromURL` —— 2/7 个有
- `PainterI2V` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `FL_RIFE` —— 1/7 个有
- `PainterI2V_Wan2_2` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `ttN seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 57% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 7 | 80% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | normal | - | 7 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，7 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 normal，7 个样本，一致性 71%
