---
name: unknown_workflow_video_lora_sampler_801
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.884
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1974340627162861570.json, 视频生成/图生视频/1952297312313880577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_801

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1974340627162861570.json、视频生成/图生视频/1952297312313880577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `PurgeVRAM_UTK` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `TorchCompileModel` —— 1/2 个有
- `WanVideoNAG` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 14.5 | - | 2 | 41% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 14.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 41%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 23，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
