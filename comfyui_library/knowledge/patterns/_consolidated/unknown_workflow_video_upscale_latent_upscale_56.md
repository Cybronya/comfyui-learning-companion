---
name: unknown_workflow_video_upscale_latent_upscale_56
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.468143
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/AI控制人物表情！LTX2.3图生视频！B站艾橘溪！_2055850166728577025.json, 视频生成/图生视频/AI控制人物表情！LTX2.3图生视频！_2059931289700102145.json, 视频生成/图生视频/LTX-2.3-图生视频_2055514596210946049.json, 视频生成/图生视频/LTX-2.3-首尾帧_2055556105299873793.json, 视频生成/图生视频/LTX-2.3图生视频（极速版）_2045427683621871617.json, 视频生成/图生视频/LTX-2.3首尾帧+语音数字人_2036654957595725826.json, 视频生成/图生视频/LTX2.3 TI2V Audio 图片音频类数字人(超极速版7分钟20秒视频)_2075071109761949697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_56

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/AI控制人物表情！LTX2.3图生视频！B站艾橘溪！_2055850166728577025.json、视频生成/图生视频/AI控制人物表情！LTX2.3图生视频！_2059931289700102145.json、视频生成/图生视频/LTX-2.3-图生视频_2055514596210946049.json、视频生成/图生视频/LTX-2.3-首尾帧_2055556105299873793.json、视频生成/图生视频/LTX-2.3图生视频（极速版）_2045427683621871617.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
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
- `LTXVEmptyLatentAudio` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `LTXVImgToVideoInplace` —— 5/7 个有
- `ResizeImagesByLongerEdge` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `LTX2SamplingPreviewOverride` —— 4/7 个有
- `ModelPatchTorchSettings` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `ImageScaleBy` —— 3/7 个有
- `LTXVChunkFeedForward` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `CR Text Concatenate` —— 2/7 个有
- `CheckpointLoaderSimple` —— 2/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `LTXVAudioVAEEncode` —— 2/7 个有
- `LTXVImgToVideoConditionOnly` —— 2/7 个有
- `LTXVImgToVideoInplaceKJ` —— 2/7 个有
- `LoadAudio` —— 2/7 个有
- `MelBandRoFormerModelLoader` —— 2/7 个有
- `MelBandRoFormerSampler` —— 2/7 个有
- `ResizeImageMaskNode` —— 2/7 个有
- `SetLatentNoiseMask` —— 2/7 个有
- `SolidMask` —— 2/7 个有
- `easy anythingIndexSwitch` —— 2/7 个有
- `AudioCrop` —— 1/7 个有
- `AudioInfo` —— 1/7 个有
- `JWFloatToInteger` —— 1/7 个有
- `PainterAudioLength` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `TrimAudioDuration` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy showAnything` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 6 | 90% |
| 高度 | 24.5 | 24 - 25 | 6 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，6 个样本，取值集中（一致性 90%）
- 高度 中位数 24.5，观测区间 24 - 25，6 个样本，取值集中（一致性 98%）
