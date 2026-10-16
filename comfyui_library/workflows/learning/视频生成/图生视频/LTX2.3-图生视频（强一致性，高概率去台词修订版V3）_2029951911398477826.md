---
key: 视频生成/图生视频/LTX2.3-图生视频（强一致性，高概率去台词修订版V3）_2029951911398477826.json
name: LTX2.3-图生视频（强一致性，高概率去台词修订版V3）_2029951911398477826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2029951911398477826.json
hash: 5b7e3b518932ca47
coverage: 0.944444
learned_at: 2026-10-15 22:35:24
nodes: [CLIPTextEncode, ShowText|pysssss, CLIPTextEncode, LTXVConditioning, LTXVChunkFeedForward, ModelPatchTorchSettings, PathchSageAttentionKJ, CFGGuider, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, ResizeImagesByLongerEdge, PrimitiveInt, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVImgToVideoInplace, llama_cpp_instruct_adv, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecodeTiled, llama_cpp_model_loader, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, CR Text, CR Text, KSamplerSelect, RandomNoise, ImageScale, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3-图生视频（强一致性，高概率去台词修订版V3）_2029951911398477826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029951911398477826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `ResizeImagesByLongerEdge`
- `PrimitiveInt`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `llama_cpp_instruct_adv`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `CR Text`
- `CR Text`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ImageScale`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`CLIPTextEncode`、`LTXVConditioning`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CFGGuider`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`ResizeImagesByLongerEdge`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`llama_cpp_instruct_adv`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`llama_cpp_model_loader`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`CR Text`、`KSamplerSelect`、`RandomNoise`、`ImageScale`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
