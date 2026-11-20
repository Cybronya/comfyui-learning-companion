---
name: unknown_workflow_sampler_vae_15
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8518
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3-尾帧参考生视频_2085267201841524738.json, 视频生成/图生视频/MiniMax-H3-首尾帧参考生视频_2084575836715438081.json, 视频生成/图生视频/MiniMax-H3-首帧参考生视频_2085267055179296770.json, 视频生成/图生视频/MiniMax-H3_图生视频_RH版_首帧驱动_2100205825334796289.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-图生视频_2100870356302131202.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-图生视频_2100933710886563842.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-图生视频_2101137262460358657.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-图生视频_2102307069243248641.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-尾帧参考生视频_2098933933139382274.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-尾帧参考生视频_2098991696456544257.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-尾帧参考生视频_2099667209504251906.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首尾帧参考生视频_2098935729991802881.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首尾帧参考生视频_2098993555862810625.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首尾帧参考生视频_2099668959648894977.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首帧参考生视频_2098936811023327233.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首帧参考生视频_2098994491230347266.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首帧参考生视频_2099669900225761282.json, 视频生成/文生视频/MiniMax+H3+FL2VA开源版-尾帧参考生视频_2084183815051894786.json, 视频生成/文生视频/MiniMax+H3+FL2VA开源版-首尾帧参考生视频_2084175487978524673.json, 视频生成/文生视频/MiniMax+H3+FL2VA开源版-首帧参考生视频_2084171293531922434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3-尾帧参考生视频_2085267201841524738.json、视频生成/图生视频/MiniMax-H3-首尾帧参考生视频_2084575836715438081.json、视频生成/图生视频/MiniMax-H3-首帧参考生视频_2085267055179296770.json、视频生成/图生视频/MiniMax-H3_图生视频_RH版_首帧驱动_2100205825334796289.json、视频生成/图生视频/MiniMax_H3_FL2VA开源版-图生视频_2100870356302131202.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 20 个 workflow 都包含：
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
- `ImageResize+` —— 16/20 个有
- `PreviewImage` —— 15/20 个有
- `RHMiniMaxH3FL2VAFirstFrameCondition` —— 15/20 个有
- `EmptyImage` —— 12/20 个有
- `ImpactSwitch` —— 12/20 个有
- `Int` —— 12/20 个有
- `RHMiniMaxH3FL2VALastFrameCondition` —— 5/20 个有
- `CR Prompt Text` —— 3/20 个有
- `ImageScale` —— 3/20 个有
- `ResolutionSelector` —— 3/20 个有
- `JjkText` —— 2/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
