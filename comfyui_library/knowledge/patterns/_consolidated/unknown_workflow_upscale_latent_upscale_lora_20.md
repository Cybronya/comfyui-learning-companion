---
name: unknown_workflow_upscale_latent_upscale_lora_20
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.850167
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2061384649385009154.json, 视频生成/图生视频/2038518064030945282.json, 视频生成/图生视频/2042205939977162753.json, 视频生成/图生视频/2042240826851463170.json, 视频生成/图生视频/2063794873710501890.json, 视频生成/图生视频/2031273311556079618.json, 视频生成/图生视频/2042812427200372738.json, 视频生成/图生视频/2054734557966020610.json, 视频生成/图生视频/2050610398684041217.json, 视频生成/图生视频/2054745328590565377.json, 视频生成/图生视频/2033530948851081217.json, 视频生成/图生视频/老孙AI  三图-首中尾帧 视频_2086324689701531649.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_20

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2061384649385009154.json、视频生成/图生视频/2038518064030945282.json、视频生成/图生视频/2042205939977162753.json、视频生成/图生视频/2042240826851463170.json、视频生成/图生视频/2063794873710501890.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 11/12 个有
- `PrimitiveStringMultiline` —— 11/12 个有
- `RH_LLMAPI_Pro_Node` —— 11/12 个有
- `ResizeImagesByLongerEdge` —— 10/12 个有
- `SimpleMath+` —— 10/12 个有
- `FloatConstant` —— 9/12 个有
- `LTXVChunkFeedForward` —— 9/12 个有
- `LTXVImgToVideoInplaceKJ` —— 9/12 个有
- `ModelPatchTorchSettings` —— 9/12 个有
- `PathchSageAttentionKJ` —— 9/12 个有
- `ResizeImageMaskNode` —— 9/12 个有
- `ImageResizeKJv2` —— 7/12 个有
- `CreateVideo` —— 6/12 个有
- `SaveVideo` —— 6/12 个有
- `TextCombinerTwo` —— 6/12 个有
- `VHS_VideoCombine` —— 6/12 个有
- `Fast Groups Bypasser (rgthree)` —— 4/12 个有
- `PrimitiveBoolean` —— 3/12 个有
- `ColorMatchV2` —— 2/12 个有
- `BDXTestInt` —— 1/12 个有
- `Image Resize` —— 1/12 个有
- `JoinStrings` —— 1/12 个有
- `MultiplicationNode` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `Qwen3_VQA` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `Resize` —— 1/12 个有
- `Text Multiline` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy ifElse` —— 1/12 个有

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
