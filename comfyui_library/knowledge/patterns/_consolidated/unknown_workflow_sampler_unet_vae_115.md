---
name: unknown_workflow_sampler_unet_vae_115
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.770778
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/首尾帧参考生成视频_MiniMax H3 FL2VA_2084119812443299842.json, 视频生成/图生视频/高尚-MINIMAX-H3-多参_2084287046587342849.json, 视频生成/文生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V2_2087059626914308097.json, 视频生成/文生视频/37.MiniMax H3 文生视频_2085360265259995138.json, 视频生成/文生视频/39.MiniMax H3 多参考图生视频_2085360251456548866.json, 视频生成/文生视频/4步MiniMax-H3文生视频-LynnReal-Omni_2099804217237135361.json, 视频生成/文生视频/MiniMax H3 Ref2VA 剧本直出｜六段式自动生成+自动校验 · 9图参考成片 · H3原生音画同步版_2088206128625840130.json, 视频生成/文生视频/MiniMax H3多图参考生视频（速度提升2倍+提示词自动优化）_2086492553964253185.json, 视频生成/文生视频/多图参考生视频（速度提升2倍+提示词自动优化）_2086268908348207105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_115

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/首尾帧参考生成视频_MiniMax H3 FL2VA_2084119812443299842.json、视频生成/图生视频/高尚-MINIMAX-H3-多参_2084287046587342849.json、视频生成/文生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V2_2087059626914308097.json、视频生成/文生视频/37.MiniMax H3 文生视频_2085360265259995138.json、视频生成/文生视频/39.MiniMax H3 多参考图生视频_2085360251456548866.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
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
- `PrimitiveStringMultiline` —— 8/9 个有
- `LoadImage` —— 6/9 个有
- `MiniMaxH3ReferenceToVideo` —— 5/9 个有
- `MiniMaxH3BlockCacheT8` —— 4/9 个有
- `MiniMaxH3ImageToVideo` —— 4/9 个有
- `RHLLMChatNode` —— 3/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `ComfySwitchNode` —— 1/9 个有
- `Fast Groups Muter (rgthree)` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `SetNode` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
