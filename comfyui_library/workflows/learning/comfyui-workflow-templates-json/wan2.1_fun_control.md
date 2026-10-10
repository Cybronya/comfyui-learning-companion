---
key: comfyui-workflow-templates-json/wan2.1_fun_control.json
name: wan2.1_fun_control
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/wan2.1_fun_control.json
hash: 79ca227973ae5f09
official: true
coverage: 0.909091
learned_at: 2026-10-10 22:50:55
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, CLIPVisionEncode, WanFunControlToVideo, SkipLayerGuidanceDiT, CFGZeroStar, ModelSamplingSD3, UNetTemporalAttentionMultiply, Canny, PreviewImage, VAEDecode, CreateVideo, SaveVideo, MarkdownNote, LoadImage, LoadVideo, GetVideoComponents]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 887940314022885, "steps": 20}
---

# comfyui-workflow-templates-json/wan2.1_fun_control.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/wan2.1_fun_control.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `WanFunControlToVideo`
- `SkipLayerGuidanceDiT`
- `CFGZeroStar`
- `ModelSamplingSD3`
- `UNetTemporalAttentionMultiply`
- `Canny`
- `PreviewImage`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `LoadImage`
- `LoadVideo`
- `GetVideoComponents`

## 关键参数

- `seed` = `887940314022885`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`KSampler`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`WanFunControlToVideo`、`SkipLayerGuidanceDiT`、`CFGZeroStar`、`ModelSamplingSD3`、`UNetTemporalAttentionMultiply`、`Canny`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`LoadImage`、`LoadVideo`、`GetVideoComponents`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Canny
