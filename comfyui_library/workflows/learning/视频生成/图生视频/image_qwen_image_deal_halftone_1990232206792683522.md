---
key: 视频生成/图生视频/image_qwen_image_deal_halftone_1990232206792683522.json
name: image_qwen_image_deal_halftone_1990232206792683522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1990232206792683522.json
hash: 772c1d2b4b4af523
coverage: 0.772727
learned_at: 2026-10-15 22:33:09
nodes: [MarkdownNote, MarkdownNote, Note, ModelSamplingAuraFlow, CLIPTextEncode, EmptySD3LatentImage, INTConstant, INTConstant, Note, KSampler, CLIPTextEncode, LoraLoaderModelOnly, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, VAEDecode, VAEUtils_VAEDecodeTiled, VAEUtils_CustomVAELoader, ImageScaleBy, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 584228356249918, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/image_qwen_image_deal_halftone_1990232206792683522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990232206792683522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `INTConstant`
- `INTConstant`
- `Note`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEUtils_VAEDecodeTiled` ★核心
- `VAEUtils_CustomVAELoader`
- `ImageScaleBy`
- `SaveImage`

## 关键参数

- `seed` = `584228356249918`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`ModelSamplingAuraFlow`、`CLIPTextEncode`、`EmptySD3LatentImage`、`INTConstant`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`VAEUtils_VAEDecodeTiled`、`VAEUtils_CustomVAELoader`、`ImageScaleBy`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、VAEUtils_CustomVAELoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
