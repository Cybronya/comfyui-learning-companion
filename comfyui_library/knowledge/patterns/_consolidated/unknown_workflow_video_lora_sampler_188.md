---
name: unknown_workflow_video_lora_sampler_188
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8381
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX-H3 多图参考生视频_2093727758789730305.json, 视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频-手动版_2092909194184839170.json, 视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频_2093644820110725122.json, 视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频_2093665442207457282.json, 视频生成/图生视频/MINIMAX-H3开源 文戏多图参考生视频-手动版_2090385859165122562.json, 视频生成/图生视频/MINIMAX-H3开源 文戏多图参考生视频-手动版_2095839324133744641.json, 视频生成/图生视频/Minimax H3 参考生视频 + 4步加速_2093367813456089090.json, 视频生成/图生视频/【官模】H3单图案例：自媒体文案配视频_2089348331234484226.json, 视频生成/图生视频/【官模】双模型双采样：Lightx2v+8步加速 _ 自动反推提词+单图_2088972692887269377.json, 视频生成/图生视频/双采样MinimaxH3音频驱动数字人单人版-v1.0_2085408291433304066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_188

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3 多图参考生视频_2093727758789730305.json、视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频-手动版_2092909194184839170.json、视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频_2093644820110725122.json、视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频_2093665442207457282.json、视频生成/图生视频/MINIMAX-H3开源 文戏多图参考生视频-手动版_2090385859165122562.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 9/10 个有
- `ExtendIntermediateSigmas` —— 8/10 个有
- `H3SigmaRefiner` —— 8/10 个有
- `INTConstant` —— 8/10 个有
- `LoadAudio` —— 8/10 个有
- `ImageResizeKJv2` —— 7/10 个有
- `PT_H3ConcatAVLatent` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `VAEEncode` —— 7/10 个有
- `VAEEncodeAudio` —— 7/10 个有
- `MiniMaxH3AVDecodeT8` —— 4/10 个有
- `ModelAttentionBackend` —— 4/10 个有
- `CR Prompt Text` —— 3/10 个有
- `GetNode` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `easy clearCacheAll` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `AudioCrop` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `FastGroupsBypassSwitch` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `PreviewAudio` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `SolAttnMiniMax` —— 1/10 个有
- `SoundFlow_GetLength` —— 1/10 个有
- `StringFunction|pysssss` —— 1/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/10 个有
- `easy promptConcat` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
