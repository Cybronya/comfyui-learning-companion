---
name: unknown_workflow_sampler_vae_30
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.89175
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084138964008660993.json, 视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084171989127880706.json, 视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084489209519362049.json, 视频生成/图生视频/MiniMax H3 尾帧参考生视频（适用于电商广告生成宣传视频）_2086010679311552514.json, 视频生成/图生视频/MiniMax H3 开源版 首帧图生视频_2084116833204002817.json, 视频生成/图生视频/MiniMax H3 开源版-首尾帧参考生视频_2084116862950006785.json, 视频生成/图生视频/MiniMax H3 首尾帧参考生视频_2084172928119300098.json, 视频生成/图生视频/MiniMax H3 首尾帧生视频_2084309340655276033.json, 视频生成/图生视频/MiniMax+H3+FL2VA开源版-尾帧参考生视频_2110971476173213697.json, 视频生成/图生视频/MiniMaxH3尾帧生视频_2084485586924163073.json, 视频生成/图生视频/MiniMaxH3首尾帧生视频_2084480928017108993.json, 视频生成/图生视频/MiniMaxH3首帧生视频_2084472767495364610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_30

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084138964008660993.json、视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084171989127880706.json、视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084489209519362049.json、视频生成/图生视频/MiniMax H3 尾帧参考生视频（适用于电商广告生成宣传视频）_2086010679311552514.json、视频生成/图生视频/MiniMax H3 开源版 首帧图生视频_2084116833204002817.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CreateVideo`
- `LoadImage`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3FL2VAEncode`
- `RHMiniMaxH3FL2VAModelLoader`
- `RHMiniMaxH3FL2VATarget`
- `RHMiniMaxH3FL2VATextEncoderLoader`
- `RHMiniMaxH3FL2VAVAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 10/12 个有
- `ImpactSwitch` —— 8/12 个有
- `Int` —— 8/12 个有
- `RHMiniMaxH3FL2VAFirstFrameCondition` —— 7/12 个有
- `RHMiniMaxH3FL2VALastFrameCondition` —— 5/12 个有
- `PreviewImage` —— 4/12 个有
- `CR Text` —— 3/12 个有
- `DF_Int_to_Float` —— 3/12 个有
- `MultiTextConcatenate` —— 2/12 个有
- `PrimitiveStringMultiline` —— 2/12 个有
- `RH_Translator` —— 2/12 个有
- `MuyeTextEditOutput` —— 1/12 个有
- `Text` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
