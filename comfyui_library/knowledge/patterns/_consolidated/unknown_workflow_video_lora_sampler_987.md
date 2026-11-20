---
name: unknown_workflow_video_lora_sampler_987
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.466
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/视频-Wan2.2首中尾帧FMLF，首中尾三帧参考_2068809925526118401.json, 视频生成/图生视频/首尾祯动感转场_1994048317403447297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_987

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/视频-Wan2.2首中尾帧FMLF，首中尾三帧参考_2068809925526118401.json、视频生成/图生视频/首尾祯动感转场_1994048317403447297.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：47%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `CM_IntToFloat` —— 1/2 个有
- `CR Seed` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 86% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
