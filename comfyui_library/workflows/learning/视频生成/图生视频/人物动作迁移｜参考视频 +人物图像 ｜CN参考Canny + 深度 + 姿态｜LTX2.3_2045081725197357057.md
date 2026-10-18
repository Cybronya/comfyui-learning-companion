---
key: 视频生成/图生视频/人物动作迁移｜参考视频 +人物图像 ｜CN参考Canny + 深度 + 姿态｜LTX2.3_2045081725197357057.json
name: 人物动作迁移｜参考视频 +人物图像 ｜CN参考Canny + 深度 + 姿态｜LTX2.3_2045081725197357057.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物动作迁移｜参考视频 +人物图像 ｜CN参考Canny + 深度 + 姿态｜LTX2.3_2045081725197357057.json
hash: a1212cd2ec59427d
coverage: 0.666667
learned_at: 2026-10-15 22:36:45
nodes: [RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVLatentUpsampler, ManualSigmas, KSamplerSelect, CFGGuider, LTXVConcatAVLatent, RandomNoise, LTXVCropGuides, LTXVPreprocess, ResizeImageMaskNode, Note, Note, Note, Note, Note, CLIPTextEncode, DepthAnythingPreprocessor, LTXVEmptyLatentAudio, ResizeImageMaskNode, ResizeImageMaskNode, GetImageSize, SimpleMath+, easy showAnything, VHS_VideoInfo, LTXVImgToVideoInplace, CannyEdgePreprocessor, DWPreprocessor, Note, Note, easy showAnything, Note, Note, Note, Qwen3_VQA, Note, Note, Note, easy showAnything, Note, Note, Note, Note, Qwen3_VQA, Note, Note, ttN concat, CR Text, ImageLoader, CR Text, Note, easy cleanGpuUsed, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, VAEDecodeTiled, easy cleanGpuUsed, LTXVSeparateAVLatent, JoinStrings, easy cleanGpuUsed, SeedGenerator, SamplerCustomAdvanced, LTX2_NAG, ttN concat, Note, ShowText|pysssss, MemoryCleaner, JoinStrings, MemoryCleaner, ShowText|pysssss, LTXVConditioning, LatentUpscaleModelLoader, Note, easy cleanGpuUsed, Note, VHS_LoadVideo, VideoLoaderPlus, Note, Note, MultiplePathsInputPlus, Note, Note, Note, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, UNETLoader, easy cleanGpuUsed, LTXICLoRALoaderModelOnly, ModelPatchTorchSettings, LTXVChunkFeedForward, easy cleanGpuUsed, PathchSageAttentionKJ, LTXVImgToVideoConditionOnly, LTXAddVideoICLoRAGuide, VHS_VideoCombine, Note, MultiplePathsInputPlus, CLIPTextEncode, easy cleanGpuUsed, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/人物动作迁移｜参考视频 +人物图像 ｜CN参考Canny + 深度 + 姿态｜LTX2.3_2045081725197357057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045081725197357057.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（105 个）：
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `DepthAnythingPreprocessor`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `GetImageSize`
- `SimpleMath+`
- `easy showAnything`
- `VHS_VideoInfo`
- `LTXVImgToVideoInplace`
- `CannyEdgePreprocessor`
- `DWPreprocessor`
- `Note`
- `Note`
- `easy showAnything`
- `Note`
- `Note`
- `Note`
- `Qwen3_VQA`
- `Note`
- `Note`
- `Note`
- `easy showAnything`
- `Note`
- `Note`
- `Note`
- `Note`
- `Qwen3_VQA`
- `Note`
- `Note`
- `ttN concat`
- `CR Text`
- `ImageLoader`
- `CR Text`
- `Note`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `JoinStrings`
- `easy cleanGpuUsed`
- `SeedGenerator`
- `SamplerCustomAdvanced` ★核心
- `LTX2_NAG`
- `ttN concat`
- `Note`
- `ShowText|pysssss`
- `MemoryCleaner`
- `JoinStrings`
- `MemoryCleaner`
- `ShowText|pysssss`
- `LTXVConditioning`
- `LatentUpscaleModelLoader`
- `Note`
- `easy cleanGpuUsed`
- `Note`
- `VHS_LoadVideo`
- `VideoLoaderPlus`
- `Note`
- `Note`
- `MultiplePathsInputPlus`
- `Note`
- `Note`
- `Note`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `LTXICLoRALoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `easy cleanGpuUsed`
- `PathchSageAttentionKJ`
- `LTXVImgToVideoConditionOnly`
- `LTXAddVideoICLoRAGuide`
- `VHS_VideoCombine`
- `Note`
- `MultiplePathsInputPlus`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（70/105）

**有卡**：`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVPreprocess`、`ResizeImageMaskNode`、`CLIPTextEncode`、`DepthAnythingPreprocessor`、`LTXVEmptyLatentAudio`、`GetImageSize`、`SimpleMath+`、`VHS_VideoInfo`、`LTXVImgToVideoInplace`、`CannyEdgePreprocessor`、`DWPreprocessor`、`Qwen3_VQA`、`ttN concat`、`CR Text`、`ImageLoader`、`easy cleanGpuUsed`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`JoinStrings`、`SeedGenerator`、`LTX2_NAG`、`MemoryCleaner`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`VHS_LoadVideo`、`VideoLoaderPlus`、`MultiplePathsInputPlus`、`DualCLIPLoader`、`VAELoaderKJ`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LTXVImgToVideoConditionOnly`、`LTXAddVideoICLoRAGuide`、`VHS_VideoCombine`

**用到的条目**：CLIPTextEncode、UNETLoader、DepthAnythingPreprocessor、CannyEdgePreprocessor、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
