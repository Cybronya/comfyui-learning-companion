---
key: 视频生成/图生视频/Ltx2.3 Prompt Relay Smart｜VBVR 390K单图精准控制｜参考生视频稳_2104801534893711362.json
name: Ltx2.3 Prompt Relay Smart｜VBVR 390K单图精准控制｜参考生视频稳_2104801534893711362
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3 Prompt Relay Smart｜VBVR 390K单图精准控制｜参考生视频稳_2104801534893711362.json
hash: 115c508027214336
coverage: 0.858974
learned_at: 2026-10-17 02:43:50
nodes: [LTXVAudioVAEDecode, GetNode, SetNode, VisualizeSigmasKJ, LTX2SamplingPreviewOverride, PreviewImage, LTXVSeparateAVLatent, VAEDecode, VHS_VideoCombine, GetNode, SamplerCustom, LTXVConditioning, KSamplerSelect, ConditioningZeroOut, PathchSageAttentionKJ, BasicScheduler, LTXVConcatAVLatent, GetNode, GetNode, VAELoaderKJ, VAELoaderKJ, UNETLoader, DualCLIPLoader, LTXVImgToVideoInplaceKJ, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoraLoaderModelOnly, PromptRelaySmartEncode, LoadImage, CR Prompt Text, JWInteger, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Ltx2.3 Prompt Relay Smart｜VBVR 390K单图精准控制｜参考生视频稳_2104801534893711362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Ltx2.3 Prompt Relay Smart｜VBVR 390K单图精准控制｜参考生视频稳_2104801534893711362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `VisualizeSigmasKJ`
- `LTX2SamplingPreviewOverride`
- `PreviewImage`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `SamplerCustom` ★核心
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LTXVImgToVideoInplaceKJ`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PromptRelaySmartEncode`
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
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

**有卡**：`LTXVAudioVAEDecode`、`VisualizeSigmasKJ`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`VHS_VideoCombine`、`SamplerCustom`、`LTXVConditioning`、`KSamplerSelect`、`ConditioningZeroOut`、`PathchSageAttentionKJ`、`BasicScheduler`、`LTXVConcatAVLatent`、`VAELoaderKJ`、`UNETLoader`、`DualCLIPLoader`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`PromptRelaySmartEncode`、`LoadImage`、`CR Prompt Text`、`JWInteger`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
