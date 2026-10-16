---
key: 视频生成/图生视频/Kandinsky 5.0 图生视频_1998819521249075201.json
name: Kandinsky 5.0 图生视频_1998819521249075201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1998819521249075201.json
hash: a7bf9adb8ca21655
coverage: 0.789474
learned_at: 2026-10-15 22:33:34
nodes: [MarkdownNote, UNETLoader, VAELoader, CLIPTextEncode, ImageScale, ModelSamplingSD3, Kandinsky5ImageToVideo, KSampler, DualCLIPLoader, PrimitiveInt, PrimitiveInt, CLIPTextEncode, ReplaceVideoLatentFrames, VAEDecode, NormalizeVideoLatentStart, CreateVideo, MarkdownNote, LoadImage, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 700144514916954, "steps": 50}
---

# 视频生成/图生视频/Kandinsky 5.0 图生视频_1998819521249075201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998819521249075201.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `MarkdownNote`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ImageScale`
- `ModelSamplingSD3`
- `Kandinsky5ImageToVideo`
- `KSampler` ★核心
- `DualCLIPLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `ReplaceVideoLatentFrames`
- `VAEDecode` ★核心
- `NormalizeVideoLatentStart`
- `CreateVideo`
- `MarkdownNote`
- `LoadImage`
- `SaveVideo`

## 关键参数

- `seed` = `700144514916954`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`ImageScale`、`ModelSamplingSD3`、`Kandinsky5ImageToVideo`、`KSampler`、`DualCLIPLoader`、`ReplaceVideoLatentFrames`、`VAEDecode`、`NormalizeVideoLatentStart`、`CreateVideo`、`LoadImage`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、ReplaceVideoLatentFrames、NormalizeVideoLatentStart
