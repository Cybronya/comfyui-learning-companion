---
name: unknown_workflow_video_sampler_clip_234
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.904
common_nodes: [CLIPTextEncode, KSampler, LoadImage, ModelSamplingSD3, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2058812431790596098.json, 视频生成/图生视频/1935754825865097217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_234

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2058812431790596098.json、视频生成/图生视频/1935754825865097217.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `ClipLoaderGGUF` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | lcm | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
