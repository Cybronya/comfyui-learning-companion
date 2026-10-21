---
name: unknown_workflow_upscale_latent_upscale_lora_50
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.924833
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/2030630367857741826.json, 视频生成/图生视频/2040262792845987841.json, 视频生成/图生视频/2037900927323082754.json, 视频生成/图生视频/2008554221829885954.json, 视频生成/图生视频/2044285849671569409.json, 视频生成/图生视频/2049770281983549442.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_50

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2030630367857741826.json、视频生成/图生视频/2040262792845987841.json、视频生成/图生视频/2037900927323082754.json、视频生成/图生视频/2008554221829885954.json、视频生成/图生视频/2044285849671569409.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
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
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `ManualSigmas` —— 5/6 个有
- `PrimitiveInt` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `VAEDecodeTiled` —— 5/6 个有
- `llama_cpp_instruct_adv` —— 5/6 个有
- `llama_cpp_model_loader` —— 5/6 个有
- `ComfyMathExpression` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `LTXVImgToVideoInplace` —— 4/6 个有
- `LTXVImgToVideoInplaceKJ` —— 4/6 个有
- `SimpleMath+` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `INTConstant` —— 3/6 个有
- `LTX2_NAG` —— 3/6 个有
- `Text` —— 3/6 个有
- `llama_cpp_parameters` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `CR Text Concatenate` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `GetImageSize` —— 2/6 个有
- `ImageBatchMulti` —— 2/6 个有
- `ImageFromBatch+` —— 2/6 个有
- `ImageScaleBy` —— 2/6 个有
- `LTXVAddGuideMulti` —— 2/6 个有
- `LTXVScheduler` —— 2/6 个有
- `ResizeImageMaskNode` —— 2/6 个有
- `SimpleCalculatorKJ` —— 2/6 个有
- `AspectRatio` —— 1/6 个有
- `Bjornulf_ShowInt` —— 1/6 个有
- `ImageConcanateOfUtils` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `Int` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `SamplerCustom` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `TT_img_enc_v2` —— 1/6 个有
- `VAEDecode` —— 1/6 个有
- `llama_cpp_unload_model` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
