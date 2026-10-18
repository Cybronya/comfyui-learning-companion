---
key: 视频生成/图生视频/LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2080253203614097410.json
name: LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2080253203614097410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2080253203614097410.json
hash: cbaa9928bed620a5
coverage: 0.944444
learned_at: 2026-10-15 22:42:11
nodes: [CLIPTextEncode, ShowText|pysssss, CLIPTextEncode, LTXVConditioning, LTXVChunkFeedForward, ModelPatchTorchSettings, PathchSageAttentionKJ, CFGGuider, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, ResizeImagesByLongerEdge, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVImgToVideoInplace, llama_cpp_instruct_adv, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecodeTiled, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, CR Text, KSamplerSelect, RandomNoise, ImageScale, llama_cpp_model_loader, PrimitiveInt, VHS_VideoCombine, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2080253203614097410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080253203614097410.json`

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
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `llama_cpp_instruct_adv`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `CR Text`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ImageScale`
- `llama_cpp_model_loader`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`CLIPTextEncode`、`LTXVConditioning`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CFGGuider`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`ResizeImagesByLongerEdge`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`llama_cpp_instruct_adv`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`CR Text`、`KSamplerSelect`、`RandomNoise`、`ImageScale`、`llama_cpp_model_loader`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
