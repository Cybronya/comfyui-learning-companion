---
name: unknown_workflow_lora_sampler_clip_31
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.851
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, SimpleMath+, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/74wsspduoren_2052611683218145282.json, 视频生成/图生视频/LTX2.3 -首尾帧双图生视频-长镜头一镜到底-提示词高遵从-直出1K_2057749829224329218.json, 视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 优化版_2033038199701905410.json, 视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 音频克隆(附带音色设计) 优化版_2033197165668999170.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2033156764371263490.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2044341747362304001.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2052949271544123393.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版「Supermate」_2047731840944967682.json, 视频生成/图生视频/LTX2.3 _ 首尾帧 快速优化版_2044586983204327425.json, 视频生成/图生视频/LTX2.3 _ 首尾帧 视频_2052216878214467585.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/74wsspduoren_2052611683218145282.json、视频生成/图生视频/LTX2.3 -首尾帧双图生视频-长镜头一镜到底-提示词高遵从-直出1K_2057749829224329218.json、视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 优化版_2033038199701905410.json、视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 音频克隆(附带音色设计) 优化版_2033197165668999170.json、视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2033156764371263490.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleMath+`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `FloatConstant` —— 9/10 个有
- `LTXVCropGuides` —— 9/10 个有
- `LTXVEmptyLatentAudio` —— 9/10 个有
- `LTXVImgToVideoInplace` —— 9/10 个有
- `LTXVImgToVideoInplaceKJ` —— 9/10 个有
- `LTXVLatentUpsampler` —— 9/10 个有
- `LatentUpscaleModelLoader` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `RH_LLMAPI_Pro_Node` —— 9/10 个有
- `LTXVPreprocess` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `ResizeImagesByLongerEdge` —— 8/10 个有
- `Resize` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `ResizeImageMaskNode` —— 2/10 个有
- `easy int` —— 2/10 个有
- `kkResize` —— 2/10 个有
- `Bjornulf_ShowInt` —— 1/10 个有
- `CM_FloatToInt` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `LTXVAudioVAEEncode` —— 1/10 个有
- `LTXVScheduler` —— 1/10 个有
- `PainterAudioLength` —— 1/10 个有
- `RTXVideoSuperResolution` —— 1/10 个有
- `ResizeAndPadImage` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `SetLatentNoiseMask` —— 1/10 个有
- `SolidMask` —— 1/10 个有
- `easy float` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 24 - 25 | 9 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，9 个样本，取值集中（一致性 99%）
