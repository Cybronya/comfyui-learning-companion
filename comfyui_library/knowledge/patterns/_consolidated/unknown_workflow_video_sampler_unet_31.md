---
name: unknown_workflow_video_sampler_unet_31
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.784538
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/FastH3 VSA文生视频优化版V1_2096244135350067201.json, 视频生成/文生视频/H3文生视频-融合模型10Eros-加速lora+双时钟_2087828994078105602.json, 视频生成/文生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-文生视频_2093348888148267009.json, 视频生成/文生视频/MINIMAX-H3文生视频T8加速版_2097572430410772482.json, 视频生成/文生视频/MINIMAX-H3文生视频_2093582444862730242.json, 视频生成/文生视频/MiniMax H3-文生视频V1-双时钟-8步高质量极速-step600_2086838165842780162.json, 视频生成/文生视频/MiniMax H3多参生视频1(双时钟-8步高质量极速)_2085802445816553474.json, 视频生成/文生视频/MiniMax H3音频驱动数字人-参考生视频-长视频直出【加速版】_2100939860373762049.json, 视频生成/文生视频/MiniMax H3音频驱动数字人-多人对话-加速版-支持长视频直出-单采_2100933650757017601.json, 视频生成/文生视频/MiniMax+H3！加速版！提速480%！全能参考！_2085641752681213953.json, 视频生成/文生视频/极速版 MinimaxH3 文生视频 图生视频  T8版_2085912109149417474.json, 视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）.json, 视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_31

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/FastH3 VSA文生视频优化版V1_2096244135350067201.json、视频生成/文生视频/H3文生视频-融合模型10Eros-加速lora+双时钟_2087828994078105602.json、视频生成/文生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-文生视频_2093348888148267009.json、视频生成/文生视频/MINIMAX-H3文生视频T8加速版_2097572430410772482.json、视频生成/文生视频/MINIMAX-H3文生视频_2093582444862730242.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 12/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/13 个有
- `CR Prompt Text` —— 10/13 个有
- `MiniMaxH3DualClockSamplerT8` —— 9/13 个有
- `LoadImage` —— 7/13 个有
- `ModelAttentionBackend` —— 6/13 个有
- `孤海注释` —— 6/13 个有
- `LoadAudio` —— 4/13 个有
- `SolAttnMiniMax` —— 4/13 个有
- `LoraLoaderModelOnly` —— 3/13 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/13 个有
- `PrimitiveStringMultiline` —— 3/13 个有
- `VHS_LoadVideo` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `Label (rgthree)` —— 1/13 个有
- `MiniMaxH3FastH34StepSetupT8Advanced` —— 1/13 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
