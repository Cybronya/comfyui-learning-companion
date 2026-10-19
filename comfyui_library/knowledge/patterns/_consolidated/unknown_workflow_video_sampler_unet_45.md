---
name: unknown_workflow_video_sampler_unet_45
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.807143
common_nodes: [BasicGuider, CLIPLoader, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜VSA 4步_2098331619802308610.json, 视频生成/文生视频/双时钟采样6步极速图文生视频_2085767587174113281.json, 视频生成/文生视频/开源版Minimax H3 多合一T8版本+全节点注释_2086677614869172225.json, 视频生成/文生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086660578432610305.json, 视频生成/文生视频/文生视频-MiniMaxH3-BV2-模板_2090726527729233921.json, 视频生成/文生视频/首帧&首尾帧&关键帧&文生视频_2089598221407580161.json, 视频生成/文生视频/（本地加速版）Minimax H3 文生视频_2086449507176378369.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_45

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜VSA 4步_2098331619802308610.json、视频生成/文生视频/双时钟采样6步极速图文生视频_2085767587174113281.json、视频生成/文生视频/开源版Minimax H3 多合一T8版本+全节点注释_2086677614869172225.json、视频生成/文生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086660578432610305.json、视频生成/文生视频/文生视频-MiniMaxH3-BV2-模板_2090726527729233921.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `LoraLoaderBypassModelOnly` —— 4/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/7 个有
- `MiniMaxH3FastH34StepSetupT8Advanced` —— 1/7 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 1/7 个有
- `PainterVRAM` —— 1/7 个有
- `UniBlockSwap` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
