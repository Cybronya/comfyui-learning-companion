---
name: unknown_workflow_sampler_vae_14
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.855364
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-图生视频_2084472539518164994.json, 视频生成/图生视频/MiniMax H3-现实世界手绘特效_2085245279707688962.json, 视频生成/图生视频/MiniMax H3-现实世界手绘特效_2086663800769572866.json, 视频生成/图生视频/MiniMax H3图生视频RH开源版_2084145059666161665.json, 视频生成/图生视频/MiniMax H3图生视频RH开源版_2084148143737892866.json, 视频生成/图生视频/MiniMax H3图生视频RH开源版_2084151877721214978.json, 视频生成/图生视频/MiniMax H3图生视频RH开源版_2084153810871742465.json, 视频生成/图生视频/MiniMax H3图生视频RH开源版_2084155669799849985.json, 视频生成/图生视频/MiniMax H3图生视频RH开源版_2084157528535035906.json, 视频生成/图生视频/MiniMax H3图生视频RH开源版_2084159561623236609.json, 视频生成/图生视频/MiniMax H3图生视频开源RH版_2084115633087795201.json, 视频生成/图生视频/MiniMax H3尾帧图生视频RH开源版_2084144093843771394.json, 视频生成/图生视频/MiniMax H3尾帧图生视频RH开源版_2084147517679296514.json, 视频生成/图生视频/MiniMax H3尾帧图生视频RH开源版_2084150934657130498.json, 视频生成/图生视频/MiniMax H3尾帧图生视频RH开源版_2084153321937530881.json, 视频生成/图生视频/MiniMax H3尾帧图生视频RH开源版_2084155105561108482.json, 视频生成/图生视频/MiniMax H3尾帧图生视频RH开源版_2084156990619734018.json, 视频生成/图生视频/MiniMax H3尾帧图生视频RH开源版_2084159033002516481.json, 视频生成/图生视频/MiniMax H3开源版尾帧参考生视频_2084111157392134145.json, 视频生成/图生视频/MiniMax H3开源版首尾帧参考生视频_2084111270114062338.json, 视频生成/图生视频/MiniMax H3开源版首帧参考生视频_2084111309850898434.json, 视频生成/图生视频/首尾帧视频-MiniMax H3开源版_2084194304708407298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_14

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-图生视频_2084472539518164994.json、视频生成/图生视频/MiniMax H3-现实世界手绘特效_2085245279707688962.json、视频生成/图生视频/MiniMax H3-现实世界手绘特效_2086663800769572866.json、视频生成/图生视频/MiniMax H3图生视频RH开源版_2084145059666161665.json、视频生成/图生视频/MiniMax H3图生视频RH开源版_2084148143737892866.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 22 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 19/22 个有
- `CR Text` —— 16/22 个有
- `PrimitiveInt` —— 16/22 个有
- `RHMiniMaxH3FL2VAFirstFrameCondition` —— 14/22 个有
- `RHMiniMaxH3FL2VALastFrameCondition` —— 8/22 个有
- `easy showAnything` —— 2/22 个有
- `llama_cpp_instruct_adv` —— 2/22 个有
- `llama_cpp_model_loader` —— 2/22 个有
- `llama_cpp_parameters` —— 2/22 个有
- `PreviewImage` —— 1/22 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
