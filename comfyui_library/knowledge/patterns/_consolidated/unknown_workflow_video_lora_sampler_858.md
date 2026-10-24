---
name: unknown_workflow_video_lora_sampler_858
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.948
common_nodes: [BasicMath, CLIPLoader, CLIPTextEncode, FloatConstant, INTConstant, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, StringConcatenate, ToFloat, ToInt, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【AI播草机】WAN2.2首帧尾帧视频生成_2031354841515171842.json, 视频生成/图生视频/【AI播草机】WAN2.2首帧视频生成_2031004369734344706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_858

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【AI播草机】WAN2.2首帧尾帧视频生成_2031354841515171842.json、视频生成/图生视频/【AI播草机】WAN2.2首帧视频生成_2031004369734344706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicMath`
- `CLIPLoader`
- `CLIPTextEncode`
- `FloatConstant`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `StringConcatenate`
- `ToFloat`
- `ToInt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
