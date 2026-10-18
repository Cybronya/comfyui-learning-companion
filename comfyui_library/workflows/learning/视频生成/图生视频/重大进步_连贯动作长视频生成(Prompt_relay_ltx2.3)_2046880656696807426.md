---
key: 视频生成/图生视频/重大进步_连贯动作长视频生成(Prompt_relay_ltx2.3)_2046880656696807426.json
name: 重大进步_连贯动作长视频生成(Prompt_relay_ltx2.3)_2046880656696807426.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/重大进步_连贯动作长视频生成(Prompt_relay_ltx2.3)_2046880656696807426.json
hash: 588ff464bacce4b0
coverage: 0.688889
learned_at: 2026-10-15 22:37:02
nodes: [KSamplerSelect, SetNode, GetNode, VisualizeSigmasKJ, ConditioningZeroOut, VAEDecode, BasicScheduler, PathchSageAttentionKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, PreviewImage, SetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, VHS_VideoCombine, VAELoaderKJ, LTXVPreprocess, VAELoaderKJ, DualCLIPLoader, LTX2SamplingPreviewOverride, LTXVImgToVideoInplaceKJ, UNETLoader, SamplerCustom, LTXVConditioning, PrimitiveString, StringReplace, RH_Translator, RH_Translator, PromptRelayEncode, PrimitiveInt, LoadImage, RH_LLMAPI_NODE, PrimitiveStringMultiline, RH_Translator, PreviewAny, PreviewAny, RH_Translator, StringReplace, PrimitiveStringMultiline, StringReplace, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 241}
---

# 视频生成/图生视频/重大进步_连贯动作长视频生成(Prompt_relay_ltx2.3)_2046880656696807426.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046880656696807426.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `VisualizeSigmasKJ`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `BasicScheduler`
- `PathchSageAttentionKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `VHS_VideoCombine`
- `VAELoaderKJ`
- `LTXVPreprocess`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTX2SamplingPreviewOverride`
- `LTXVImgToVideoInplaceKJ`
- `UNETLoader` ★核心
- `SamplerCustom` ★核心
- `LTXVConditioning`
- `PrimitiveString`
- `StringReplace`
- `RH_Translator`
- `RH_Translator`
- `PromptRelayEncode`
- `PrimitiveInt`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `PrimitiveStringMultiline`
- `RH_Translator`
- `PreviewAny`
- `PreviewAny`
- `RH_Translator`
- `StringReplace`
- `PrimitiveStringMultiline`
- `StringReplace`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `241`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（31/45）

**有卡**：`KSamplerSelect`、`VisualizeSigmasKJ`、`ConditioningZeroOut`、`VAEDecode`、`BasicScheduler`、`PathchSageAttentionKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`VAELoaderKJ`、`LTXVPreprocess`、`DualCLIPLoader`、`LTX2SamplingPreviewOverride`、`LTXVImgToVideoInplaceKJ`、`UNETLoader`、`SamplerCustom`、`LTXVConditioning`、`StringReplace`、`RH_Translator`、`PromptRelayEncode`、`LoadImage`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent
