---
name: unknown_workflow_sampler_unet_vae_26
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.861667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2-MiniMax-H3-单图-首尾帧生视频工作流V2_2084639140699795458.json, 视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json, 视频生成/图生视频/360度旋转_minimax_h3_2109928610961387522.json, 视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2100287204726755329.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2107413322575470593.json, 视频生成/图生视频/FastVideo-FastH3-8-Step-V2 图生视频_2101581826061062145.json, 视频生成/图生视频/H3 关键帧视频动画_2106371268684636162.json, 视频生成/图生视频/H3-图生视频-首尾帧_2087831020287643649.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2101850161256423426.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2104052395767582721.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播5秒_2101848980366913538.json, 视频生成/图生视频/fastvideo_fasth3_图生视频_2101837609382277121.json, 视频生成/文生视频/1-MiniMaxh-H3-文生视频工作流-V2_2084639097741725698.json, 视频生成/文生视频/3-MiniMax-H3-参考生视频工作流-V2_2084639172459065346.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_26

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/2-MiniMax-H3-单图-首尾帧生视频工作流V2_2084639140699795458.json、视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json、视频生成/图生视频/360度旋转_minimax_h3_2109928610961387522.json、视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json、视频生成/图生视频/FastVideo FastH3：图生视频_2100287204726755329.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 14/15 个有
- `VAEDecodeAudio` —— 14/15 个有
- `MiniMaxH3ImageToVideo` —— 13/15 个有
- `MiniMaxH3SigmaShift` —— 11/15 个有
- `GetImageSize` —— 10/15 个有
- `ImageScaleToTotalPixels` —— 10/15 个有
- `ModelAttentionBackend` —— 10/15 个有
- `BlockSparseAttention` —— 7/15 个有
- `LoraLoaderModelOnly` —— 6/15 个有
- `ResolutionSelector` —— 6/15 个有
- `Fast Groups Bypasser (rgthree)` —— 3/15 个有
- `MiniMaxH3ContextIR` —— 3/15 个有
- `MiniMaxH3ReferenceToVideo` —— 2/15 个有
- `PrimitiveInt` —— 2/15 个有
- `PrimitiveStringMultiline` —— 2/15 个有
- `ShowText|pysssss` —— 2/15 个有
- `Text` —— 2/15 个有
- `EmptyImage` —— 1/15 个有
- `PreviewAny` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `SaveImage` —— 1/15 个有
- `VHS_LoadAudioUpload` —— 1/15 个有
- `VHS_LoadVideo` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
