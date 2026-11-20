---
name: unknown_workflow_video_lora_sampler_701
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8565
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ImageConcatMulti, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, ResizeImageMaskNode, SAM3_VideoTrack, SCAIL2ColoredMask, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanContextWindowsManual, WanSCAILToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/视频人物替换-极速版_2080134823569608705.json, 平台全量/视频转绘工作流_2082077916808175617.json, 数字人/数字人/SCAIL V2人物动作迁移工作流_2081619582183362562.json, 数字人/数字人/SCAIL V2视频人物替换+影视二创_2081623383111979009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_701

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/视频人物替换-极速版_2080134823569608705.json、平台全量/视频转绘工作流_2082077916808175617.json、数字人/数字人/SCAIL V2人物动作迁移工作流_2081619582183362562.json、数字人/数字人/SCAIL V2视频人物替换+影视二创_2081623383111979009.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `VHS_SelectImages` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
