---
name: unknown_workflow_video_lora_sampler_616
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.551
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax 单采打戏_2095742874632675330.json, 视频生成/图生视频/Minimax-H3多参-人物自然_2092153269014589441.json, 视频生成/图生视频/MinimaxH3 长视频生成~_2095477683223355393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_616

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Minimax 单采打戏_2095742874632675330.json、视频生成/图生视频/Minimax-H3多参-人物自然_2092153269014589441.json、视频生成/图生视频/MinimaxH3 长视频生成~_2095477683223355393.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 2/3 个有
- `LayerColor: Brightness & Contrast` —— 2/3 个有
- `MiniMaxH3SigmaShift` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `SolAttnPatch` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `FrameInterpolate` —— 1/3 个有
- `FrameInterpolationModelLoader` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `MiniMaxH3AddGuide` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
