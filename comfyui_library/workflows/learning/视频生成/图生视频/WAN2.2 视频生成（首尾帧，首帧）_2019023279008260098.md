---
key: 视频生成/图生视频/WAN2.2 视频生成（首尾帧，首帧）_2019023279008260098.json
name: WAN2.2 视频生成（首尾帧，首帧）_2019023279008260098.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2019023279008260098.json
hash: 060893ecfaa200ae
coverage: 0.945205
learned_at: 2026-10-15 22:35:00
nodes: [CLIPTextEncode, MarkdownNote, MarkdownNote, Note, UnetLoaderGGUF, UnetLoaderGGUF, VAEDecode, CreateVideo, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, VAELoader, CLIPLoader, KSamplerAdvanced, SaveVideo, LoadImage, WanImageToVideo, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPTextEncode, VAEDecode, KSamplerAdvanced, CLIPVisionEncode, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, CreateVideo, LoadImage, LoraLoaderModelOnly, ApplySageAttention, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, ApplySageAttention, ModelSamplingSD3, SimpleMath+, Int, ModelSamplingSD3, LoraLoaderModelOnly, VAELoader, VAEDecode, CLIPVisionEncode, CLIPVisionLoader, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, SaveVideo, CreateVideo, LoraLoaderModelOnly, ApplySageAttention, ModelSamplingSD3, KSamplerAdvanced, ApplySageAttention, SimpleMath+, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo, LoadImage, LoadImage, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2 视频生成（首尾帧，首帧）_2019023279008260098.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019023279008260098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `LoadImage`
- `WanImageToVideo`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CreateVideo`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ApplySageAttention`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ApplySageAttention`
- `ModelSamplingSD3`
- `SimpleMath+`
- `Int`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `ApplySageAttention`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `ApplySageAttention`
- `SimpleMath+`
- `Int`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstLastFrameToVideo`
- `LoadImage`
- `LoadImage`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `SaveVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（69/73）

**有卡**：`CLIPTextEncode`、`UnetLoaderGGUF`、`VAEDecode`、`CreateVideo`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`SaveVideo`、`LoadImage`、`WanImageToVideo`、`CLIPVisionEncode`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`ApplySageAttention`、`SimpleMath+`、`Int`、`WanFirstLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
