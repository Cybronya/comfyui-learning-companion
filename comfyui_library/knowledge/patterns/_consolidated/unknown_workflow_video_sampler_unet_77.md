---
name: unknown_workflow_video_sampler_unet_77
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.882
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageResize+, JjkText, KSampler, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PreviewAny, UNETLoader, VAEDecode, VAEDecodeAudio, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3-首帧参考图生视频-智能分镜助手-本地加速开源版v3_2084497299471953922.json, 视频生成/文生视频/MiniMaxH3-首帧参考图生视频-智能分镜助手-本地加速开源版v3_2084236513688252418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_77

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3-首帧参考图生视频-智能分镜助手-本地加速开源版v3_2084497299471953922.json、视频生成/文生视频/MiniMaxH3-首帧参考图生视频-智能分镜助手-本地加速开源版v3_2084236513688252418.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageResize+`
- `JjkText`
- `KSampler`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `Vignette` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
