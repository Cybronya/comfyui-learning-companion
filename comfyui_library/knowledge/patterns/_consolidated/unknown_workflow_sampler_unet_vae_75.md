---
name: unknown_workflow_sampler_unet_vae_75
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.900444
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 极速单图或首尾帧视频工作流_2085305466082643970.json, 视频生成/图生视频/Minimax H3 首尾帧_2089249903888392193.json, 视频生成/图生视频/Minimax H3-i2v 加速版图生视频-文生视频_2091734941167087618.json, 视频生成/图生视频/Minimax H3-图生视频（高动态去噪点）_2089348010357641217.json, 视频生成/图生视频/Minimax H3-多参视频生成（高动态去噪点）_2089353256249151489.json, 视频生成/图生视频/▶▷MiniMaxH3-图生视频_2093020292909195265.json, 视频生成/图生视频/首尾帧-MiniMaxH3-图生视频-模板_2090038373938458625.json, 视频生成/文生视频/Minimax H3-文生视频（高动态去噪点）_2089345292486402050.json, 视频生成/文生视频/【终极版本】MiniMax H3 双采高清工作流 提速不降质【AI小王子】_2095420966586376194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_75

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 极速单图或首尾帧视频工作流_2085305466082643970.json、视频生成/图生视频/Minimax H3 首尾帧_2089249903888392193.json、视频生成/图生视频/Minimax H3-i2v 加速版图生视频-文生视频_2091734941167087618.json、视频生成/图生视频/Minimax H3-图生视频（高动态去噪点）_2089348010357641217.json、视频生成/图生视频/Minimax H3-多参视频生成（高动态去噪点）_2089353256249151489.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `CreateVideo` —— 7/9 个有
- `MiniMaxH3ImageToVideo` —— 7/9 个有
- `ResolutionSelector` —— 7/9 个有
- `SaveVideo` —— 7/9 个有
- `ExtendIntermediateSigmas` —— 4/9 个有
- `H3SigmaRefiner` —— 4/9 个有
- `ModelAttentionBackend` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `Label (rgthree)` —— 3/9 个有
- `INTConstant` —— 2/9 个有
- `MiniMaxH3ReferenceToVideo` —— 2/9 个有
- `MiniMaxH3SigmaShift` —— 2/9 个有
- `Seed (rgthree)` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `VHS_VideoCombine` —— 2/9 个有
- `CacheDiT_Model_Optimizer` —— 1/9 个有
- `LTXVConcatAVLatent` —— 1/9 个有
- `LTXVSeparateAVLatent` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `MinimaxH3LatentUpscaler3D` —— 1/9 个有
- `SolAttnPatch` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
