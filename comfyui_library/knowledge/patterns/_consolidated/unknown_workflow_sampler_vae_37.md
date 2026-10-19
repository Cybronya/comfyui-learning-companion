---
name: unknown_workflow_sampler_vae_37
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.957
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3Ref2VAEncode, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3  图生视频  多图生视频_2084914452868194306.json, 视频生成/图生视频/MiniMax H3 AI提示词润色｜双角色有声微短剧｜两图一句话_2087013189312667650.json, 视频生成/图生视频/MiniMax H3｜多模态单图15秒急速_2085393570013474817.json, 视频生成/图生视频/MiniMax H3｜多模态参考原生有声视频｜双图15秒自媒体导演台 优化版_2086558677456216065.json, 视频生成/图生视频/MiniMax H3｜多模态参考原生有声视频｜双图15秒自媒体导演台_2084281246422753281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_37

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3  图生视频  多图生视频_2084914452868194306.json、视频生成/图生视频/MiniMax H3 AI提示词润色｜双角色有声微短剧｜两图一句话_2087013189312667650.json、视频生成/图生视频/MiniMax H3｜多模态单图15秒急速_2085393570013474817.json、视频生成/图生视频/MiniMax H3｜多模态参考原生有声视频｜双图15秒自媒体导演台 优化版_2086558677456216065.json、视频生成/图生视频/MiniMax H3｜多模态参考原生有声视频｜双图15秒自媒体导演台_2084281246422753281.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateVideo`
- `LoadImage`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3Ref2VAEncode`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3Ref2VAModelLoader`
- `RHMiniMaxH3Ref2VATarget`
- `RHMiniMaxH3Ref2VATextEncoderLoader`
- `RHMiniMaxH3Ref2VAVAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `StringConstantMultiline` —— 4/5 个有
- `CLIPLoader` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有
- `TextGenerate` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
