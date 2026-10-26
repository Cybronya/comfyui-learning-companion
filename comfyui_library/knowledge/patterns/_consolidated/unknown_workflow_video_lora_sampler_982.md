---
name: unknown_workflow_video_lora_sampler_982
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9735
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/最新WAN2.2-14B图生视频_1949839253868077058.json, 视频生成/文生视频/Wan2.2&lightx2v加速_1950385703961149441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_982

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/最新WAN2.2-14B图生视频_1949839253868077058.json、视频生成/文生视频/Wan2.2&lightx2v加速_1950385703961149441.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStarAndInit` —— 1/2 个有
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `WanVideoEnhanceAVideoKJ` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 75% |
| 采样算法 | 2.25 | - | 2 | 44% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本
- 采样算法 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 调度器 最常用 euler，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
