---
name: unknown_workflow_video_lora_sampler_806
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.867
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ImageConcatMulti, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, ResizeImageMaskNode, SAM3_VideoTrack, SCAIL2ColoredMask, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanContextWindowsManual, WanSCAILToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/SCAIL V2人物动作迁移工作流_2081619582183362562.json, 数字人/数字人/SCAIL V2视频人物替换+影视二创_2081623383111979009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_806

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/SCAIL V2人物动作迁移工作流_2081619582183362562.json、数字人/数字人/SCAIL V2视频人物替换+影视二创_2081623383111979009.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ImageConcatMulti`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `ResizeImageMaskNode`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanContextWindowsManual`
- `WanSCAILToVideo`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
