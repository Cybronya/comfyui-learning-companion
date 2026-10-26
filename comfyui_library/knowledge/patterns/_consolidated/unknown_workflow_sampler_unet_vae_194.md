---
name: unknown_workflow_sampler_unet_vae_194
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8385
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/首尾帧-MiniMaxH3-图生视频-模板_2090038373938458625.json, 视频生成/文生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V2_2087059626914308097.json, 视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V3_2086292004803276802.json, 视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V4_2084169977384497154.json, 视频生成/文生视频/260818001.MiniMax-H3 文生丨首尾帧生视频_2089370217431523330.json, 视频生成/文生视频/MiniMax H3 Larry + Sageattention加速_2086411824722956290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_194

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/首尾帧-MiniMaxH3-图生视频-模板_2090038373938458625.json、视频生成/文生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V2_2087059626914308097.json、视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V3_2086292004803276802.json、视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V4_2084169977384497154.json、视频生成/文生视频/260818001.MiniMax-H3 文生丨首尾帧生视频_2089370217431523330.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `MiniMaxH3BlockCacheT8` —— 3/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `PatchFlashAttentionKJ` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `SolAttnPatch` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
