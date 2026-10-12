---
key: 视频生成/图生视频/LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818.json
name: LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818.json
hash: 69208460962f8b9a
coverage: 0.833333
learned_at: 2026-10-13 01:36:52
nodes: [CLIPTextEncode, ShowText|pysssss, CLIPTextEncode, LTXVConditioning, LTXVChunkFeedForward, ModelPatchTorchSettings, PathchSageAttentionKJ, CFGGuider, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, ResizeImagesByLongerEdge, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVImgToVideoInplace, llama_cpp_instruct_adv, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecodeTiled, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, CR Text, KSamplerSelect, RandomNoise, ImageScale, llama_cpp_model_loader, LoadImage, CR Text, PrimitiveInt, VHS_VideoCombine]
patterns: []
missing: [CR Text, CR Text, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "height": 24, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818.json`

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
- `LoadImage`
- `CR Text`
- `PrimitiveInt`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`CLIPTextEncode`、`LTXVConditioning`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CFGGuider`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`ResizeImagesByLongerEdge`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`llama_cpp_instruct_adv`、`VAEDecodeTiled`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`KSamplerSelect`、`RandomNoise`、`ImageScale`、`llama_cpp_model_loader`、`LoadImage`、`VHS_VideoCombine`

**缺卡**（4）：`CR Text`、`CR Text`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
