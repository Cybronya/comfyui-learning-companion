---
key: 视频生成/图生视频/Ltx2.3 MSR全能参考生视频V1_2067141677512482818.json
name: Ltx2.3 MSR全能参考生视频V1_2067141677512482818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3 MSR全能参考生视频V1_2067141677512482818.json
hash: 6b4fbe7d8d869461
coverage: 0.90566
learned_at: 2026-10-15 22:39:57
nodes: [LTXAVTextEncoderLoader, LTXVSeparateAVLatent, LTXVCropGuides, LTXVAudioVAEDecode, VAEDecode, LTXVAudioVAELoader, KSamplerSelect, ShowText|pysssss, SamplerCustomAdvanced, CFGGuider, LTXVConcatAVLatent, ManualSigmas, Fast Groups Bypasser (rgthree), EmptyLTXVLatentVideo, LTXAddVideoICLoRAGuide, LoadImage, LoadImage, SaveVideo, Qwen3VL_Chat, SaveVideo, LoadImage, CreateVideo, SaveVideo, LoadImage, LoadImage, CR Prompt Text, RH_LLMAPI_Pro_Node, CR Prompt Text, ShowText|pysssss, Fast Groups Bypasser (rgthree), Note, CLIPTextEncode, CLIPTextEncode, RandomNoise, LTXVEmptyLatentAudio, INTConstant, INTConstant, INTConstant, LiconMSR, LTXVConditioning, LowVRAMCheckpointLoader, LTXICLoRALoaderModelOnly, LoadImage, LoadImage, LoadImage, SaveVideo, LoadImage, LoadImage, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 40, "width": 241}
---

# 视频生成/图生视频/Ltx2.3 MSR全能参考生视频V1_2067141677512482818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067141677512482818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（53 个）：
- `LTXAVTextEncoderLoader`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LTXVAudioVAELoader`
- `KSamplerSelect` ★核心
- `ShowText|pysssss`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLTXVLatentVideo`
- `LTXAddVideoICLoRAGuide`
- `LoadImage`
- `LoadImage`
- `SaveVideo`
- `Qwen3VL_Chat`
- `SaveVideo`
- `LoadImage`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVEmptyLatentAudio` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LiconMSR`
- `LTXVConditioning`
- `LowVRAMCheckpointLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `241`
- `height` = `40`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **91%**（48/53）

**有卡**：`LTXAVTextEncoderLoader`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVAudioVAELoader`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVConcatAVLatent`、`ManualSigmas`、`EmptyLTXVLatentVideo`、`LTXAddVideoICLoRAGuide`、`LoadImage`、`SaveVideo`、`Qwen3VL_Chat`、`CreateVideo`、`CR Prompt Text`、`RH_LLMAPI_Pro_Node`、`CLIPTextEncode`、`RandomNoise`、`LTXVEmptyLatentAudio`、`INTConstant`、`LiconMSR`、`LTXVConditioning`、`LowVRAMCheckpointLoader`、`LTXICLoRALoaderModelOnly`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
