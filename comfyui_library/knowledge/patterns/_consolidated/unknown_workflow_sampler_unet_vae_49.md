---
name: unknown_workflow_sampler_unet_vae_49
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.857364
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3多条件参考视频工作流低显存加速版 开源 Ref2VA_2084437517675352065.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成_2084247428697518082.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2085948478043283457.json, 视频生成/图生视频/MiniMax-H3全能参考工作流_2084872705010130945.json, 视频生成/图生视频/MiniMaxH3_KeyFarmes_X2（二关键帧）视频生成工作流_2094650229818748929.json, 视频生成/图生视频/MiniMaxH3_KeyFarmes_X4（四关键帧）视频生成工作流_2094650342708436993.json, 视频生成/图生视频/minimax_h3_全能参考（参考视频输入）_2085193849571463169.json, 视频生成/图生视频/加速版Minimax多参生视频BF16高质量-sage+Block Cache (T8)_2085374592817909762.json, 视频生成/文生视频/MiniMax H3+ 新4步LoRa + 参考图图生视频工作流_2092505916875829250.json, 视频生成/文生视频/video_minimax_h3_r2v多参=加速_2095122591458615297.json, 视频生成/文生视频/极速版+高质开源MiniMax+H3+RE2VA开源版-多图参考生视频_2087042755322277889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_49

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多条件参考视频工作流低显存加速版 开源 Ref2VA_2084437517675352065.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成_2084247428697518082.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2085948478043283457.json、视频生成/图生视频/MiniMax-H3全能参考工作流_2084872705010130945.json、视频生成/图生视频/MiniMaxH3_KeyFarmes_X2（二关键帧）视频生成工作流_2094650229818748929.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
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
- `LoadImage` —— 10/11 个有
- `PrimitiveStringMultiline` —— 7/11 个有
- `VHS_LoadVideo` —— 7/11 个有
- `LoadAudio` —— 5/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `ModelAttentionBackend` —— 4/11 个有
- `PathchSageAttentionKJ` —— 4/11 个有
- `Label (rgthree)` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `H3SigmaRefiner` —— 2/11 个有
- `MiniMaxH3AddGuide` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有
- `CS-MultiImageLoader` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `Int` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `VHS_LoadAudioUpload` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
