---
name: unknown_workflow_video_sampler_clip_192
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.969
common_nodes: [CLIPLoader, CLIPTextEncode, DWPreprocessor, DepthAnythingPreprocessor, ImageBlend, LoadImage, ModelSamplingSD3, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo, WanVideoKsampler]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1945140520291323905.json, 视频生成/图生视频/1956332696773513217.json, 视频生成/图生视频/1956176405350547458.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_192

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1945140520291323905.json、视频生成/图生视频/1956332696773513217.json、视频生成/图生视频/1956176405350547458.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
- `DepthAnythingPreprocessor`
- `ImageBlend`
- `LoadImage`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoKsampler`

**可变部分**（部分 workflow 才有）：
- `Display Any (rgthree)` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | ddpm | - | 2 | 100% |
| 调度器 | ddim_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddpm，2 个样本，一致性 100%
- 调度器 最常用 ddim_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
