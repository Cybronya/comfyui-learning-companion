---
key: 视频生成/文生视频/ltx2.3参考声纹+ 文生视频（声音参考文生视频）_2047943915977842690.json
name: ltx2.3参考声纹+ 文生视频（声音参考文生视频）_2047943915977842690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3参考声纹+ 文生视频（声音参考文生视频）_2047943915977842690.json
hash: 6a3bb5b8426dad36
coverage: 0.519481
learned_at: 2026-10-11 19:49:44
nodes: [MarkdownNote, Bjornulf_ShowInt, PainterAudioLength, FishS2VoiceCloneTTS, CM_FloatToInt, PlaySound|pysssss, Load Whisper (mtb), Audio To Text (mtb), ShowText|pysssss, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, GetNode, RandomNoise, LTXVCropGuides, LatentUpscaleModelLoader, PrimitiveFloat, INTConstant, SimpleMath+, Reroute, LoadAudio, LTXVSeparateAVLatent, VAEDecodeTiled, MarkdownNote, Reroute, LayerUtility: PurgeVRAM, easy mathInt, easy mathInt, GetNode, GetNode, SetNode, SetNode, SetNode, MarkdownNote, CR Text, TTResolutionSelector, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, PreviewAudio, PreviewAny, LTXAVTextEncoderLoader, GetNode, CombinationText, TextGenerateLTX2Prompt, GetNode, SetNode, RH_Translator, Reroute, PreviewAny, DualCLIPLoader, SetNode, CheckpointLoaderSimple, LTXVAudioVAELoader, SetNode, EmptyLTXVLatentVideo, GetNode, CFGGuider, SamplerCustomAdvanced, KSamplerSelect, LTXVSeparateAVLatent, GetNode, GetNode, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, KSampler, LTXVConditioning, CR Prompt Text, JjkText, LTXVScheduler, RHHiddenNodes, VHS_VideoCombine]
patterns: []
missing: [Audio To Text (mtb), CR Text, LayerUtility: PurgeVRAM, Load Whisper (mtb), PlaySound|pysssss, SimpleMath+, easy mathInt, easy mathInt, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 216654308440775, "steps": 4}
discoveries: [次要节点 `Audio To Text (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `Load Whisper (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/ltx2.3参考声纹+ 文生视频（声音参考文生视频）_2047943915977842690.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3参考声纹+ 文生视频（声音参考文生视频）_2047943915977842690.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Other

**节点**（77 个）：
- `MarkdownNote`
- `Bjornulf_ShowInt`
- `PainterAudioLength`
- `FishS2VoiceCloneTTS`
- `CM_FloatToInt`
- `PlaySound|pysssss`
- `Load Whisper (mtb)`
- `Audio To Text (mtb)`
- `ShowText|pysssss`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `RandomNoise`
- `LTXVCropGuides`
- `LatentUpscaleModelLoader`
- `PrimitiveFloat`
- `INTConstant`
- `SimpleMath+`
- `Reroute`
- `LoadAudio`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `easy mathInt`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `CR Text`
- `TTResolutionSelector`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `PreviewAudio`
- `PreviewAny`
- `LTXAVTextEncoderLoader`
- `GetNode`
- `CombinationText`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `SetNode`
- `RH_Translator`
- `Reroute`
- `PreviewAny`
- `DualCLIPLoader`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LTXVConditioning`
- `CR Prompt Text`
- `JjkText`
- `LTXVScheduler`
- `RHHiddenNodes`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `216654308440775`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **52%**（40/77）

**有卡**：`Bjornulf_ShowInt`、`PainterAudioLength`、`FishS2VoiceCloneTTS`、`CM_FloatToInt`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`RandomNoise`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`INTConstant`、`LoadAudio`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`TTResolutionSelector`、`LoadImage`、`PreviewAudio`、`LTXAVTextEncoderLoader`、`CombinationText`、`TextGenerateLTX2Prompt`、`RH_Translator`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`EmptyLTXVLatentVideo`、`CFGGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`KSampler`、`LTXVConditioning`、`LTXVScheduler`、`RHHiddenNodes`、`VHS_VideoCombine`

**缺卡**（9）：`Audio To Text (mtb)`、`CR Text`、`LayerUtility: PurgeVRAM`、`Load Whisper (mtb)`、`PlaySound|pysssss`、`SimpleMath+`、`easy mathInt`、`easy mathInt`、`CR Prompt Text`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `Audio To Text (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `Load Whisper (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
