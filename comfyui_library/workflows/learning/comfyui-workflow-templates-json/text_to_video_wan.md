---
key: comfyui-workflow-templates-json/text_to_video_wan.json
name: text_to_video_wan
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/text_to_video_wan.json
hash: 6cfcb2bcc842926d
official: true
coverage: 1
learned_at: 2026-10-07 21:36:40
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, UNETLoader, EmptyHunyuanLatentVideo, VAEDecode, CreateVideo, KSampler, SaveVideo, ModelSamplingSD3]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 82628696717253, "steps": 30}
---

# comfyui-workflow-templates-json/text_to_video_wan.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/text_to_video_wan.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `CreateVideo`
- `KSampler` ★核心
- `SaveVideo`
- `ModelSamplingSD3`

## 关键参数

- `seed` = `82628696717253`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`CreateVideo`、`KSampler`、`SaveVideo`、`ModelSamplingSD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、SaveVideo
