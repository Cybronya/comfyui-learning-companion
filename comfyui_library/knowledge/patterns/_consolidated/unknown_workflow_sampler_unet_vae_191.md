---
name: unknown_workflow_sampler_unet_vae_191
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.886833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3图生视频&首尾帧 量化加速版_2084545071873093633.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2101850161256423426.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2104052395767582721.json, 视频生成/图生视频/fastvideo_fasth3_图生视频-口播5秒_2101848980366913538.json, 视频生成/图生视频/fastvideo_fasth3_图生视频_2101837609382277121.json, 视频生成/图生视频/海螺H3八步极速生成文图首尾帧视频3合一工作流_2088515866974576641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_191

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3图生视频&首尾帧 量化加速版_2084545071873093633.json、视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2101850161256423426.json、视频生成/图生视频/fastvideo_fasth3_图生视频-口播10秒_2104052395767582721.json、视频生成/图生视频/fastvideo_fasth3_图生视频-口播5秒_2101848980366913538.json、视频生成/图生视频/fastvideo_fasth3_图生视频_2101837609382277121.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetImageSize`
- `ImageScaleToTotalPixels`
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
- `BlockSparseAttention` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `AnyBooleanSwitch` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `CM_BoolBinaryOperation` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `Float` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `ImpactConditionalBranch` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `Switch image [Crystools]` —— 1/6 个有
- `easy float` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
