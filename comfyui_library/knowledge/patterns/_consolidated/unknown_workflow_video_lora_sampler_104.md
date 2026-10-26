---
name: unknown_workflow_video_lora_sampler_104
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.871875
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3多参卡点换装工作流_2097696437873242114.json, 视频生成/图生视频/MiniMax-图生视频-双时钟加速_2086024045186871298.json, 视频生成/图生视频/MiniMaxH3-V1-step600ENG8步高质量极速双时钟ENG参考生视频ENGENG_2087090322936516610.json, 视频生成/图生视频/Minimax H3 10Eros 8步 图生视频_2087104877880233985.json, 视频生成/图生视频/Minimax H3 双时钟参考图生视频（4步极速）_2111092460335226882.json, 视频生成/图生视频/Minimax H3 图生视频 V1_2086828683976855553.json, 视频生成/图生视频/Minimax H3(双时钟-8步极速高质量)参考生视频-fl2va_2085750687979360258.json, 视频生成/图生视频/Minimax H3(双时钟-8步高质量极速)参考生视频-fl2va_2085718965225091073.json, 视频生成/图生视频/Minimax图生视频_2088591493631135746.json, 视频生成/图生视频/Minimax图生视频（Lightx2v正式版8步lora+双时钟）_2087718729126862850.json, 视频生成/图生视频/Minimax海螺h3开源版 8步高质量极速图生视频加速优化版_2085679906003968001.json, 视频生成/图生视频/QHDMinimax-H3加速版_2086351325427748866.json, 视频生成/图生视频/minimax三图工作流_2092594675935956993.json, 视频生成/图生视频/minimax参考生视频-4张图官方案例（light2v8步lora正式版+双时钟）_2087937856227602434.json, 视频生成/图生视频/minimax图生视频（light2v8步lora正式版+双时钟）_2087533230470811649.json, 视频生成/图生视频/海螺Minimax_H3_图生视频_2084150796144435202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_104

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3多参卡点换装工作流_2097696437873242114.json、视频生成/图生视频/MiniMax-图生视频-双时钟加速_2086024045186871298.json、视频生成/图生视频/MiniMaxH3-V1-step600ENG8步高质量极速双时钟ENG参考生视频ENGENG_2087090322936516610.json、视频生成/图生视频/Minimax H3 10Eros 8步 图生视频_2087104877880233985.json、视频生成/图生视频/Minimax H3 双时钟参考图生视频（4步极速）_2111092460335226882.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AVDecodeT8` —— 15/16 个有
- `MiniMaxH3AudioConditioningT8` —— 15/16 个有
- `CR Prompt Text` —— 14/16 个有
- `ModelAttentionBackend` —— 6/16 个有
- `孤海注释` —— 3/16 个有
- `WujiCleaner` —— 2/16 个有
- `easy cleanGpuUsed` —— 2/16 个有
- `CM_FloatToInt` —— 1/16 个有
- `MiniMaxH3BlockCacheT8` —— 1/16 个有
- `MiniMaxH3ReferenceToVideo` —— 1/16 个有
- `Text` —— 1/16 个有
- `VAEDecode` —— 1/16 个有
- `VAEDecodeAudio` —— 1/16 个有
- `VHS_LoadVideo` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
