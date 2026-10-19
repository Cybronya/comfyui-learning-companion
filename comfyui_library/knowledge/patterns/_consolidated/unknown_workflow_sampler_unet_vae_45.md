---
name: unknown_workflow_sampler_unet_vae_45
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.73525
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json, 视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json, 视频生成/图生视频/A-4 MiniMax H3 图生视频 _ 首尾帧控制 _ 原生音频 _ 两张图变一段电影_2084559447325757441.json, 视频生成/图生视频/CG迷-MiniMax H3参考生视频工作流_2085601489535455234.json, 视频生成/图生视频/H3 Ref2VA 多图综合参考 - 87time_2084503529204576258.json, 视频生成/图生视频/H3 关键帧视频动画_2106371268684636162.json, 视频生成/图生视频/H3-参考生视频（全能参考）_2087759964113821697.json, 视频生成/图生视频/H3-官方长视频续接_2095155400160141314.json, 视频生成/文生视频/H3-官方长视频_2092501348708343810.json, 视频生成/文生视频/影视级minimax h3，无限长视频接续-手动版_2096601875046027266.json, 视频生成/文生视频/长视频续接+去油+高质量minimax-H3-官方版-无限延长视频-手动版_2092974453855703041.json, 视频生成/文生视频/🔪🔪H3突破15秒！长视频不劣化！工作流拆解系列06集_2093951850499366914.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_45

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json、视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json、视频生成/图生视频/A-4 MiniMax H3 图生视频 _ 首尾帧控制 _ 原生音频 _ 两张图变一段电影_2084559447325757441.json、视频生成/图生视频/CG迷-MiniMax H3参考生视频工作流_2085601489535455234.json、视频生成/图生视频/H3 Ref2VA 多图综合参考 - 87time_2084503529204576258.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
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
- `VAEDecode` —— 11/12 个有
- `MiniMaxH3ReferenceToVideo` —— 10/12 个有
- `PrimitiveStringMultiline` —— 10/12 个有
- `VAEDecodeAudio` —— 10/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/12 个有
- `VHS_LoadVideo` —— 6/12 个有
- `ComfySwitchNode` —— 5/12 个有
- `ExtendIntermediateSigmas` —— 5/12 个有
- `GetImageRangeFromBatch` —— 5/12 个有
- `LoadAudio` —— 5/12 个有
- `MiniMaxH3AddGuide` —— 5/12 个有
- `ModelPreviewOverrideKJ` —— 5/12 个有
- `PrimitiveBoolean` —— 5/12 个有
- `easy showAnything` —— 5/12 个有
- `ImageAddNoise` —— 4/12 个有
- `孤海注释` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `GetNode` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `MiniMaxH3ImageToVideo` —— 2/12 个有
- `MiniMaxH3SigmaShift` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `Text` —— 2/12 个有
- `TrimAudioDuration` —— 2/12 个有
- `忽略多组孤海` —— 2/12 个有
- `H3SigmaRefiner` —— 1/12 个有
- `MiniMaxH3AVDecodeT8` —— 1/12 个有
- `ModelAttentionBackend` —— 1/12 个有
- `PathchSageAttentionKJ` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `SolAttnMiniMax` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
