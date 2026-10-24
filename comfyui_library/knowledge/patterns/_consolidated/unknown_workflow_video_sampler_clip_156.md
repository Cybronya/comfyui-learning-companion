---
name: unknown_workflow_video_sampler_clip_156
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.925
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/fusionx 图生视频官方工作流_1923740000817434626.json, 视频生成/图生视频/wan2.1图生视频官流【教学】_2001218246663602177.json, 视频生成/图生视频/wan2.1首尾帧视频【教学】_2000392269180137473.json, 视频生成/图生视频/动态壁纸无缝循环_1955953531285065730.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_156

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/fusionx 图生视频官方工作流_1923740000817434626.json、视频生成/图生视频/wan2.1图生视频官流【教学】_2001218246663602177.json、视频生成/图生视频/wan2.1首尾帧视频【教学】_2000392269180137473.json、视频生成/图生视频/动态壁纸无缝循环_1955953531285065730.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ApplySageAttention` —— 2/4 个有
- `PatchModelPatcherOrder` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `WanImageToVideo` —— 2/4 个有
- `CR Upscale Image` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `TorchCompileModelWanVideo` —— 1/4 个有
- `TorchCompileModelWanVideoV2` —— 1/4 个有
- `WanFirstLastFrameToVideo` —— 1/4 个有
- `WanImageToVideo_F2` —— 1/4 个有
- `mxSlider` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 6 - 10 | 4 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 4 | 0% |
| 采样算法 | uni_pc | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 6 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 uni_pc，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
