---
key: 视频生成/图生视频/LTX2.3-VBVR逻辑优化-图生视频-AIGC大赏_2042489551154847745.json
name: LTX2.3-VBVR逻辑优化-图生视频-AIGC大赏_2042489551154847745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042489551154847745.json
hash: de56cacdf7ed3818
coverage: 0.913793
learned_at: 2026-10-15 22:36:28
nodes: [CFGGuider, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, LTXVImgToVideoInplace, LTXVSeparateAVLatent, SamplerCustomAdvanced, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVScheduler, KSamplerSelect, SamplerCustomAdvanced, GetNode, CM_IntToFloat, SetNode, LTXVImgToVideoInplace, PathchSageAttentionKJ, ModelPatchTorchSettings, LatentUpscaleModelLoader, VAELoaderKJ, VAELoaderKJ, LTXVEmptyLatentAudio, LTXVConditioning, GetNode, LTXVPreprocess, LTXVChunkFeedForward, INTConstant, ResizeImagesByLongerEdge, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, DualCLIPLoader, LTXVAudioVAEDecode, VAEDecodeTiled, SimpleCalculatorKJ, EmptyLTXVLatentVideo, INTConstant, INTConstant, llama_cpp_model_loader, llama_cpp_instruct_adv, CLIPTextEncode, UNETLoader, SaveImage, LoadImage, CFGGuider, RandomNoise, CR Text, CLIPTextEncode, Anything Everywhere3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, TT_img_enc_v2, CR Text, LoraLoaderModelOnly, ShowText|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3-VBVR逻辑优化-图生视频-AIGC大赏_2042489551154847745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042489551154847745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `CFGGuider`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CM_IntToFloat`
- `SetNode`
- `LTXVImgToVideoInplace`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `GetNode`
- `LTXVPreprocess`
- `LTXVChunkFeedForward`
- `INTConstant`
- `ResizeImagesByLongerEdge`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `DualCLIPLoader`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `SimpleCalculatorKJ`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `INTConstant`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `CFGGuider`
- `RandomNoise`
- `CR Text`
- `CLIPTextEncode` ★核心
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TT_img_enc_v2`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（53/58）

**有卡**：`CFGGuider`、`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVScheduler`、`CM_IntToFloat`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVPreprocess`、`LTXVChunkFeedForward`、`INTConstant`、`ResizeImagesByLongerEdge`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`DualCLIPLoader`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`SimpleCalculatorKJ`、`EmptyLTXVLatentVideo`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`CLIPTextEncode`、`UNETLoader`、`SaveImage`、`LoadImage`、`CR Text`、`LoraLoaderModelOnly`、`TT_img_enc_v2`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
