---
name: unknown_workflow_sampler_vae_41
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8246
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3Ref2VAEncode, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [图片生成/图生图/H3生成视频最终版本_2085274502887460865.json, 图片生成/图生图/MiniMax H3 FL2VA开源版-多图参考生视频_2096830763638542337.json, 图片生成/图生图/MiniMax H3 FL2VA正式版-多图参考生视频_2097242785194795009.json, 视频生成/动作迁移/MiniMax+H3+FL2VA开源版-多图参考生视频_2084476749886353409.json, 视频生成/图生视频/MiniMax H3 AI提示词润色｜双角色有声微短剧｜两图一句话_2087013189312667650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_41

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/H3生成视频最终版本_2085274502887460865.json、图片生成/图生图/MiniMax H3 FL2VA开源版-多图参考生视频_2096830763638542337.json、图片生成/图生图/MiniMax H3 FL2VA正式版-多图参考生视频_2097242785194795009.json、视频生成/动作迁移/MiniMax+H3+FL2VA开源版-多图参考生视频_2084476749886353409.json、视频生成/图生视频/MiniMax H3 AI提示词润色｜双角色有声微短剧｜两图一句话_2087013189312667650.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

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
- `PrimitiveStringMultiline` —— 2/5 个有
- `CLIPLoader` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有
- `TextGenerate` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
