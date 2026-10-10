---
key: Anima vs Anima Preview3 vs Illustrious 对比测试_2100439731292168193.json
name: Anima vs Anima Preview3 vs Illustrious 对比测试_2100439731292168193
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima vs Anima Preview3 vs Illustrious 对比测试_2100439731292168193.json
hash: 337615625ead4cc8
coverage: 0.95
learned_at: 2026-10-10 21:26:14
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, SaveImage, AddLabel, CLIPTextEncode, ModelSamplingAuraFlow, KSampler, VAELoader, VAEDecode, SaveImage, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, ImageConcanate, AddLabel, AddLabel, easy seed, KSampler, AddLabel, ModelSamplingAuraFlow, KSampler, CheckpointLoaderSimple, CLIPTextEncode, CLIPLoader, VAELoader, CLIPLoader, UNETLoader, UNETLoader, ImageConcanate, VAEDecode, SaveImage, SaveImage, MarkdownNote, LoadImage, LoadImage, Text, LoadImage, LoadImage]
patterns: [text_to_image]
missing: [easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "waiIllustriousSDXL_v170.safetensors", "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "beta57", "seed": 42, "steps": 6, "width": 1024}
discoveries: [次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Anima vs Anima Preview3 vs Illustrious 对比测试_2100439731292168193.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima vs Anima Preview3 vs Illustrious 对比测试_2100439731292168193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageConcanate`
- `AddLabel`
- `AddLabel`
- `easy seed`
- `KSampler` ★核心
- `AddLabel`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ImageConcanate`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `Text`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `42`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `waiIllustriousSDXL_v170.safetensors`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`AddLabel`、`ModelSamplingAuraFlow`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`ImageConcanate`、`CheckpointLoaderSimple`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`Text`

**缺卡**（1）：`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
