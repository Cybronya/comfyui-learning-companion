---
name: unknown_workflow_lora_sampler_clip_20
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.950909
common_nodes: [BasicScheduler, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SaveVideo, SimpleMath+, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2058253695313342465.json, 视频生成/图生视频/2060545124828016642.json, 视频生成/图生视频/2058345686520909825.json, 视频生成/图生视频/2053077492440809473.json, 视频生成/图生视频/2053390831737950210.json, 视频生成/图生视频/2066483566602702849.json, 视频生成/图生视频/2057441452547993601.json, 视频生成/图生视频/2057121441094651906.json, 视频生成/图生视频/2060978714996994050.json, 视频生成/图生视频/2051306841547788290.json, 视频生成/图生视频/2051306846396399618.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2058253695313342465.json、视频生成/图生视频/2060545124828016642.json、视频生成/图生视频/2058345686520909825.json、视频生成/图生视频/2053077492440809473.json、视频生成/图生视频/2053390831737950210.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SaveVideo`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `VisualizeSigmasKJ` —— 10/11 个有
- `UNETLoader` —— 8/11 个有
- `DualCLIPLoaderGGUF` —— 7/11 个有
- `PreviewImage` —— 7/11 个有
- `DualCLIPLoader` —— 6/11 个有
- `UnetLoaderGGUF` —— 5/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `StringConstantMultiline` —— 3/11 个有
- `Label (rgthree)` —— 2/11 个有
- `Power Lora Loader (rgthree)` —— 2/11 个有
- `VHS_VideoCombine` —— 2/11 个有
- `DuckHideNode` —— 1/11 个有
- `MuyeTextEditOutput` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `VHS_SelectImages` —— 1/11 个有
- `VRAM_Debug` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | 97 - 361 | 11 | 77% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，观测区间 97 - 361，11 个样本
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
