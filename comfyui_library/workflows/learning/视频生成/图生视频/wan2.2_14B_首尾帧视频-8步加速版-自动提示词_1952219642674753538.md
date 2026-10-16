---
key: 视频生成/图生视频/wan2.2_14B_首尾帧视频-8步加速版-自动提示词_1952219642674753538.json
name: wan2.2_14B_首尾帧视频-8步加速版-自动提示词_1952219642674753538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952219642674753538.json
hash: b47bcae176aa56b6
coverage: 0.861111
learned_at: 2026-10-15 22:31:00
nodes: [CLIPVisionEncode, CLIPVisionEncode, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, CLIPLoader, CLIPVisionLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, WanVideoNAG, CLIPTextEncode, WanFirstLastFrameToVideo, ImageStitch, easy showAnything, RH_Translator, LoadImage, LoadImage, SimpleMath+, KSamplerAdvanced, CLIPTextEncode, DF_Integer, Textbox, PrimitiveBoolean, easy showAnything, easy ifElse, CR Image Size, RHHiddenNodes, MarkdownNote, MarkdownNote, UNETLoader, VAEDecode, CustomAddLabel, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2_14B_首尾帧视频-8步加速版-自动提示词_1952219642674753538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952219642674753538.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `ImageStitch`
- `easy showAnything`
- `RH_Translator`
- `LoadImage`
- `LoadImage`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `DF_Integer`
- `Textbox`
- `PrimitiveBoolean`
- `easy showAnything`
- `easy ifElse`
- `CR Image Size`
- `RHHiddenNodes`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CustomAddLabel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`CLIPVisionEncode`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`UNETLoader`、`WanVideoNAG`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`ImageStitch`、`RH_Translator`、`LoadImage`、`SimpleMath+`、`DF_Integer`、`Textbox`、`PrimitiveBoolean`、`CR Image Size`、`RHHiddenNodes`、`VAEDecode`、`CustomAddLabel`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
