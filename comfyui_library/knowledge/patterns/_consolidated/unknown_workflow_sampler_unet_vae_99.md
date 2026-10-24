---
name: unknown_workflow_sampler_unet_vae_99
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7558
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3-多图参考生视频_2100470995197980673.json, 视频生成/图生视频/Minimax H3 - 参考生视频_2095080820255059969.json, 视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084974167941804033.json, 视频生成/图生视频/minimax_h3_全能参考_2084642306531086337.json, 视频生成/图生视频/minimax_h3_全能参考生视频_2084112691525939201.json, 视频生成/图生视频/minimax_h3_全能参考视频_2084269876935479297.json, 视频生成/图生视频/minimax_h3_全能参考（参考视频输入）_2085193849571463169.json, 视频生成/图生视频/minimax_h3全能参考_2084451707098066946.json, 视频生成/图生视频/minimax全能参考 8步加速_2088816074463735810.json, 视频生成/图生视频/text（测试用）_2108791779993677825.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_99

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3-多图参考生视频_2100470995197980673.json、视频生成/图生视频/Minimax H3 - 参考生视频_2095080820255059969.json、视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084974167941804033.json、视频生成/图生视频/minimax_h3_全能参考_2084642306531086337.json、视频生成/图生视频/minimax_h3_全能参考生视频_2084112691525939201.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 8/10 个有
- `VHS_VideoCombine` —— 6/10 个有
- `easy showAnything` —— 6/10 个有
- `PathchSageAttentionKJ` —— 5/10 个有
- `CreateVideo` —— 4/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `SaveVideo` —— 4/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `DisableNoise` —— 1/10 个有
- `ExtendIntermediateSigmas` —— 1/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/10 个有
- `NanFengH3ReleaseBeforeDecode` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `SplitSigmasDenoise` —— 1/10 个有
- `VHS_VideoInfoLoaded` —— 1/10 个有
- `VRAM_Debug` —— 1/10 个有
- `ttN float` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
