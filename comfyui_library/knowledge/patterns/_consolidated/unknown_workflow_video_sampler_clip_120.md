---
name: unknown_workflow_video_sampler_clip_120
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9392
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, JjkText, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, Primitive integer [Crystools], RHHiddenNodes, SimpleMath+, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2058158011801235458.json, 视频生成/图生视频/1987176720614797313.json, 视频生成/图生视频/2059600905217069058.json, 视频生成/图生视频/1987901489630875649.json, 视频生成/图生视频/1988297907646414850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2058158011801235458.json、视频生成/图生视频/1987176720614797313.json、视频生成/图生视频/2059600905217069058.json、视频生成/图生视频/1987901489630875649.json、视频生成/图生视频/1988297907646414850.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `JjkText`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `SimpleMath+`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `WanImageToVideo` —— 4/5 个有
- `SaveImage` —— 2/5 个有
- `TT_img_enc_v2` —— 2/5 个有
- `CompressImages` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `VHS_SelectFilename` —— 1/5 个有
- `WanFirstLastFrameToVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 5 | 82% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | normal | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，5 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 normal，5 个样本，一致性 100%
