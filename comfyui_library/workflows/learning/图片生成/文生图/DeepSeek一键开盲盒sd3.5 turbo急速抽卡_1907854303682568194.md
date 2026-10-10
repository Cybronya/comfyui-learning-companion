---
key: DeepSeek一键开盲盒sd3.5 turbo急速抽卡_1907854303682568194.json
name: DeepSeek一键开盲盒sd3.5 turbo急速抽卡_1907854303682568194
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/DeepSeek一键开盲盒sd3.5 turbo急速抽卡_1907854303682568194.json
hash: 6b74168654bd43b7
coverage: 0.888889
learned_at: 2026-10-10 21:27:12
nodes: [JoinStrings, JjkText, TripleCLIPLoader, Fast Groups Bypasser (rgthree), FluxResolutionNode, FluxResolutionNode, EmptyLatentImage, EmptyLatentImage, KSampler, SaveImage, EmptyLatentImage, EmptyLatentImage, KSampler, VAEDecode, VAEDecode, VAEDecode, SaveImage, SaveImage, KSampler, FluxResolutionNode, VAEDecode, EmptyLatentImage, CLIPTextEncode, CLIPTextEncodeFlux, ModelSamplingSD3, CheckpointLoaderSimple, VAEDecode, FluxResolutionNode, SaveImage, SaveImage, KSampler, KSampler, ShowText|pysssss, LayerUtility: DeepSeekAPIV2, FluxResolutionNode, OneButtonPrompt]
patterns: [text_to_image]
missing: [LayerUtility: DeepSeekAPIV2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "sd3.5_large_turbo.safetensors", "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 220839500466962, "steps": 4, "width": 1024}
discoveries: [次要节点 `LayerUtility: DeepSeekAPIV2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# DeepSeek一键开盲盒sd3.5 turbo急速抽卡_1907854303682568194.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/DeepSeek一键开盲盒sd3.5 turbo急速抽卡_1907854303682568194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（36 个）：
- `JoinStrings`
- `JjkText`
- `TripleCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxResolutionNode`
- `FluxResolutionNode`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `FluxResolutionNode`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `ModelSamplingSD3`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `FluxResolutionNode`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `ShowText|pysssss`
- `LayerUtility: DeepSeekAPIV2`
- `FluxResolutionNode`
- `OneButtonPrompt`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `220839500466962`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `sd3.5_large_turbo.safetensors`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`JoinStrings`、`TripleCLIPLoader`、`FluxResolutionNode`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`CLIPTextEncodeFlux`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`OneButtonPrompt`

**缺卡**（1）：`LayerUtility: DeepSeekAPIV2`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、CLIPTextEncodeFlux、FluxResolutionNode、TripleCLIPLoader

## 参数体检

发现 5 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: DeepSeekAPIV2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
