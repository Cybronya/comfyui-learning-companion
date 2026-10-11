---
key: 视频生成/文生视频/小说原文转15秒漫剧｜Seedance2.5一键文生视频生成_2092553338125643778.json
name: 小说原文转15秒漫剧｜Seedance2.5一键文生视频生成_2092553338125643778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/小说原文转15秒漫剧｜Seedance2.5一键文生视频生成_2092553338125643778.json
hash: 09d6ad3f62c67e63
coverage: 0.809524
learned_at: 2026-10-11 21:30:38
nodes: [LoadImage, LoadImage, CR Prompt Text, CR Prompt Text, CR Prompt Text, RHHiddenNodes, RHLLMChatNode, ShowText|pysssss, LoadImage, RHHiddenNodes, RHHiddenNodes, RH_RhartImageG2OfficialImageToImage, SaveImage, RH_BytedanceSeedance25TokenMultimodalVideo, SaveVideo, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: [CR Prompt Text, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/小说原文转15秒漫剧｜Seedance2.5一键文生视频生成_2092553338125643778.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/小说原文转15秒漫剧｜Seedance2.5一键文生视频生成_2092553338125643778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `RHHiddenNodes`
- `RHLLMChatNode`
- `ShowText|pysssss`
- `LoadImage`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`
- `RH_BytedanceSeedance25TokenMultimodalVideo`
- `SaveVideo`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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

覆盖率 **81%**（34/42）

**有卡**：`LoadImage`、`RHHiddenNodes`、`RHLLMChatNode`、`RH_RhartImageG2OfficialImageToImage`、`SaveImage`、`RH_BytedanceSeedance25TokenMultimodalVideo`、`SaveVideo`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（3）：`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
