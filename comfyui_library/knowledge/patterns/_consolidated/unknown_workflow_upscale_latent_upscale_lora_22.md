---
name: unknown_workflow_upscale_latent_upscale_lora_22
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.888833
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/多图一致性，LTX+2.3，_2045784883724820481.json, 视频生成/图生视频/LTX-2.3+Qwen3.5电影_2030820457208877058.json, 视频生成/图生视频/LTX2.3 i2v 丝滑过度转场+变身效果_2037117341531643906.json, 视频生成/图生视频/LTX2.3 i2v 优化版  提升画面质量~减少运动崩坏_2042604454435889153.json, 视频生成/图生视频/LTX2.3 i2v 优化版_2030584551327670273.json, 视频生成/图生视频/LTX2.3 多图丝滑过度转场+变身效果_2037112524918755329.json, 视频生成/图生视频/LTX2.3+i2v+优化版_2034102193380401154.json, 视频生成/图生视频/LTX2.3-首中尾3帧变身转场特效_2040262792845987841.json, 视频生成/图生视频/Ltx2.3 首尾帧 丝滑过度转场+变身效果_2037115894140248065.json, 视频生成/图生视频/Ltx2.3 首尾帧 优化版_2030985719384121346.json, 视频生成/图生视频/多图一致性，LTX+2.3+首中尾三图+多图参考，顺滑转场，符合物理逻辑，强引导参考，_2044285849671569409.json, 视频生成/图生视频/多图生视频ltx2.3_2049770281983549442.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_22

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/多图一致性，LTX+2.3，_2045784883724820481.json、视频生成/图生视频/LTX-2.3+Qwen3.5电影_2030820457208877058.json、视频生成/图生视频/LTX2.3 i2v 丝滑过度转场+变身效果_2037117341531643906.json、视频生成/图生视频/LTX2.3 i2v 优化版  提升画面质量~减少运动崩坏_2042604454435889153.json、视频生成/图生视频/LTX2.3 i2v 优化版_2030584551327670273.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LTX2_NAG` —— 11/12 个有
- `SaveVideo` —— 11/12 个有
- `ResizeImageMaskNode` —— 9/12 个有
- `ImageResizeKJv2` —— 8/12 个有
- `LTXVImgToVideoInplace` —— 7/12 个有
- `PrimitiveStringMultiline` —— 7/12 个有
- `LTXVImgToVideoInplaceKJ` —— 5/12 个有
- `CR Text` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 4/12 个有
- `ShowText|pysssss` —— 4/12 个有
- `CR Text Concatenate` —— 3/12 个有
- `INTConstant` —— 3/12 个有
- `ImageBatchMulti` —— 3/12 个有
- `ImageFromBatch+` —— 3/12 个有
- `ImageStitch` —— 3/12 个有
- `LTXVAddGuideMulti` —— 3/12 个有
- `SimpleCalculatorKJ` —— 3/12 个有
- `SimpleMath+` —— 3/12 个有
- `easy showAnything` —— 3/12 个有
- `Bjornulf_ShowInt` —— 2/12 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/12 个有
- `LTXVImgToVideoConditionOnly` —— 2/12 个有
- `SamplerCustom` —— 2/12 个有
- `AspectRatio` —— 1/12 个有
- `ImageConcanateOfUtils` —— 1/12 个有
- `PrimitiveBoolean` —— 1/12 个有
- `QZ_ResolutionPreset` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `TT_img_enc_v2` —— 1/12 个有
- `Text` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
