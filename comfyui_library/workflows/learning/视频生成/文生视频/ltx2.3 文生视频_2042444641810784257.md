---
key: 视频生成/文生视频/ltx2.3 文生视频_2042444641810784257.json
name: ltx2.3 文生视频_2042444641810784257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3 文生视频_2042444641810784257.json
hash: b20ed5d563b2453e
coverage: 0.809524
learned_at: 2026-10-11 19:49:44
nodes: [LTXVScheduler, LTXVConditioning, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, KSamplerSelect, KSampler, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, DualCLIPLoader, PrimitiveFloat, MarkdownNote, CLIPTextEncode, RandomNoise, CLIPTextEncode, LTXVLatentUpsampler, LoraLoaderModelOnly, Reroute, CreateVideo, easy mathInt, easy mathInt, SaveVideo, LTXVCropGuides, CombinationText, PrimitiveInt, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, JjkText, CheckpointLoaderSimple, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, Int, MathExpression_UTK, Int, TextGenerateLTX2Prompt, JjkText, Int]
patterns: []
missing: [easy mathInt, easy mathInt]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 628611078184540, "steps": 4, "width": 97}
discoveries: [次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/ltx2.3 文生视频_2042444641810784257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3 文生视频_2042444641810784257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（42 个）：
- `LTXVScheduler`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `KSampler` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `DualCLIPLoader`
- `PrimitiveFloat`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `CreateVideo`
- `easy mathInt`
- `easy mathInt`
- `SaveVideo`
- `LTXVCropGuides`
- `CombinationText`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `JjkText`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `Int`
- `MathExpression_UTK`
- `Int`
- `TextGenerateLTX2Prompt`
- `JjkText`
- `Int`

## 关键参数

- `seed` = `628611078184540`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`LTXVScheduler`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CFGGuider`、`KSamplerSelect`、`KSampler`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LTXVConcatAVLatent`、`DualCLIPLoader`、`CLIPTextEncode`、`RandomNoise`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`CreateVideo`、`SaveVideo`、`LTXVCropGuides`、`CombinationText`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`Int`、`MathExpression_UTK`、`TextGenerateLTX2Prompt`

**缺卡**（2）：`easy mathInt`、`easy mathInt`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
