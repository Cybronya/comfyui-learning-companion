---
key: 数字人/数字人/AI短剧人物开口说话V1.1｜8秒有声测试版先睹为快_2112399633505939458.json
name: AI短剧人物开口说话V1.1｜8秒有声测试版先睹为快_2112399633505939458
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI短剧人物开口说话V1.1｜8秒有声测试版先睹为快_2112399633505939458.json
hash: 60e31c6a56fffb8f
coverage: 0.888889
learned_at: 2026-10-26 01:53:45
nodes: [PrimitiveStringMultiline, ResolutionSelector, CLIPLoader, VAELoader, VAELoader, BasicGuider, RandomNoise, SamplerCustomAdvanced, PrimitiveFloat, ComfyMathExpression, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AVDecodeT8, MiniMaxH3MultiRateSamplerEXPT8, CLIPLoader, VAELoader, VAELoader, BasicGuider, RandomNoise, ComfyMathExpression, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AVDecodeT8, CLIPLoader, VAELoader, VAELoader, BasicGuider, RandomNoise, SamplerCustomAdvanced, UniBlockSwap, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MultiRateSamplerEXPT8, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, ComfyMathExpression, PrimitiveStringMultiline, VHS_VideoCombine, LoadAudio, ResolutionSelector, PrimitiveFloat, MiniMaxH3AudioConditioningT8, MiniMaxH3AudioConditioningT8, UNETLoader, UNETLoader, LoraLoaderModelOnly, UniBlockSwap, Fast Groups Bypasser (rgthree), UniBlockSwap, UNETLoader, SamplerCustomAdvanced, VHS_VideoCombine, MiniMaxH3AudioConditioningT8, PrimitiveFloat, MiniMaxH3MultiRateSamplerEXPT8, ResolutionSelector, PrimitiveStringMultiline, LoadImage, LoraLoaderModelOnly, StringFormat, YuanCustomCombo, YuanCustomCombo, YuanCustomCombo, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/AI短剧人物开口说话V1.1｜8秒有声测试版先睹为快_2112399633505939458.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI短剧人物开口说话V1.1｜8秒有声测试版先睹为快_2112399633505939458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（108 个）：
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveFloat`
- `ComfyMathExpression`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `ComfyMathExpression`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3AVDecodeT8`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `UniBlockSwap`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `LoadAudio`
- `ResolutionSelector`
- `PrimitiveFloat`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AudioConditioningT8`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UniBlockSwap`
- `Fast Groups Bypasser (rgthree)`
- `UniBlockSwap`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `StringFormat`
- `YuanCustomCombo`
- `YuanCustomCombo`
- `YuanCustomCombo`
- `PrimitiveStringMultiline`
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

覆盖率 **89%**（96/108）

**有卡**：`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3MultiRateSamplerEXPT8`、`UniBlockSwap`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LoadImage`、`LoadAudio`、`MiniMaxH3AudioConditioningT8`、`UNETLoader`、`StringFormat`、`YuanCustomCombo`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
