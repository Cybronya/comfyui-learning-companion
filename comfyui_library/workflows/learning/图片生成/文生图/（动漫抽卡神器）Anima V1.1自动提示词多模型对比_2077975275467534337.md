---
key: 图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词多模型对比_2077975275467534337.json
name: （动漫抽卡神器）Anima V1.1自动提示词多模型对比_2077975275467534337
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词多模型对比_2077975275467534337.json
hash: 50e04d35a7f36a92
coverage: 0.934783
learned_at: 2026-10-20 00:21:40
nodes: [UNETLoader, CLIPLoader, RHLLMChatNode, Random Line, easy showAnything, ConcatTextOfUtils, easy showAnything, CLIPTextEncode, VAEDecode, VAELoader, EmptyLatentImage, CLIPTextEncode, VAEDecode, CR Prompt Text, CR Prompt Text, ConditioningZeroOut, VAELoader, CLIPLoader, UNETLoader, KSampler, ConditioningKrea2Rebalance, easy showAnything, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, ImageConcatMulti, SaveImage, SaveImage, easy seed, easy seed, KSampler, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Prompt Text, CLIPTextEncode, ConcatTextOfUtils, AddLabel, AddLabel, AddLabel, SaveImage, SaveImage, CR Prompt Text, UNETLoader, RHLLMChatNode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1920, "sampler_name": "er_sde", "scheduler": "beta", "seed": 630893975497648, "steps": 40, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词多模型对比_2077975275467534337.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（动漫抽卡神器）Anima V1.1自动提示词多模型对比_2077975275467534337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `RHLLMChatNode`
- `Random Line`
- `easy showAnything`
- `ConcatTextOfUtils`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ConditioningKrea2Rebalance`
- `easy showAnything`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `SaveImage`
- `SaveImage`
- `easy seed`
- `easy seed`
- `KSampler` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `ConcatTextOfUtils`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `RHLLMChatNode`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `630893975497648`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（43/46）

**有卡**：`UNETLoader`、`CLIPLoader`、`RHLLMChatNode`、`Random Line`、`ConcatTextOfUtils`、`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`EmptyLatentImage`、`CR Prompt Text`、`ConditioningZeroOut`、`KSampler`、`ConditioningKrea2Rebalance`、`easy cleanGpuUsed`、`ImageConcatMulti`、`SaveImage`、`easy seed`、`LoraLoaderModelOnly`、`AddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
