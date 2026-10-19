---
name: unknown_workflow_sampler_vae_16
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.889375
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/首尾帧生视频 -开源海螺minimax-H3_2084249905740210177.json, 视频生成/图生视频/首尾帧视频-MiniMax H3开源版_2084194304708407298.json, 视频生成/图生视频/（开源版）H3图生视频（图生视频&首尾帧）_2084181753610194946.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-图生视频+全节点注释_2084168465803464705.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-图生视频_2092263577653694466.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-图生视频_2092965212705083394.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-图生视频_2105674788806160385.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-首尾帧参考生视频+全节点注释_2084158451135111169.json, 视频生成/文生视频/MiniMax H3 低显存15秒音画工作流_2085021778228891650.json, 视频生成/文生视频/MiniMax H3 图生视频 开源版_2084243906950164482.json, 视频生成/文生视频/MiniMax H3 图生视频 开源版_2088063956425465858.json, 视频生成/文生视频/MiniMax H3 图生视频 开源版_2097846209267462146.json, 视频生成/文生视频/MiniMax H3 图生视频 首帧生视频 开源版_2084887895084720130.json, 视频生成/文生视频/MiniMax H3首尾帧视频RH开源版_2084229817393836033.json, 视频生成/文生视频/MiniMax H3首尾帧视频RH开源版_2084890657570770945.json, 视频生成/文生视频/MiniMaxH3RH开源版ENG首尾帧视频ENGENG_2087106846300663809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_16

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/首尾帧生视频 -开源海螺minimax-H3_2084249905740210177.json、视频生成/图生视频/首尾帧视频-MiniMax H3开源版_2084194304708407298.json、视频生成/图生视频/（开源版）H3图生视频（图生视频&首尾帧）_2084181753610194946.json、视频生成/文生视频/MiniMax H3 FL2VA开源版-图生视频+全节点注释_2084168465803464705.json、视频生成/文生视频/MiniMax H3 FL2VA开源版-图生视频_2092263577653694466.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
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
- `CR Text` —— 9/16 个有
- `Int` —— 9/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/16 个有
- `PrimitiveInt` —— 8/16 个有
- `intToFloat _O` —— 7/16 个有
- `ImageResize+` —— 6/16 个有
- `PrimitiveFloat` —— 1/16 个有
- `easy int` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
