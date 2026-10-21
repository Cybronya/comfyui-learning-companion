---
name: unknown_workflow_sampler_unet_vae_153
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8242
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 长视频  音频驱动（数字人）唱歌30s_1分钟 切换_2099343389337673730.json, 视频生成/图生视频/MiniMax H3 音频驱动（数字人）唱歌视频_2084544809620041730.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2104901215766278145.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2106317299799121921.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2110247938256625666.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_153

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 长视频  音频驱动（数字人）唱歌30s_1分钟 切换_2099343389337673730.json、视频生成/图生视频/MiniMax H3 音频驱动（数字人）唱歌视频_2084544809620041730.json、视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2104901215766278145.json、视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2106317299799121921.json、视频生成/图生视频/minimax_h3_turbo_v4_step600_ema_2110247938256625666.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `ExtendIntermediateSigmas` —— 3/5 个有
- `TrimAudioDuration` —— 2/5 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/5 个有
- `AudioConcat` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImageBatch` —— 1/5 个有
- `MiniMaxH3AddGuide` —— 1/5 个有
- `MiniMaxH3TurboLoRA` —— 1/5 个有
- `SelectImages` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `SolAttnPatch` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
