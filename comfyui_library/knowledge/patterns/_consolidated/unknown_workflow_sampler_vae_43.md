---
name: unknown_workflow_sampler_vae_43
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.942333
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3Ref2VAEncode, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 Ref2VA开源版_2084935927293632513.json, 视频生成/图生视频/MiniMax H3-多图参考生视频_2084171436985511938.json, 视频生成/图生视频/MiniMax H3开源版-多图参考视频工作流V1.0_2084146583087702018.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_43

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 Ref2VA开源版_2084935927293632513.json、视频生成/图生视频/MiniMax H3-多图参考生视频_2084171436985511938.json、视频生成/图生视频/MiniMax H3开源版-多图参考视频工作流V1.0_2084146583087702018.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
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
- `GetImageRangeFromBatch` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `Text` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
