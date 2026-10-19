---
name: unknown_workflow_video_sampler_clip_219
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8555
common_nodes: [AILab_QwenVL, CLIPTextEncode, CR Text, GetImageSize, ImageScale, ImpactSwitch, JWInteger, KSamplerAdvanced, LayerUtility: BooleanOperatorV2, LayerUtility: If , LoadImage, MathExpression|pysssss, PreviewAny, PreviewImage, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VAEDecode, VHS_VideoCombine, WanImageToVideo, easy imageScaleDownToSize, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1982274042864517122.json, 视频生成/图生视频/1979813439872864257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_219

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1982274042864517122.json、视频生成/图生视频/1979813439872864257.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPTextEncode`
- `CR Text`
- `GetImageSize`
- `ImageScale`
- `ImpactSwitch`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: If `
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewAny`
- `PreviewImage`
- `RIFE VFI`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy imageScaleDownToSize`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有
- `workflow>SMOOTH MIX-WAN2.2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
