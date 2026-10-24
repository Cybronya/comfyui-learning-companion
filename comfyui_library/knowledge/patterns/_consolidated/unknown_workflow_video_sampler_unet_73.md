---
name: unknown_workflow_video_sampler_unet_73
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.844667
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MultiRateSamplerEXPT8, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/文生视频-MiniMaxH3-BV2-模板_2090726527729233921.json, 视频生成/文生视频/首帧&首尾帧&关键帧&文生视频_2089598221407580161.json, 视频生成/文生视频/（本地加速版）Minimax H3 文生视频_2086449507176378369.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_73

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/文生视频-MiniMaxH3-BV2-模板_2090726527729233921.json、视频生成/文生视频/首帧&首尾帧&关键帧&文生视频_2089598221407580161.json、视频生成/文生视频/（本地加速版）Minimax H3 文生视频_2086449507176378369.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `INTConstant` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PainterVRAM` —— 1/3 个有
- `UniBlockSwap` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
