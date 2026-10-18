---
key: 视频生成/图生视频/（高帧率）Ltx2.3 Licon-MSR自动提示词版全能参考生视频正式版V1_2063464652104884226.json
name: （高帧率）Ltx2.3 Licon-MSR自动提示词版全能参考生视频正式版V1_2063464652104884226.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（高帧率）Ltx2.3 Licon-MSR自动提示词版全能参考生视频正式版V1_2063464652104884226.json
hash: cdc46d50659b6838
coverage: 0.971429
learned_at: 2026-10-15 22:39:13
nodes: [LoadImage, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXAddVideoICLoRAGuide, CFGGuider, LowVRAMCheckpointLoader, LTXAVTextEncoderLoader, LiconMSR, CreateVideo, INTConstant, INTConstant, INTConstant, LTXVCropGuides, VAEDecode, CLIPTextEncode, LTXVAudioVAELoader, LTXVConditioning, EmptyLTXVLatentVideo, RandomNoise, KSamplerSelect, LTXVEmptyLatentAudio, SaveVideo, ShowText|pysssss, LoadImage, CLIPTextEncode, RH_LLMAPI_Pro_Node, LoadImage, LoadImage, LoadImage, CR Prompt Text, CR Prompt Text, LTXICLoRALoaderModelOnly, ManualSigmas, SamplerCustomAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
---

# 视频生成/图生视频/（高帧率）Ltx2.3 Licon-MSR自动提示词版全能参考生视频正式版V1_2063464652104884226.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063464652104884226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（35 个）：
- `LoadImage`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXAddVideoICLoRAGuide`
- `CFGGuider`
- `LowVRAMCheckpointLoader` ★核心
- `LTXAVTextEncoderLoader`
- `LiconMSR`
- `CreateVideo`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAELoader`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SaveVideo`
- `ShowText|pysssss`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `LTXICLoRALoaderModelOnly` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`LoadImage`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXAddVideoICLoRAGuide`、`CFGGuider`、`LowVRAMCheckpointLoader`、`LTXAVTextEncoderLoader`、`LiconMSR`、`CreateVideo`、`INTConstant`、`LTXVCropGuides`、`VAEDecode`、`CLIPTextEncode`、`LTXVAudioVAELoader`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`RandomNoise`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`SaveVideo`、`RH_LLMAPI_Pro_Node`、`CR Prompt Text`、`LTXICLoRALoaderModelOnly`、`ManualSigmas`、`SamplerCustomAdvanced`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
