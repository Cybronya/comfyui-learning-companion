---
key: 视频生成/文生视频/ltx-2.3图生视频单阶段蒸馏生产最优_2030352240698986497.json
name: ltx-2.3图生视频单阶段蒸馏生产最优_2030352240698986497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx-2.3图生视频单阶段蒸馏生产最优_2030352240698986497.json
hash: 1c0f8a231c75e79b
coverage: 0.933333
learned_at: 2026-10-15 22:47:22
nodes: [LTXVAudioVAEDecode, VAEDecodeTiled, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, LTXVConditioning, LTXVConcatAVLatent, LTXVPreprocess, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, CM_FloatToInt, KSamplerSelect, CFGGuider, RandomNoise, LoraLoaderModelOnly, VAELoaderKJ, DualCLIPLoader, PrimitiveFloat, PrimitiveBoolean, CLIPTextEncode, PrimitiveInt, EmptyLTXVLatentVideo, CLIPTextEncode, UnetLoaderGGUF, LoraLoaderModelOnly, VHS_VideoCombine, LoadImage, ResizeImageMaskNode, UNETLoader, VAELoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx-2.3图生视频单阶段蒸馏生产最优_2030352240698986497.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx-2.3图生视频单阶段蒸馏生产最优_2030352240698986497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（30 个）：
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CM_FloatToInt`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `ResizeImageMaskNode`
- `UNETLoader` ★核心
- `VAELoader`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CM_FloatToInt`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`DualCLIPLoader`、`PrimitiveBoolean`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`UnetLoaderGGUF`、`VHS_VideoCombine`、`LoadImage`、`ResizeImageMaskNode`、`UNETLoader`、`VAELoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
