---
key: comfyui-workflow-templates-json/wan2.1_fun_inp.json
name: wan2.1_fun_inp
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/wan2.1_fun_inp.json
hash: fcaa86b3cd82e7a0
official: true
coverage: 0.947368
learned_at: 2026-10-10 22:50:56
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, SkipLayerGuidanceDiT, CFGZeroStar, ModelSamplingSD3, LoadImage, WanFunInpaintToVideo, VAEDecode, UNetTemporalAttentionMultiply, SaveVideo, CreateVideo, CLIPLoader, VAELoader, UNETLoader, LoadImage, CLIPVisionLoader, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 622093119444720, "steps": 20}
---

# comfyui-workflow-templates-json/wan2.1_fun_inp.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/wan2.1_fun_inp.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `SkipLayerGuidanceDiT`
- `CFGZeroStar`
- `ModelSamplingSD3`
- `LoadImage`
- `WanFunInpaintToVideo`
- `VAEDecode` ★核心
- `UNetTemporalAttentionMultiply`
- `SaveVideo`
- `CreateVideo`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPVisionLoader`
- `MarkdownNote`

## 关键参数

- `seed` = `622093119444720`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`KSampler`、`CLIPTextEncode`、`CLIPVisionEncode`、`SkipLayerGuidanceDiT`、`CFGZeroStar`、`ModelSamplingSD3`、`LoadImage`、`WanFunInpaintToVideo`、`VAEDecode`、`UNetTemporalAttentionMultiply`、`SaveVideo`、`CreateVideo`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPVisionLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStar
