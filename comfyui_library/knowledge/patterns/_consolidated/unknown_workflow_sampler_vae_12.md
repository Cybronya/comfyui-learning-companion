---
name: unknown_workflow_sampler_vae_12
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.843957
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084138964008660993.json, 视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084171989127880706.json, 视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084489209519362049.json, 视频生成/图生视频/MiniMax H3 尾帧参考生视频（适用于电商广告生成宣传视频）_2086010679311552514.json, 视频生成/图生视频/MiniMax H3 开源版 首帧图生视频_2084116833204002817.json, 视频生成/图生视频/MiniMax H3 开源版-首尾帧参考生视频_2084116862950006785.json, 视频生成/图生视频/MiniMax H3 首帧参考生视频_2084126354357968897.json, 视频生成/图生视频/MiniMax H3-图生视频_2084472539518164994.json, 视频生成/图生视频/MiniMax H3-首尾帧参考生视频（中文提示词）_2084256715142426625.json, 视频生成/图生视频/MiniMax+H3+FL2VA开源版-尾帧参考生视频_2110971476173213697.json, 视频生成/图生视频/MiniMax+H3+FL2VA开源版-首尾帧参考生视频_2110973759195799553.json, 视频生成/图生视频/MiniMax+H3+FL2VA开源版-首帧参考生视频_2110966496859082754.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-尾帧参考生视频_2098933933139382274.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-尾帧参考生视频_2098991696456544257.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-尾帧参考生视频_2099667209504251906.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首尾帧参考生视频_2098935729991802881.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首尾帧参考生视频_2098993555862810625.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首尾帧参考生视频_2099668959648894977.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首帧参考生视频_2098936811023327233.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首帧参考生视频_2098994491230347266.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-首帧参考生视频_2099669900225761282.json, 视频生成/图生视频/图生视频尾帧MiniMax+H3+FL2VA开源版-尾帧参考生视频_2084131204399452161.json, 视频生成/文生视频/MiniMax+H3+FL2VA开源版-尾帧参考生视频_2084183815051894786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_12

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084138964008660993.json、视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084171989127880706.json、视频生成/图生视频/MiniMax H3 尾帧参考生视频_2084489209519362049.json、视频生成/图生视频/MiniMax H3 尾帧参考生视频（适用于电商广告生成宣传视频）_2086010679311552514.json、视频生成/图生视频/MiniMax H3 开源版 首帧图生视频_2084116833204002817.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 23 个 workflow 都包含：
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
- `ImageResize+` —— 20/23 个有
- `ImpactSwitch` —— 19/23 个有
- `Int` —— 19/23 个有
- `PreviewImage` —— 18/23 个有
- `RHMiniMaxH3FL2VAFirstFrameCondition` —— 14/23 个有
- `EmptyImage` —— 9/23 个有
- `RHMiniMaxH3FL2VALastFrameCondition` —— 9/23 个有
- `MuyeTextEditOutput` —— 3/23 个有
- `MultiTextConcatenate` —— 2/23 个有
- `PrimitiveStringMultiline` —— 2/23 个有
- `RH_Translator` —— 2/23 个有
- `RH_OneShot_Prompter` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
