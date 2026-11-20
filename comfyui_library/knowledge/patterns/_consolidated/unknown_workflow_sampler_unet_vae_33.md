---
name: unknown_workflow_sampler_unet_vae_33
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.821833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Minimax+H3+I2v_首尾帧+(好用）_2085173384211685378.json, 图片生成/图生图/Minimax-h3首尾帧版-天运子_2084529125984923650.json, 图片生成/图生图/trim fast minimax_2107875369050267650.json, 视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2100287204726755329.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2107413322575470593.json, 视频生成/图生视频/FastVideo-FastH3-8-Step-V2 图生视频_2101581826061062145.json, 视频生成/图生视频/MiniMax H3 首尾帧生视频_2084510292645601281.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧 (加速版，去动态噪点）_2084495129297121281.json, 视频生成/图生视频/Minimax H3 图生视频_首尾帧 (加速版，去高动态噪点）_2088505534927433729.json, 视频生成/图生视频/Minimax H3-图生视频（高动态去噪点）_2089348010357641217.json, 视频生成/图生视频/Minimax+H3+I2v_首尾帧+(加速版，去动态噪点）_2089185922914021377.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2101850161256423426.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播5秒_2101848980366913538.json, 视频生成/图生视频/fastvideo_fasth3_图生视频_2101837609382277121.json, 视频生成/图生视频/地表最强Minimax-h3图生视频版_2084422222730588162.json, 视频生成/图生视频/地表最强Minimax-h3完美首尾帧版_2084469809009483778.json, 视频生成/文生视频/地表最强开源视频！Minimax-h3 文生丨图生视频版 26-08-03_2084186070467567618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_33

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Minimax+H3+I2v_首尾帧+(好用）_2085173384211685378.json、图片生成/图生图/Minimax-h3首尾帧版-天运子_2084529125984923650.json、图片生成/图生图/trim fast minimax_2107875369050267650.json、视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json、视频生成/图生视频/FastVideo FastH3：图生视频_2100287204726755329.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
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
- `ImageScaleToTotalPixels` —— 17/18 个有
- `GetImageSize` —— 13/18 个有
- `ResolutionSelector` —— 11/18 个有
- `ModelAttentionBackend` —— 8/18 个有
- `PathchSageAttentionKJ` —— 8/18 个有
- `BlockSparseAttention` —— 7/18 个有
- `MiniMaxH3SigmaShift` —— 7/18 个有
- `CR Text` —— 4/18 个有
- `EasyCache` —— 4/18 个有
- `ImageCrop+` —— 4/18 个有
- `ImageScale` —— 4/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/18 个有
- `LayerUtility: TextBox` —— 4/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/18 个有
- `孤海注释` —— 4/18 个有
- `Note Plus (mtb)` —— 3/18 个有
- `ExtendIntermediateSigmas` —— 2/18 个有
- `H3SigmaRefiner` —— 2/18 个有
- `LoraLoaderModelOnly` —— 2/18 个有
- `PrimitiveStringMultiline` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
