---
name: unknown_workflow_sampler_vae_66
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CreateVideo, ImageResize+, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/高清版MiniMax H3 FL2VA-图生视频_2086620893954002945.json, 视频生成/图生视频/（开源版）H3图生视频（图生视频&首尾帧）_2084181753610194946.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_66

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/高清版MiniMax H3 FL2VA-图生视频_2086620893954002945.json、视频生成/图生视频/（开源版）H3图生视频（图生视频&首尾帧）_2084181753610194946.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateVideo`
- `ImageResize+`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `FlashVSR_SM_KSampler` —— 1/2 个有
- `FlashVSR_SM_Model` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `ImageCASharpening+` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `Primitive float [Crystools]` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.70953e+08 | - | 1 | 100% |
| Prompt 约束强度(CFG) | randomize | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 4.70953e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
