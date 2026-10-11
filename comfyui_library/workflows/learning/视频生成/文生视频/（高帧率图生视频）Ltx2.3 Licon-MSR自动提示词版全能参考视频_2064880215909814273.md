---
key: 视频生成/文生视频/（高帧率图生视频）Ltx2.3 Licon-MSR自动提示词版全能参考视频_2064880215909814273.json
name: （高帧率图生视频）Ltx2.3 Licon-MSR自动提示词版全能参考视频_2064880215909814273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（高帧率图生视频）Ltx2.3 Licon-MSR自动提示词版全能参考视频_2064880215909814273.json
hash: 64ac96ead04027aa
coverage: 0.916667
learned_at: 2026-10-11 20:21:36
nodes: [LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXAddVideoICLoRAGuide, CFGGuider, LowVRAMCheckpointLoader, LTXAVTextEncoderLoader, LiconMSR, INTConstant, INTConstant, INTConstant, LTXVCropGuides, CLIPTextEncode, LTXVAudioVAELoader, LTXVConditioning, EmptyLTXVLatentVideo, RandomNoise, KSamplerSelect, LTXVEmptyLatentAudio, SaveVideo, ShowText|pysssss, LoadImage, CLIPTextEncode, RH_LLMAPI_Pro_Node, LoadImage, LoadImage, LoadImage, CR Prompt Text, CR Prompt Text, LTXICLoRALoaderModelOnly, ManualSigmas, SamplerCustomAdvanced, TT_img_enc, SaveImage, VAEDecode, CreateVideo, LTXVAudioVAEDecode]
patterns: []
missing: [CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（高帧率图生视频）Ltx2.3 Licon-MSR自动提示词版全能参考视频_2064880215909814273.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（高帧率图生视频）Ltx2.3 Licon-MSR自动提示词版全能参考视频_2064880215909814273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（36 个）：
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXAddVideoICLoRAGuide`
- `CFGGuider`
- `LowVRAMCheckpointLoader` ★核心
- `LTXAVTextEncoderLoader`
- `LiconMSR`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LTXVCropGuides`
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
- `TT_img_enc`
- `SaveImage`
- `VAEDecode` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXAddVideoICLoRAGuide`、`CFGGuider`、`LowVRAMCheckpointLoader`、`LTXAVTextEncoderLoader`、`LiconMSR`、`INTConstant`、`LTXVCropGuides`、`CLIPTextEncode`、`LTXVAudioVAELoader`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`RandomNoise`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`SaveVideo`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`LTXICLoRALoaderModelOnly`、`ManualSigmas`、`SamplerCustomAdvanced`、`TT_img_enc`、`SaveImage`、`VAEDecode`、`CreateVideo`、`LTXVAudioVAEDecode`

**缺卡**（2）：`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
