---
name: unknown_workflow_sampler_vae_64
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9085
common_nodes: [CreateVideo, ImageResize+, LoadImage, PDRatioSelector, PreviewImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, RH_Captioner, SaveVideo, StringConcatenate, StringConstantMultiline]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 FL2VA开源版-尾参考生视频_2084223496103747586.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-首帧参考生视频_2084209553008316417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_64

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 FL2VA开源版-尾参考生视频_2084223496103747586.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-首帧参考生视频_2084209553008316417.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateVideo`
- `ImageResize+`
- `LoadImage`
- `PDRatioSelector`
- `PreviewImage`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3FL2VAEncode`
- `RHMiniMaxH3FL2VAModelLoader`
- `RHMiniMaxH3FL2VATarget`
- `RHMiniMaxH3FL2VATextEncoderLoader`
- `RHMiniMaxH3FL2VAVAELoader`
- `RH_Captioner`
- `SaveVideo`
- `StringConcatenate`
- `StringConstantMultiline`

**可变部分**（部分 workflow 才有）：
- `CustomAddLabel` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `RHMiniMaxH3FL2VAFirstFrameCondition` —— 1/2 个有
- `RHMiniMaxH3FL2VALastFrameCondition` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
