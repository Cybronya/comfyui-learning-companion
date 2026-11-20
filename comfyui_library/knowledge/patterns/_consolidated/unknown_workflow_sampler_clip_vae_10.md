---
name: unknown_workflow_sampler_clip_vae_10
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.936846
common_nodes: [BasicScheduler, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, PathchSageAttentionKJ, SamplerCustom, SaveVideo, SimpleMath+, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/文生图/（黑鹤UP主的）▶▶LTX23-文生视频流_2051306835285692417.json, 视频生成/图生视频/(黑鹤UP）LTX23-单多图分段控制(任意图数)2_2055789826540097537.json, 视频生成/图生视频/GS-LTX2.3单图生视频效果超棒工作流_2058253695313342465.json, 视频生成/图生视频/LTX2.3 图生视频作流_2060545124828016642.json, 视频生成/图生视频/LTX2.3 图生视频超快工作流-8G可用_2058345686520909825.json, 视频生成/图生视频/LTX2.3-单采样-4图慢剧视频_2053077492440809473.json, 视频生成/图生视频/LTX2.3-单采样-5图叙事慢剧视频_2053390831737950210.json, 视频生成/图生视频/LTX2.3图生视频_2066483566602702849.json, 视频生成/图生视频/LTX23-单图生视频流_2057441452547993601.json, 视频生成/图生视频/▶▶LTX23--情绪强化-单图生视频_2057121441094651906.json, 视频生成/图生视频/▶▶LTX23--情绪强化-单图生视频_2060978714996994050.json, 视频生成/图生视频/（黑鹤UP主的）▶▶LTX23-单图生视频流_2051306841547788290.json, 视频生成/图生视频/（黑鹤UP主的）▶▶LTX23-首尾帧视频(双图)_2051306846396399618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_10

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/（黑鹤UP主的）▶▶LTX23-文生视频流_2051306835285692417.json、视频生成/图生视频/(黑鹤UP）LTX23-单多图分段控制(任意图数)2_2055789826540097537.json、视频生成/图生视频/GS-LTX2.3单图生视频效果超棒工作流_2058253695313342465.json、视频生成/图生视频/LTX2.3 图生视频作流_2060545124828016642.json、视频生成/图生视频/LTX2.3 图生视频超快工作流-8G可用_2058345686520909825.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
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
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SaveVideo`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/13 个有
- `VisualizeSigmasKJ` —— 12/13 个有
- `LTXVImgToVideoInplaceKJ` —— 11/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/13 个有
- `LTXVPreprocess` —— 10/13 个有
- `LoadImage` —— 10/13 个有
- `DualCLIPLoaderGGUF` —— 9/13 个有
- `UNETLoader` —— 9/13 个有
- `PreviewImage` —— 8/13 个有
- `DualCLIPLoader` —— 7/13 个有
- `UnetLoaderGGUF` —— 7/13 个有
- `Power Lora Loader (rgthree)` —— 4/13 个有
- `VHS_VideoCombine` —— 4/13 个有
- `ImageResizeKJv2` —— 3/13 个有
- `StringConstantMultiline` —— 3/13 个有
- `Label (rgthree)` —— 2/13 个有
- `ComfyMathExpression` —— 1/13 个有
- `DuckHideNode` —— 1/13 个有
- `ImageFromBatch` —— 1/13 个有
- `LTXSequencer` —— 1/13 个有
- `MultiImageLoader` —— 1/13 个有
- `MuyeTextEditOutput` —— 1/13 个有
- `PromptRelayEncodeTimeline` —— 1/13 个有
- `SaveImage` —— 1/13 个有
- `VHS_SelectImages` —— 1/13 个有
- `VRAM_Debug` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | 97 - 361 | 13 | 79% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，观测区间 97 - 361，13 个样本
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
