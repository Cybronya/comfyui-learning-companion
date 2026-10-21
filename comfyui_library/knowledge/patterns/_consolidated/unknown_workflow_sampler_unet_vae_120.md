---
name: unknown_workflow_sampler_unet_vae_120
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.866857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax+H3_全能参考视频工作流_2084920348532887554.json, 视频生成/文生视频/MiniMax-4步加速工作流_2085226868072083458.json, 视频生成/文生视频/MiniMax-H3-参考生视频_2085243192571686914.json, 视频生成/文生视频/MiniMax-H3全能参考工作流-金水1987_2084528401230159874.json, 视频生成/文生视频/MiniMaxH3地表最强阿里3步加速Lora 全能参考速度起飞_2099733663037607937.json, 视频生成/文生视频/Minimax-H3 (电影质感_8步加速版)_2093740212219367425.json, 视频生成/文生视频/minimaxH3UltraFastestTrue4_v80LightningSpeed_2098097827569295361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_120

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/MiniMax+H3_全能参考视频工作流_2084920348532887554.json、视频生成/文生视频/MiniMax-4步加速工作流_2085226868072083458.json、视频生成/文生视频/MiniMax-H3-参考生视频_2085243192571686914.json、视频生成/文生视频/MiniMax-H3全能参考工作流-金水1987_2084528401230159874.json、视频生成/文生视频/MiniMaxH3地表最强阿里3步加速Lora 全能参考速度起飞_2099733663037607937.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
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
- `SaveVideo` —— 6/7 个有
- `LoadAudio` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `VHS_LoadVideo` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `EasyCache` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `RTXVideoSuperResolution` —— 2/7 个有
- `SpectrumApplyMiniMaxH3` —— 2/7 个有
- `easy anythingIndexSwitch` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `Int` —— 1/7 个有
- `LTX_lora_loader` —— 1/7 个有
- `MiniMaxH3BlockCacheT8` —— 1/7 个有
- `MiniMaxH3SigmaShift` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `ModelPreviewOverrideKJ` —— 1/7 个有
- `PixaromaLabel` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
