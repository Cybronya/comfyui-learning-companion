---
key: 视频生成/文生视频/🐳wan2.2文生+图生视频 5B模型🐳_1949986413421969410.json
name: 🐳wan2.2文生+图生视频 5B模型🐳_1949986413421969410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1949986413421969410.json
hash: 8ed38d242879f047
coverage: 0.888889
learned_at: 2026-10-15 22:43:33
nodes: [CLIPTextEncode, VAELoader, KSampler, ModelSamplingSD3, CLIPTextEncode, ImpactInt, ImpactInt, ImpactInt, SimpleMath+, Wan22ImageToVideoLatent, VAEDecode, MarkdownNote, Fast Groups Bypasser (rgthree), CLIPLoader, VHS_VideoCombine, UNETLoader, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 573914400313739, "steps": 20}
---

# 视频生成/文生视频/🐳wan2.2文生+图生视频 5B模型🐳_1949986413421969410.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949986413421969410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（18 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `SimpleMath+`
- `Wan22ImageToVideoLatent`
- `VAEDecode` ★核心
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `573914400313739`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CLIPTextEncode`、`VAELoader`、`KSampler`、`ModelSamplingSD3`、`ImpactInt`、`SimpleMath+`、`Wan22ImageToVideoLatent`、`VAEDecode`、`CLIPLoader`、`VHS_VideoCombine`、`UNETLoader`、`LoadImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Wan22ImageToVideoLatent
