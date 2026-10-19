---
name: unknown_workflow_sampler_unet_vae_107
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/【遇见AI】Minimax H3，多参考生图，9视频9图3音频_2084533778860568577.json, 视频生成/文生视频/【遇见AI】Minimax H3，文生图基础流_2084511826766811137.json, 视频生成/文生视频/【遇见AI】minimax H3 高动态打斗场景武术动作二采修复+提示词skill工作流_2095684866888257537.json, 视频生成/文生视频/万象AI--MiniMax H3 多参生视频--基础工作流_2084961117960491010.json, 视频生成/文生视频/剑斗多参模式_2094373732667187201.json, 视频生成/文生视频/战斗双采首尾帧模式_2094373774731862018.json, 视频生成/文生视频/视频生成（文生_图生_参考生）Minimax-H3_2087564591730618370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_107

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/【遇见AI】Minimax H3，多参考生图，9视频9图3音频_2084533778860568577.json、视频生成/文生视频/【遇见AI】Minimax H3，文生图基础流_2084511826766811137.json、视频生成/文生视频/【遇见AI】minimax H3 高动态打斗场景武术动作二采修复+提示词skill工作流_2095684866888257537.json、视频生成/文生视频/万象AI--MiniMax H3 多参生视频--基础工作流_2084961117960491010.json、视频生成/文生视频/剑斗多参模式_2094373732667187201.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/7 个有
- `MiniMaxH3ReferenceToVideo` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `SaveVideo` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `MiniMaxH3ImageToVideo` —— 4/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `DisableNoise` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `ExtendIntermediateSigmas` —— 2/7 个有
- `SplitSigmasDenoise` —— 2/7 个有
- `VHS_VideoCombine` —— 2/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `ReservedVRAMSetter` —— 1/7 个有
- `SplitSigmas` —— 1/7 个有
- `UniBlockSwap` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
