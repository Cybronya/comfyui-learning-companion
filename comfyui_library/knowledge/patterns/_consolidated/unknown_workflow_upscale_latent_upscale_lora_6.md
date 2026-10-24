---
name: unknown_workflow_upscale_latent_upscale_lora_6
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.8705
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版「Supermate」_2047731840944967682.json, 视频生成/图生视频/LTX2.3 _ 首尾帧 快速优化版_2044586983204327425.json, 视频生成/图生视频/LTX2.3 _ 首尾帧 视频_2052216878214467585.json, 视频生成/图生视频/LTX2.3 中间帧+图生视频 三图-首中尾帧+优化版_2051164751694184449.json, 视频生成/图生视频/LTX2.3 全自动提示词--首中尾帧三图生视频_2035325465820405761.json, 视频生成/图生视频/LTX2.3 数字人艾希&李小小《我们都是数字人》播客生产工作流 V3.00331_2038794251055669250.json, 视频生成/图生视频/LTX2.3 首中尾三帧图生视频 (定)_2042205939977162753.json, 视频生成/图生视频/LTX2.3 首中尾三帧图生视频 (定)_2042240826851463170.json, 视频生成/图生视频/LTX2.3+中间帧+图生视频优化版+三图-首中尾帧_2063794873710501890.json, 视频生成/图生视频/LTX2.3-五图生视频10秒电商展示变装-全自动提示词_2051490555791720450.json, 视频生成/图生视频/LTX2.3-五图生视频15秒电商展示变装-全自动提示词_2051660543777361922.json, 视频生成/图生视频/LTX2.3_自动【首尾帧】视频工作流优化版_2032374429937836033.json, 视频生成/图生视频/LTX2.3_自动【首尾帧】视频工作流优化版_2032414154048413698.json, 视频生成/图生视频/LTX2.3_首尾帧 视频工作流_2033429258751709185.json, 视频生成/图生视频/LTX2.3自动首中尾三帧视频_2031361873404239873.json, 视频生成/图生视频/LTX2.3自动首中尾三帧视频（自用）_2036273219824521217.json, 视频生成/图生视频/LTX2.3首尾帧【 提示词自动优化版 】_2042812427200372738.json, 视频生成/图生视频/LTX2.3首尾帧双图生视频-单镜头自动提示词版本_2051217425542201345.json, 视频生成/图生视频/LTX2.3首尾帧双图生视频-手动提示词版--注释含提示词模板_2051911216334942209.json, 视频生成/图生视频/opsv-ltx2.3首尾帧_2054734557966020610.json, 视频生成/图生视频/opsv-首尾帧_2050610398684041217.json, 视频生成/图生视频/全能图片G 2.0+LTX2.3文生图首尾帧生视频&自动提示词版本_2051654152509501441.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_6

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版「Supermate」_2047731840944967682.json、视频生成/图生视频/LTX2.3 _ 首尾帧 快速优化版_2044586983204327425.json、视频生成/图生视频/LTX2.3 _ 首尾帧 视频_2052216878214467585.json、视频生成/图生视频/LTX2.3 中间帧+图生视频 三图-首中尾帧+优化版_2051164751694184449.json、视频生成/图生视频/LTX2.3 全自动提示词--首中尾帧三图生视频_2035325465820405761.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 22 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
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
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 21/22 个有
- `RH_LLMAPI_Pro_Node` —— 21/22 个有
- `LTXVPreprocess` —— 20/22 个有
- `FloatConstant` —— 19/22 个有
- `PrimitiveInt` —— 19/22 个有
- `SimpleMath+` —— 19/22 个有
- `CreateVideo` —— 18/22 个有
- `SaveVideo` —— 18/22 个有
- `LTXVChunkFeedForward` —— 16/22 个有
- `ModelPatchTorchSettings` —— 16/22 个有
- `PathchSageAttentionKJ` —— 16/22 个有
- `PrimitiveStringMultiline` —— 16/22 个有
- `ResizeImagesByLongerEdge` —— 15/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/22 个有
- `ResizeImageMaskNode` —— 7/22 个有
- `CR Prompt Text` —— 6/22 个有
- `DualCLIPLoader` —— 6/22 个有
- `PreviewAny` —— 6/22 个有
- `TextGenerateLTX2Prompt` —— 6/22 个有
- `ImageResizeKJv2` —— 5/22 个有
- `Resize` —— 4/22 个有
- `TextCombinerTwo` —— 4/22 个有
- `VHS_VideoCombine` —— 4/22 个有
- `Int` —— 3/22 个有
- `PreviewImage` —— 3/22 个有
- `easy int` —— 3/22 个有
- `ColorMatchV2` —— 2/22 个有
- `Fast Groups Bypasser (rgthree)` —— 2/22 个有
- `CR Text Concatenate` —— 1/22 个有
- `Image Resize` —— 1/22 个有
- `ImageSizeInfo` —— 1/22 个有
- `RHHiddenNodes` —— 1/22 个有
- `RH_RhartImageG2TextToImage` —— 1/22 个有
- `ResizeAndPadImage` —— 1/22 个有
- `easy mathInt` —— 1/22 个有
- `kkResize` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 22 | 100% |
| 高度 | 25 | 25 - 25 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，22 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，22 个样本，取值集中（一致性 100%）
