---
name: unknown_workflow_video_sampler_clip_259
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.705
common_nodes: [CLIPLoader, CLIPTextEncode, ImpactSwitch, KSamplerAdvanced, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_NODE, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979825054756278274.json, 视频生成/文生视频/1955095898542018561.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_259

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979825054756278274.json、视频生成/文生视频/1955095898542018561.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImpactSwitch`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `Wan22PromptSelector` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 50% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 80% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
