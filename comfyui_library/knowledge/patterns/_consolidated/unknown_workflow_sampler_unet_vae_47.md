---
name: unknown_workflow_sampler_unet_vae_47
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.842353
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/调用版minimax+H3+开源版 -首尾帧_2091060784687308801.json, 视频生成/图生视频/调用版minimax+H3+开源版+文生视频+T2VA文生_2086814099383607297.json, 视频生成/图生视频/高尚-MINIMAX-H3-多参_2084287046587342849.json, 视频生成/文生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V2_2087059626914308097.json, 视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V3_2086292004803276802.json, 视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V4_2084169977384497154.json, 视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084908134719643649.json, 视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084998635074445314.json, 视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2085402316232019969.json, 视频生成/文生视频/FS-video_minimax_h3_r2v_2105628001928044546.json, 视频生成/文生视频/FastH3 文生视频_2100134500020867073.json, 视频生成/文生视频/FastVideo FastH3：文生视频_2100285646945472514.json, 视频生成/文生视频/FastVideo-FastH3-8-Step-V2 文生视频_2100836004453249025.json, 视频生成/文生视频/MiniMax FastH3 v2首尾帧视频_2100074906296872962.json, 视频生成/文生视频/MiniMax H3 Ref2VA 剧本直出｜六段式自动生成+自动校验 · 9图参考成片 · H3原生音画同步版_2088206128625840130.json, 视频生成/文生视频/MiniMax H3多图参考生视频（速度提升2倍+提示词自动优化）_2086492553964253185.json, 视频生成/文生视频/多图参考生视频（速度提升2倍+提示词自动优化）_2086268908348207105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_47

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/调用版minimax+H3+开源版 -首尾帧_2091060784687308801.json、视频生成/图生视频/调用版minimax+H3+开源版+文生视频+T2VA文生_2086814099383607297.json、视频生成/图生视频/高尚-MINIMAX-H3-多参_2084287046587342849.json、视频生成/文生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V2_2087059626914308097.json、视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V3_2086292004803276802.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 17 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo` —— 12/17 个有
- `MiniMaxH3BlockCacheT8` —— 9/17 个有
- `PrimitiveStringMultiline` —— 9/17 个有
- `ModelAttentionBackend` —— 8/17 个有
- `LoadImage` —— 7/17 个有
- `BlockSparseAttention` —— 5/17 个有
- `CR Prompt Text` —— 5/17 个有
- `MiniMaxH3ReferenceToVideo` —— 5/17 个有
- `MiniMaxH3SigmaShift` —— 5/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/17 个有
- `PathchSageAttentionKJ` —— 3/17 个有
- `RHLLMChatNode` —— 3/17 个有
- `H3SigmaRefiner` —— 2/17 个有
- `LoraLoaderBypassModelOnly` —— 2/17 个有
- `ShowText|pysssss` —— 2/17 个有
- `Text Multiline` —— 2/17 个有
- `easy cleanGpuUsed` —— 2/17 个有
- `easy showAnything` —— 2/17 个有
- `Label (rgthree)` —— 1/17 个有
- `SaveImage` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
