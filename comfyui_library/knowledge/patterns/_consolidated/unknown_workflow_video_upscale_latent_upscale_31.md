---
name: unknown_workflow_video_upscale_latent_upscale_31
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.459167
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2055850166728577025.json, 视频生成/图生视频/2059931289700102145.json, 视频生成/图生视频/2045427683621871617.json, 视频生成/图生视频/2045565510112251906.json, 视频生成/图生视频/2044453497332043777.json, 视频生成/图生视频/2055968633255407618.json, 视频生成/图生视频/2079551168036032513.json, 视频生成/图生视频/2044570790150017026.json, 视频生成/图生视频/2016770696625524737.json, 视频生成/图生视频/数字人直播、影视预演，情绪演绎 表情调节 人物表情控制，视频生成ltx2.3_2082710649158848514.json, 视频生成/图生视频/2081587131981590529.json, 视频生成/图生视频/2058014119055421441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_31

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2055850166728577025.json、视频生成/图生视频/2059931289700102145.json、视频生成/图生视频/2045427683621871617.json、视频生成/图生视频/2045565510112251906.json、视频生成/图生视频/2044453497332043777.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTX2_NAG` —— 11/12 个有
- `LTXVScheduler` —— 11/12 个有
- `LTXVImgToVideoConditionOnly` —— 9/12 个有
- `CheckpointLoaderSimple` —— 8/12 个有
- `PathchSageAttentionKJ` —— 8/12 个有
- `PrimitiveStringMultiline` —— 8/12 个有
- `CR Text Concatenate` —— 7/12 个有
- `JWInteger` —— 7/12 个有
- `JjkText` —— 7/12 个有
- `ModelPatchTorchSettings` —— 7/12 个有
- `ShowText|pysssss` —— 7/12 个有
- `easy anythingIndexSwitch` —— 7/12 个有
- `LTXVImgToVideoInplace` —— 5/12 个有
- `ResizeImagesByLongerEdge` —— 5/12 个有
- `UNETLoader` —— 5/12 个有
- `ImageScaleBy` —— 4/12 个有
- `LTX2SamplingPreviewOverride` —— 4/12 个有
- `LTXVAddGuideMulti` —— 2/12 个有
- `LTXVCropGuides` —— 2/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有
- `CR Text` —— 1/12 个有
- `ConcatTextOfUtils` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `LTXVChunkFeedForward` —— 1/12 个有
- `LTXVImgToVideoInplaceKJ` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有
- `ResizeImageMaskNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 12 | 90% |
| 高度 | 24 | 24 - 25 | 12 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，12 个样本，取值集中（一致性 90%）
- 高度 中位数 24，观测区间 24 - 25，12 个样本，取值集中（一致性 98%）
