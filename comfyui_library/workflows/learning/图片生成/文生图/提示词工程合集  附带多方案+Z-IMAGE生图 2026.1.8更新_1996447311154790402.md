---
key: 图片生成/文生图/提示词工程合集  附带多方案+Z-IMAGE生图 2026.1.8更新_1996447311154790402.json
name: 提示词工程合集  附带多方案+Z-IMAGE生图 2026.1.8更新_1996447311154790402
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/提示词工程合集  附带多方案+Z-IMAGE生图 2026.1.8更新_1996447311154790402.json
hash: 594178edb7c40092
coverage: 0.555556
learned_at: 2026-10-19 21:33:32
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, CLIPTextEncode, ConditioningZeroOut, VAEDecode, SaveImage, KSampler, CLIPLoader, UNETLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, KSampler, VAEDecode, SaveImage, easy promptList, EmptyLatentImage, Note, Note, LoadImage, Note, Note, LoadImage, Note, Note, Note, Note, Note, JjkText, MarkdownNote, Note, Note, JjkText, PreviewAny, CLIPLoader, UNETLoader, VAELoader, CLIPTextEncode, SaveImage, ConditioningZeroOut, VAEDecode, EmptyLatentImage, RH_LLMAPI_Pro_Node, RH_LLMAPI_Pro_Node, MarkdownNote, KSampler, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PreviewAny, Note, Fast Groups Bypasser (rgthree), Note, LoadImage, LoadImage, JjkText, LoadImage, Note, Note, JjkText, Note, MarkdownNote]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "dpmpp_2m_sde", "scheduler": "sgm_uniform", "seed": 1018689829019483, "steps": 9, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/提示词工程合集  附带多方案+Z-IMAGE生图 2026.1.8更新_1996447311154790402.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/提示词工程合集  附带多方案+Z-IMAGE生图 2026.1.8更新_1996447311154790402.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（63 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy promptList`
- `EmptyLatentImage` ★核心
- `Note`
- `Note`
- `LoadImage`
- `Note`
- `Note`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `JjkText`
- `MarkdownNote`
- `Note`
- `Note`
- `JjkText`
- `PreviewAny`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `RH_LLMAPI_Pro_Node`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `LoadImage`
- `Note`
- `Note`
- `JjkText`
- `Note`
- `MarkdownNote`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1018689829019483`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **56%**（35/63）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`KSampler`、`easy promptList`、`LoadImage`、`RH_LLMAPI_Pro_Node`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
