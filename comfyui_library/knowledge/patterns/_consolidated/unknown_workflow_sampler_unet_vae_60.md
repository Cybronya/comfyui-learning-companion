---
name: unknown_workflow_sampler_unet_vae_60
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7041
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json, 视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json, 视频生成/图生视频/A-4 MiniMax H3 图生视频 _ 首尾帧控制 _ 原生音频 _ 两张图变一段电影_2084559447325757441.json, 视频生成/图生视频/BUNNY_H3_单采_er_sde_手动Sigma_2109936169202049026.json, 视频生成/图生视频/H3-官方长视频续接_2095155400160141314.json, 视频生成/图生视频/（2320）H3-最优官流_2089001915131711490.json, 视频生成/文生视频/H3-官方长视频_2092501348708343810.json, 视频生成/文生视频/影视级minimax h3，无限长视频接续-手动版_2096601875046027266.json, 视频生成/文生视频/长视频续接+去油+高质量minimax-H3-官方版-无限延长视频-手动版_2092974453855703041.json, 视频生成/文生视频/🔪🔪H3突破15秒！长视频不劣化！工作流拆解系列06集_2093951850499366914.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_60

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json、视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json、视频生成/图生视频/A-4 MiniMax H3 图生视频 _ 首尾帧控制 _ 原生音频 _ 两张图变一段电影_2084559447325757441.json、视频生成/图生视频/BUNNY_H3_单采_er_sde_手动Sigma_2109936169202049026.json、视频生成/图生视频/H3-官方长视频续接_2095155400160141314.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 9/10 个有
- `VAEDecode` —— 9/10 个有
- `VAEDecodeAudio` —— 9/10 个有
- `BasicScheduler` —— 8/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `LoadAudio` —— 7/10 个有
- `ModelPreviewOverrideKJ` —— 7/10 个有
- `ComfySwitchNode` —— 6/10 个有
- `PrimitiveBoolean` —— 6/10 个有
- `VHS_LoadVideo` —— 6/10 个有
- `ExtendIntermediateSigmas` —— 5/10 个有
- `GetImageRangeFromBatch` —— 5/10 个有
- `MiniMaxH3AddGuide` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `ImageAddNoise` —— 4/10 个有
- `孤海注释` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `GetNode` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `ManualSigmas` —— 2/10 个有
- `MiniMaxH3ImageToVideo` —— 2/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `TrimAudioDuration` —— 2/10 个有
- `忽略多组孤海` —— 2/10 个有
- `CLIPTextEncode` —— 1/10 个有
- `H3SigmaRefiner` —— 1/10 个有
- `MiniMaxH3AVDecodeT8` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `SolAttnMiniMax` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
