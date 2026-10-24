---
name: unknown_workflow_video_sampler_clip_210
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.927
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningCombine, DWPreprocessor, ImageBatchMultiple+, ImageConcanate, ImageConcatFromBatch, ImageResize+, ImageResizeKJv2, KSampler, LoadImage, ModelSamplingSD3, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [视频生成/文生视频/VACE_Skyreels_V3_R2V_Merge骨骼引导视频_2025493219651362817.json, 视频生成/文生视频/万相 多人运动迁移控制 VACE+Phantom融合模ComfyUI工作流_1954000374674051073.json, 视频生成/文生视频/万相 多人运动迁移控制 VACE+Phantom融合模ComfyUI工作流_2049298868713558017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_210

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/VACE_Skyreels_V3_R2V_Merge骨骼引导视频_2025493219651362817.json、视频生成/文生视频/万相 多人运动迁移控制 VACE+Phantom融合模ComfyUI工作流_1954000374674051073.json、视频生成/文生视频/万相 多人运动迁移控制 VACE+Phantom融合模ComfyUI工作流_2049298868713558017.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningCombine`
- `DWPreprocessor`
- `ImageBatchMultiple+`
- `ImageConcanate`
- `ImageConcatFromBatch`
- `ImageResize+`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `ImageBatch` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_GetImageCount` —— 2/3 个有
- `WanPhantomSubjectToVideo` —— 2/3 个有
- `WanVaceToVideo` —— 2/3 个有
- `WanVacePhantomSimpleV2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 15 | 3 | 89% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 15，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
