---
key: 视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_1928466472526553089.json
name: Wan2 2.1 Vace GGUF 6步生成视频_1928466472526553089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_1928466472526553089.json
hash: e92a04639a444112
coverage: 0.887097
learned_at: 2026-10-10 23:06:29
nodes: [SaveVideo, CLIPTextEncode, KSampler, VAEDecode, CreateVideo, MarkdownNote, TrimVideoLatent, WanVaceToVideo, CLIPTextEncode, KSampler, TrimVideoLatent, VAEDecode, CreateVideo, ModelSamplingSD3, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSampler, TrimVideoLatent, VAEDecode, CreateVideo, WanVaceToVideo, CLIPTextEncode, CLIPTextEncode, LoadImage, ModelSamplingSD3, WanVaceToVideo, KSampler, TrimVideoLatent, VAEDecode, CreateVideo, GetVideoComponents, PreviewImage, CLIPLoader, CLIPTextEncode, KSampler, TrimVideoLatent, VAEDecode, CreateVideo, ModelSamplingSD3, CLIPTextEncode, WanVaceToVideo, VAELoader, UnetLoaderGGUF, CLIPTextEncode, WanVaceToVideo, LoadVideo, SaveVideo, LoadImage, SaveVideo, CLIPTextEncode, CLIPTextEncode, Power Lora Loader (rgthree), LoadImage, SaveVideo, AIO_Preprocessor, LoadImage, Power Lora Loader (rgthree), Fast Groups Muter (rgthree), easy imageColorMatch, SaveVideo, MarkdownNote]
patterns: []
missing: [easy imageColorMatch, Power Lora Loader (rgthree), Power Lora Loader (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 839334514552854, "steps": 20}
discoveries: [次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_1928466472526553089.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2 2.1 Vace GGUF 6步生成视频_1928466472526553089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `MarkdownNote`
- `TrimVideoLatent`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `GetVideoComponents`
- `PreviewImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `LoadVideo`
- `SaveVideo`
- `LoadImage`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Power Lora Loader (rgthree)`
- `LoadImage`
- `SaveVideo`
- `AIO_Preprocessor`
- `LoadImage`
- `Power Lora Loader (rgthree)`
- `Fast Groups Muter (rgthree)`
- `easy imageColorMatch`
- `SaveVideo`
- `MarkdownNote`

## 关键参数

- `seed` = `839334514552854`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（55/62）

**有卡**：`SaveVideo`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`CreateVideo`、`TrimVideoLatent`、`WanVaceToVideo`、`ModelSamplingSD3`、`LoadImage`、`GetVideoComponents`、`CLIPLoader`、`VAELoader`、`UnetLoaderGGUF`、`LoadVideo`、`AIO_Preprocessor`

**缺卡**（3）：`easy imageColorMatch`、`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、TrimVideoLatent、SaveVideo

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
