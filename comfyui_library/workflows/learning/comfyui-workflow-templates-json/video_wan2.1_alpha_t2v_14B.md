---
key: comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json
name: video_wan2.1_alpha_t2v_14B
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json
hash: 06540729fb1cc313
official: true
coverage: 0.894737
learned_at: 2026-10-10 22:50:32
nodes: [ImageToMask, InvertMask, VAEDecode, VAEDecode, JoinImageWithAlpha, CLIPTextEncode, SaveAnimatedWEBP, CLIPTextEncode, EmptyHunyuanLatentVideo, UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAELoader, VAELoader, ModelSamplingSD3, KSampler, MarkdownNote, MarkdownNote, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 558449140107503, "steps": 20}
---

# comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_wan2.1_alpha_t2v_14B.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ImageToMask`
- `InvertMask`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `JoinImageWithAlpha`
- `CLIPTextEncode` ★核心
- `SaveAnimatedWEBP`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAELoader`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `558449140107503`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`ImageToMask`、`InvertMask`、`VAEDecode`、`JoinImageWithAlpha`、`CLIPTextEncode`、`SaveAnimatedWEBP`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`ModelSamplingSD3`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo
