---
name: unknown_workflow_video_clip_vae_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6585
common_nodes: [AILab_MiniCPM_4_V, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CR Prompt Text, GetNode, ImageFromBatch+, ImageResizeKJv2, ImpactSwitch, JjkText, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewImage, Primitive integer [Crystools], RHHiddenNodes, RH_LLMAPI_NODE, SetNode, ShowText|pysssss, SimpleMath+, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1981286128290529281.json, 视频生成/图生视频/1981040376029003777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_vae_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1981286128290529281.json、视频生成/图生视频/1981040376029003777.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_MiniCPM_4_V`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CR Prompt Text`
- `GetNode`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `JjkText`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `WanMoeKSampler` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 1 | 100% |
| 重绘幅度 | beta57 | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 beta57，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
