---
key: 数字人/数字人/LTX2.3-图生视频工业版_2030090763832401922.json
name: LTX2.3-图生视频工业版_2030090763832401922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3-图生视频工业版_2030090763832401922.json
hash: 2090ddac638e818a
coverage: 0.944444
learned_at: 2026-10-26 01:55:54
nodes: [CLIPTextEncode, CLIPTextEncode, LTXVConditioning, CFGGuider, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, ResizeImagesByLongerEdge, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVImgToVideoInplace, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecodeTiled, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, KSamplerSelect, RandomNoise, ImageScale, llama_cpp_model_loader, LoadImage, PrimitiveInt, UNETLoader, LTXVChunkFeedForward, ModelPatchTorchSettings, PathchSageAttentionKJ, CR Text, CR Text, llama_cpp_instruct_adv, ShowText|pysssss, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 数字人/数字人/LTX2.3-图生视频工业版_2030090763832401922.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3-图生视频工业版_2030090763832401922.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `ResizeImagesByLongerEdge`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ImageScale`
- `llama_cpp_model_loader`
- `LoadImage`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CR Text`
- `CR Text`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`CLIPTextEncode`、`LTXVConditioning`、`CFGGuider`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`ResizeImagesByLongerEdge`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`VAELoaderKJ`、`DualCLIPLoader`、`KSamplerSelect`、`RandomNoise`、`ImageScale`、`llama_cpp_model_loader`、`LoadImage`、`UNETLoader`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CR Text`、`llama_cpp_instruct_adv`、`VHS_VideoCombine`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
