---
name: unknown_workflow_sampler_vae_38
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.921667
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3Ref2VAEncode, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-TVC成片_2085258608484376578.json, 视频生成/图生视频/MiniMax H3-TVC电商视频短片（自动写提示词）_2085616604645253121.json, 视频生成/图生视频/MiniMax H3-拼贴画_2085258588230086657.json, 视频生成/图生视频/MiniMax+H3+FL2VA开源版-多图参考生视频_2110975883623354370.json, 视频生成/图生视频/MiniMax-H3多图参考工作流_2091527800783196161.json, 视频生成/图生视频/MiniMaxH3_多角色视频_场景_2084637312218128386.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-多图参考生视频_2098933038003613698.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-多图参考生视频_2098990768466776065.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源版-多图参考生视频_2099666343804096513.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_38

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-TVC成片_2085258608484376578.json、视频生成/图生视频/MiniMax H3-TVC电商视频短片（自动写提示词）_2085616604645253121.json、视频生成/图生视频/MiniMax H3-拼贴画_2085258588230086657.json、视频生成/图生视频/MiniMax+H3+FL2VA开源版-多图参考生视频_2110975883623354370.json、视频生成/图生视频/MiniMax-H3多图参考工作流_2091527800783196161.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
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
- `PreviewImage` —— 6/9 个有
- `ImageConcanate` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `llama_cpp_instruct_adv` —— 3/9 个有
- `llama_cpp_model_loader` —— 3/9 个有
- `llama_cpp_parameters` —— 3/9 个有
- `EmptyImage` —— 2/9 个有
- `MuyeTextEditOutput` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
