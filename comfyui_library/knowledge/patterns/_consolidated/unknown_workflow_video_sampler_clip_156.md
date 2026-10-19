---
name: unknown_workflow_video_sampler_clip_156
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.807
common_nodes: [CLIPLoader, CLIPTextEncode, ImageBatchMulti, ImageConcatMulti, ImageResizeKJv2, Int, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, Qwen3_VQA, RIFE VFI, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMultiFrameRefToVideo, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2031688685132976129.json, 视频生成/图生视频/2044969480081641474.json, 视频生成/图生视频/2009925117761032194.json, 视频生成/图生视频/2023651384347860994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_156

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2031688685132976129.json、视频生成/图生视频/2044969480081641474.json、视频生成/图生视频/2009925117761032194.json、视频生成/图生视频/2023651384347860994.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `RIFE VFI`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMultiFrameRefToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 3/4 个有
- `INTConstant` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `CustomAddLabel` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImagesFromBatchIndexed` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
