---
key: 视频生成/图生视频/超牛叉 ltx2.3 电商带货 自定义 人物 产品 背景 动作 话术  去字幕版_2073463647009259520.json
name: 超牛叉 ltx2.3 电商带货 自定义 人物 产品 背景 动作 话术  去字幕版_2073463647009259520.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/超牛叉 ltx2.3 电商带货 自定义 人物 产品 背景 动作 话术  去字幕版_2073463647009259520.json
hash: f4e1cb2608fb1cea
coverage: 0.811321
learned_at: 2026-10-15 22:41:07
nodes: [CreateVideo, LoadImage, LoadImage, 孤海注释, 孤海注释, 孤海注释, 孤海注释, String, PrimitiveBoolean, RHLLMChatNode, LTXVAudioVAELoader, LTXVConditioning, KSamplerSelect, SamplerCustom, LTX2SamplingPreviewOverride, CheckpointLoaderSimple, LTXFloatToInt, LTXVEmptyLatentAudio, VisualizeSigmasKJ, LTXVConcatAVLatent, LTXAddVideoICLoRAGuide, BasicScheduler, LTXVCropGuides, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LTXVAudioVAEDecode, LTX2_NAG, LoraLoaderModelOnly, 孤海注释, 孤海注释, 孤海注释, 孤海注释, CLIPTextEncode, LTXAVTextEncoderLoader, SaveVideo, LTXVPreprocess, LTXVImgToVideoConditionOnly, CLIPTextEncode, PrimitiveFloat, EmptyLTXVLatentVideo, RHHiddenNodes, PrimitiveInt, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, PixaromaShowText, LoadImage, RH_RhartImageG2ImageToImage, Preview from image [Crystools], CR Text, LoraLoaderModelOnly, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/超牛叉 ltx2.3 电商带货 自定义 人物 产品 背景 动作 话术  去字幕版_2073463647009259520.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073463647009259520.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `CreateVideo`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `String`
- `PrimitiveBoolean`
- `RHLLMChatNode`
- `LTXVAudioVAELoader`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `LTX2SamplingPreviewOverride`
- `CheckpointLoaderSimple` ★核心
- `LTXFloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `VisualizeSigmasKJ`
- `LTXVConcatAVLatent`
- `LTXAddVideoICLoRAGuide`
- `BasicScheduler`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `SaveVideo`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `EmptyLTXVLatentVideo`
- `RHHiddenNodes`
- `PrimitiveInt`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `PixaromaShowText`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `Preview from image [Crystools]`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（43/53）

**有卡**：`CreateVideo`、`LoadImage`、`String`、`PrimitiveBoolean`、`RHLLMChatNode`、`LTXVAudioVAELoader`、`LTXVConditioning`、`KSamplerSelect`、`SamplerCustom`、`LTX2SamplingPreviewOverride`、`CheckpointLoaderSimple`、`LTXFloatToInt`、`LTXVEmptyLatentAudio`、`VisualizeSigmasKJ`、`LTXVConcatAVLatent`、`LTXAddVideoICLoRAGuide`、`BasicScheduler`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVTiledVAEDecode`、`LTXVAudioVAEDecode`、`LTX2_NAG`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`SaveVideo`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`RHHiddenNodes`、`LTXICLoRALoaderModelOnly`、`PixaromaShowText`、`RH_RhartImageG2ImageToImage`、`Preview from image [Crystools]`、`CR Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent
