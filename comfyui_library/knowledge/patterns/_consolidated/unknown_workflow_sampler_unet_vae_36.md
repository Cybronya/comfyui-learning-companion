---
name: unknown_workflow_sampler_unet_vae_36
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.845062
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2101850161256423426.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2104052395767582721.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播5秒_2101848980366913538.json, 视频生成/图生视频/fastvideo_fasth3_图生视频_2101837609382277121.json, 视频生成/图生视频/minimax H3 开源版图生视频-4步加速极速版_2087727783698059266.json, 视频生成/图生视频/minimax H3 开源版图生视频_2084165222453039105.json, 视频生成/图生视频/minimax_h3_i2v_videoonly_2090443654421897217.json, 视频生成/图生视频/minimax_h3_i2v图生视频_2084166438562127874.json, 视频生成/图生视频/minimax_h3_图生视频_2084537327996719106.json, 视频生成/图生视频/minimax_h3_图生视频西瓜宝宝工作流_2084397677135089665.json, 视频生成/图生视频/minimax_h3_迷你别墅视频工作流_2084267933227900930.json, 视频生成/图生视频/minimax_h3图生视频（稳定）_2085014325353340930.json, 视频生成/图生视频/minnimax h3 首尾帧生视频（4步加速）_2085544529314271234.json, 视频生成/图生视频/minnimax h3 首帧生视频（8步加速）_2085549343964221442.json, 视频生成/图生视频/【老金驿站】MinimaxH3超级加速40%i2v工作流_2087177800716476417.json, 视频生成/文生视频/海螺H3首尾帧生视频_2087721274360553473.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_36

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2101850161256423426.json、视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2104052395767582721.json、视频生成/图生视频/fastvideo_fasth3_图生视频-口播5秒_2101848980366913538.json、视频生成/图生视频/fastvideo_fasth3_图生视频_2101837609382277121.json、视频生成/图生视频/minimax H3 开源版图生视频-4步加速极速版_2087727783698059266.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 16 个 workflow 都包含：
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
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 15/16 个有
- `GetImageSize` —— 14/16 个有
- `ImageScaleToTotalPixels` —— 14/16 个有
- `ResolutionSelector` —— 12/16 个有
- `MiniMaxH3SigmaShift` —— 5/16 个有
- `ModelAttentionBackend` —— 5/16 个有
- `BlockSparseAttention` —— 4/16 个有
- `LoraLoaderModelOnly` —— 4/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/16 个有
- `PreviewImage` —— 3/16 个有
- `EmptyImage` —— 2/16 个有
- `PathchSageAttentionKJ` —— 2/16 个有
- `PrimitiveStringMultiline` —— 2/16 个有
- `ResizeImageMaskNode` —— 2/16 个有
- `BOOLConstant` —— 1/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/16 个有
- `MiniMaxH3TurboLoRA` —— 1/16 个有
- `TeaCache` —— 1/16 个有
- `easy imageIndexSwitch` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
