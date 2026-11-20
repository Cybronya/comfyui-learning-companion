---
name: unknown_workflow_video_upscale_latent_upscale_60
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.535857
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, JDC_ResizeFactor, KSamplerSelect, LTX2_NAG, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, ResizeImagesByLongerEdge, SamplerCustom, Seed (rgthree), SetNode, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【数字人唱歌】LTX2.3_2057291924830248961.json, 视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json, 视频生成/文生视频/LTX-2.3+数字人对口型多人对话唱歌+高清画质工作流_2069356013098196994.json, 视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2099902577730220034.json, 视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2100620352736022529.json, 视频生成/文生视频/文生视频_+_图生视频_二合一工作流_2100755479424233473.json, 视频生成/文生视频/文生视频_+_图生视频_二合一工作流_2101124003149733889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_60

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/【数字人唱歌】LTX2.3_2057291924830248961.json、视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json、视频生成/文生视频/LTX-2.3+数字人对口型多人对话唱歌+高清画质工作流_2069356013098196994.json、视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2099902577730220034.json、视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2100620352736022529.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `JDC_ResizeFactor`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `ResizeImagesByLongerEdge`
- `SamplerCustom`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEDecode` —— 6/7 个有
- `LTXVEmptyLatentAudio` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `JoinStrings` —— 5/7 个有
- `LTX2SamplingPreviewOverride` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `RH_LLMAPI_NODE` —— 5/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `SimpleCalculatorKJ` —— 5/7 个有
- `TextInput_` —— 5/7 个有
- `AudioCrop` —— 2/7 个有
- `AudioInfo` —— 2/7 个有
- `Display Any (rgthree)` —— 2/7 个有
- `LTXVAudioVAEEncode` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `LoadAudio` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `SetLatentNoiseMask` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `SolidMask` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `FlashVSRInitPipe` —— 1/7 个有
- `FlashVSRNodeAdv` —— 1/7 个有
- `MelBandRoFormerModelLoader` —— 1/7 个有
- `MelBandRoFormerSampler` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 6 | 100% |
| 高度 | 24 | 24 - 24 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，6 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，6 个样本，取值集中（一致性 100%）
