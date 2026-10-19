---
name: unknown_workflow_upscale_latent_upscale_lora_41
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.901571
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2040262792845987841.json, 视频生成/图生视频/2037900927323082754.json, 视频生成/图生视频/2031368415541202945.json, 视频生成/图生视频/2042446425367257089.json, 视频生成/图生视频/2033785787984125953.json, 视频生成/图生视频/2044285849671569409.json, 视频生成/图生视频/2049770281983549442.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_41

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2040262792845987841.json、视频生成/图生视频/2037900927323082754.json、视频生成/图生视频/2031368415541202945.json、视频生成/图生视频/2042446425367257089.json、视频生成/图生视频/2033785787984125953.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplaceKJ` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `LTXVImgToVideoInplace` —— 5/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `llama_cpp_instruct_adv` —— 5/7 个有
- `llama_cpp_model_loader` —— 5/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `Text` —— 4/7 个有
- `llama_cpp_parameters` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `LTX2_NAG` —— 3/7 个有
- `ResizeImageMaskNode` —— 3/7 个有
- `CR Text Concatenate` —— 2/7 个有
- `INTConstant` —— 2/7 个有
- `ImageBatchMulti` —— 2/7 个有
- `ImageFromBatch+` —— 2/7 个有
- `LTXVAddGuideMulti` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `SimpleCalculatorKJ` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `AspectRatio` —— 1/7 个有
- `Bjornulf_ShowInt` —— 1/7 个有
- `Evaluate Integers` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageConcanateOfUtils` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SDVN Any Show` —— 1/7 个有
- `SamplerCustom` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `TT_img_enc_v2` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
