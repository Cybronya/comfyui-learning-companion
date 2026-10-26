---
name: unknown_workflow_sampler_vae_33
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.927091
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 首尾帧&自动提示词_2084468473316597761.json, 视频生成/图生视频/MinimaxH3首尾帧&自动提示词ENGENG_2087091217380237314.json, 视频生成/图生视频/首尾帧生视频 -开源海螺minimax-H3_2084249905740210177.json, 视频生成/图生视频/首尾帧视频-MiniMax H3开源版_2084194304708407298.json, 视频生成/文生视频/MiniMax H3 图生视频 开源版_2084243906950164482.json, 视频生成/文生视频/MiniMax H3 图生视频 开源版_2088063956425465858.json, 视频生成/文生视频/MiniMax H3 图生视频 开源版_2097846209267462146.json, 视频生成/文生视频/MiniMax H3 图生视频 首帧生视频 开源版_2084887895084720130.json, 视频生成/文生视频/MiniMax H3首尾帧视频RH开源版_2084229817393836033.json, 视频生成/文生视频/MiniMax H3首尾帧视频RH开源版_2084890657570770945.json, 视频生成/文生视频/MiniMaxH3RH开源版ENG首尾帧视频ENGENG_2087106846300663809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_33

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 首尾帧&自动提示词_2084468473316597761.json、视频生成/图生视频/MinimaxH3首尾帧&自动提示词ENGENG_2087091217380237314.json、视频生成/图生视频/首尾帧生视频 -开源海螺minimax-H3_2084249905740210177.json、视频生成/图生视频/首尾帧视频-MiniMax H3开源版_2084194304708407298.json、视频生成/文生视频/MiniMax H3 图生视频 开源版_2084243906950164482.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `CreateVideo`
- `LoadImage`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3FL2VAEncode`
- `RHMiniMaxH3FL2VAFirstFrameCondition`
- `RHMiniMaxH3FL2VAModelLoader`
- `RHMiniMaxH3FL2VATarget`
- `RHMiniMaxH3FL2VATextEncoderLoader`
- `RHMiniMaxH3FL2VAVAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `Int` —— 9/11 个有
- `intToFloat _O` —— 9/11 个有
- `PrimitiveInt` —— 8/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `RH_LLMAPI_Pro_Node` —— 2/11 个有
- `ShowAnything|Mie` —— 2/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
