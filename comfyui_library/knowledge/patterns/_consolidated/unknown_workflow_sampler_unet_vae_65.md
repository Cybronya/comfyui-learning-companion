---
name: unknown_workflow_sampler_unet_vae_65
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8304
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/minimax文字出视频_2084271438885904386.json, 视频生成/文生视频/video_minimax_h3_r2v 多素材联合参考_2085213870431490049.json, 视频生成/文生视频/video_minimax_h3_r2v多参=加速_2095122591458615297.json, 视频生成/文生视频/video_minimax_h3_r2v多参考生视频_2084510984789647362.json, 视频生成/文生视频/video_minimax_h3_t2v_2084126777605181442.json, 视频生成/文生视频/【Gensor-AI】MINIMAX-H3工作流合集【加速版】_2085550246054162433.json, 视频生成/文生视频/【V-zion】Minimax-H3【文生视频_首尾帧_首帧_尾帧】附加提示词模板_2084613485291462658.json, 视频生成/文生视频/开源版MINIMAX-H3 文生视频 图生视频 多图参考生视频 三大工作流合集_2084584790304583681.json, 视频生成/文生视频/开源版MINIMAX-H3 文生视频 图生视频 多图参考生视频 三大工作流合集_2084619362476052481.json, 视频生成/文生视频/极速版+高质开源MiniMax+H3+RE2VA开源版-多图参考生视频_2087042755322277889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_65

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/minimax文字出视频_2084271438885904386.json、视频生成/文生视频/video_minimax_h3_r2v 多素材联合参考_2085213870431490049.json、视频生成/文生视频/video_minimax_h3_r2v多参=加速_2095122591458615297.json、视频生成/文生视频/video_minimax_h3_r2v多参考生视频_2084510984789647362.json、视频生成/文生视频/video_minimax_h3_t2v_2084126777605181442.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LoadImage` —— 8/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `LoadAudio` —— 7/10 个有
- `JjkText` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `MiniMaxH3ImageToVideo` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `H3SigmaRefiner` —— 2/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `DF_Float` —— 1/10 个有
- `EasyCache` —— 1/10 个有
- `Int` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
