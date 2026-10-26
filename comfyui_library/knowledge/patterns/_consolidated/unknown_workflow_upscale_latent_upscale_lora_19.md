---
name: unknown_workflow_upscale_latent_upscale_lora_19
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.848769
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 电商专用图文生视频-提示词响应优化_2061384649385009154.json, 视频生成/图生视频/LTX2.3 真人高清一键长视频工作流 V2.3_2038518064030945282.json, 视频生成/图生视频/LTX2.3 首中尾三帧图生视频 (定)_2042205939977162753.json, 视频生成/图生视频/LTX2.3 首中尾三帧图生视频 (定)_2042240826851463170.json, 视频生成/图生视频/LTX2.3+中间帧+图生视频优化版+三图-首中尾帧_2063794873710501890.json, 视频生成/图生视频/LTX2.3首尾帧【 提示词自动优化版 】_2042812427200372738.json, 视频生成/图生视频/opsv-ltx2.3首尾帧_2054734557966020610.json, 视频生成/图生视频/opsv-首尾帧_2050610398684041217.json, 视频生成/图生视频/双人对话 LTX2.3+中间帧+图生视频优化版+三图-首中尾帧_2054745328590565377.json, 视频生成/图生视频/图生视频 中间帧 首中尾帧 LTX2.3_2033530948851081217.json, 视频生成/图生视频/老孙AI  三图-首中尾帧 视频_2086324689701531649.json, 视频生成/图生视频/首尾帧图生视频 LTX2.3  Fisher大佬优化版_2033537132236640258.json, 视频生成/文生视频/LTX2.3+中间帧+图生视频优化版+三图-首中尾帧_2052272204712300545.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_19

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 电商专用图文生视频-提示词响应优化_2061384649385009154.json、视频生成/图生视频/LTX2.3 真人高清一键长视频工作流 V2.3_2038518064030945282.json、视频生成/图生视频/LTX2.3 首中尾三帧图生视频 (定)_2042205939977162753.json、视频生成/图生视频/LTX2.3 首中尾三帧图生视频 (定)_2042240826851463170.json、视频生成/图生视频/LTX2.3+中间帧+图生视频优化版+三图-首中尾帧_2063794873710501890.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
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
- `ComfyMathExpression` —— 12/13 个有
- `PrimitiveStringMultiline` —— 12/13 个有
- `RH_LLMAPI_Pro_Node` —— 12/13 个有
- `SimpleMath+` —— 12/13 个有
- `FloatConstant` —— 11/13 个有
- `LTXVChunkFeedForward` —— 11/13 个有
- `LTXVImgToVideoInplaceKJ` —— 11/13 个有
- `ModelPatchTorchSettings` —— 11/13 个有
- `PathchSageAttentionKJ` —— 11/13 个有
- `ResizeImagesByLongerEdge` —— 10/13 个有
- `ImageResizeKJv2` —— 9/13 个有
- `ResizeImageMaskNode` —— 9/13 个有
- `TextCombinerTwo` —— 8/13 个有
- `VHS_VideoCombine` —— 8/13 个有
- `CreateVideo` —— 5/13 个有
- `Fast Groups Bypasser (rgthree)` —— 5/13 个有
- `SaveVideo` —— 5/13 个有
- `ColorMatchV2` —— 2/13 个有
- `PrimitiveBoolean` —— 2/13 个有
- `BDXTestInt` —— 1/13 个有
- `Image Resize` —— 1/13 个有
- `JoinStrings` —— 1/13 个有
- `MultiplicationNode` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `Qwen3_VQA` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `Resize` —— 1/13 个有
- `Text Multiline` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
