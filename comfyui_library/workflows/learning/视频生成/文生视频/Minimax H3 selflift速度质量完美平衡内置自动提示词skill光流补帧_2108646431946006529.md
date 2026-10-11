---
key: 视频生成/文生视频/Minimax H3 selflift速度质量完美平衡内置自动提示词skill光流补帧_2108646431946006529.json
name: Minimax H3 selflift速度质量完美平衡内置自动提示词skill光流补帧_2108646431946006529
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3 selflift速度质量完美平衡内置自动提示词skill光流补帧_2108646431946006529.json
hash: 4fc83b3069d099ff
coverage: 0.548673
learned_at: 2026-10-11 22:12:44
nodes: [VAELoader, VAELoader, VAEDecode, VAEDecodeAudio, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, MiniMaxH3SigmaShift, ModelAttentionBackend, UNETLoader, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, SetNode, SetNode, SetNode, LoraLoaderModelOnly, SetNode, GetNode, GetNode, ConditioningZeroOut, KSamplerSelect, LTXVSeparateAVLatent, SetNode, GetNode, GetNode, SetNode, ModelPreviewOverrideKJ, LoraLoaderModelOnly, SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, VHS_LoadVideo, SetNode, LoadAudio, LoadAudio, LoadAudio, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, PrimitiveFloat, QwenH3PromptLocal, ResolutionSelector, ExtendIntermediateSigmas, BasicScheduler, LoadImage, LoadImage, SelfLiftH3Sampler, GetNode, GetNode, RIFE VFI, easy textSwitch, MiniMaxH3AudioConditioningT8, MuyeTextEditOutput, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: [RIFE VFI, easy textSwitch]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Minimax H3 selflift速度质量完美平衡内置自动提示词skill光流补帧_2108646431946006529.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3 selflift速度质量完美平衡内置自动提示词skill光流补帧_2108646431946006529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（113 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelPreviewOverrideKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `QwenH3PromptLocal`
- `ResolutionSelector`
- `ExtendIntermediateSigmas`
- `BasicScheduler`
- `LoadImage`
- `LoadImage`
- `SelfLiftH3Sampler` ★核心
- `GetNode`
- `GetNode`
- `RIFE VFI`
- `easy textSwitch`
- `MiniMaxH3AudioConditioningT8`
- `MuyeTextEditOutput`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（62/113）

**有卡**：`VAELoader`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`UNETLoader`、`CLIPLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`ModelPreviewOverrideKJ`、`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`ComfyMathExpression`、`QwenH3PromptLocal`、`ResolutionSelector`、`ExtendIntermediateSigmas`、`BasicScheduler`、`SelfLiftH3Sampler`、`MiniMaxH3AudioConditioningT8`、`MuyeTextEditOutput`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**缺卡**（2）：`RIFE VFI`、`easy textSwitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
