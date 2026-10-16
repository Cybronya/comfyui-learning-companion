---
key: 视频生成/图生视频/wan2.2-TI2V-5B-ComfyUI官方_1949844295606034434.json
name: wan2.2-TI2V-5B-ComfyUI官方_1949844295606034434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949844295606034434.json
hash: b679c50e5c311342
coverage: 0.857143
learned_at: 2026-10-15 22:30:50
nodes: [CreateVideo, KSampler, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, VAEDecodeTiled, Wan22ImageToVideoLatent, Text Multiline, MarkdownNote, ImageResizeKJv2, SaveVideo, VAELoader, CLIPLoader, UNETLoader, LoadImage, Note, Note, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], MathExpression|pysssss]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 610319060814643, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/wan2.2-TI2V-5B-ComfyUI官方_1949844295606034434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949844295606034434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CreateVideo`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecodeTiled` ★核心
- `Wan22ImageToVideoLatent`
- `Text Multiline`
- `MarkdownNote`
- `ImageResizeKJv2`
- `SaveVideo`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `Note`
- `Note`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `610319060814643`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CreateVideo`、`KSampler`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAEDecodeTiled`、`Wan22ImageToVideoLatent`、`Text Multiline`、`ImageResizeKJv2`、`SaveVideo`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`Primitive integer [Crystools]`、`MathExpression|pysssss`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled、Wan22ImageToVideoLatent

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
