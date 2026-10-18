---
key: 视频生成/图生视频/Ltx2.3多镜头长时间KJ版｜时间分段剪辑加逻辑控制PromptRe｜图生视频_2099155859929649154.json
name: Ltx2.3多镜头长时间KJ版｜时间分段剪辑加逻辑控制PromptRe｜图生视频_2099155859929649154
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3多镜头长时间KJ版｜时间分段剪辑加逻辑控制PromptRe｜图生视频_2099155859929649154.json
hash: c8b7da2228646927
coverage: 0.858974
learned_at: 2026-10-17 01:44:30
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, LTXVConcatAVLatent, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, SetNode, PreviewImage, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, PromptRelayEncode, UNETLoader, PathchSageAttentionKJ, LTXVConditioning, SamplerCustom, LoraLoaderModelOnly, GetNode, VisualizeSigmasKJ, LTXVEmptyLatentAudio, GetNode, BasicScheduler, GetNode, LTXVImgToVideoInplaceKJ, ConditioningZeroOut, LTXVPreprocess, VHS_VideoCombine, JWInteger, LoadImage, CR Prompt Text, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Ltx2.3多镜头长时间KJ版｜时间分段剪辑加逻辑控制PromptRe｜图生视频_2099155859929649154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Ltx2.3多镜头长时间KJ版｜时间分段剪辑加逻辑控制PromptRe｜图生视频_2099155859929649154.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `PreviewImage`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PromptRelayEncode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `ConditioningZeroOut`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `JWInteger`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（67/78）

**有卡**：`LTXVAudioVAEDecode`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConcatAVLatent`、`KSamplerSelect`、`VAELoaderKJ`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`PromptRelayEncode`、`UNETLoader`、`PathchSageAttentionKJ`、`LTXVConditioning`、`SamplerCustom`、`LoraLoaderModelOnly`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`BasicScheduler`、`LTXVImgToVideoInplaceKJ`、`ConditioningZeroOut`、`LTXVPreprocess`、`VHS_VideoCombine`、`JWInteger`、`LoadImage`、`CR Prompt Text`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
