---
name: unknown_workflow_sampler_unet_vae_116
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3单图生视频版_2093705769144373249.json, 视频生成/图生视频/MiniMax-H3开源 单图生视频版_2094011380541247489.json, 视频生成/图生视频/Minimax-h3图生视频版_2084511817468039169.json, 视频生成/图生视频/minimax H3 开源版图生视频_2084165222453039105.json, 视频生成/图生视频/minimax h3 竖屏版_2084459891346993153.json, 视频生成/图生视频/【傲雪AIGC】MiniMax+H3首尾帧生视频版_2093696527855341570.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_116

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3单图生视频版_2093705769144373249.json、视频生成/图生视频/MiniMax-H3开源 单图生视频版_2094011380541247489.json、视频生成/图生视频/Minimax-h3图生视频版_2084511817468039169.json、视频生成/图生视频/minimax H3 开源版图生视频_2084165222453039105.json、视频生成/图生视频/minimax h3 竖屏版_2084459891346993153.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `CreateVideo` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `ImageCrop+` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `VHS_LoadVideoFFmpeg` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `Text` —— 2/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `TeaCache` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
