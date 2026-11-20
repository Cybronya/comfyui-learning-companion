---
name: unknown_workflow_sampler_unet_vae_175
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.699
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/H3_海螺_官方-文生API反推_2086103276034027521.json, 视频生成/文生视频/MINIMAX-H3文生视频工作流_2099829311577616385.json, 视频生成/文生视频/MINIMAXH3-文生视频8月8日版本_2086533093908893698.json, 视频生成/文生视频/MiniMax H3 FL2VA-文生视频-优化版_2088069601203671041.json, 视频生成/文生视频/MiniMax H3 T2V comfyorg_2084874841076887553.json, 视频生成/文生视频/MiniMax H3文生视频+首尾帧生视频_2084121630451789825.json, 视频生成/文生视频/MiniMax H3文生视频+首尾帧生视频（LightX2V加速LORA）_2087364613808672770.json, 视频生成/文生视频/乡野爬山好风光_2087832652211638274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_175

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/H3_海螺_官方-文生API反推_2086103276034027521.json、视频生成/文生视频/MINIMAX-H3文生视频工作流_2099829311577616385.json、视频生成/文生视频/MINIMAXH3-文生视频8月8日版本_2086533093908893698.json、视频生成/文生视频/MiniMax H3 FL2VA-文生视频-优化版_2088069601203671041.json、视频生成/文生视频/MiniMax H3 T2V comfyorg_2084874841076887553.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 7/8 个有
- `GetNode` —— 4/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `LoadImage` —— 3/8 个有
- `CR Text` —— 1/8 个有
- `EasyCache` —— 1/8 个有
- `MiniMaxH3ReferenceToVideo` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `SolAttnPatch` —— 1/8 个有
- `SpectrumApplyMiniMaxH3` —— 1/8 个有
- `StringFunction|pysssss` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
