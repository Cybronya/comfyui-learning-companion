---
key: 图片生成/文生图/HiDream dev_full Workflow ComfyOrg_1913645697319796738.json
name: HiDream dev_full Workflow ComfyOrg_1913645697319796738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/HiDream dev_full Workflow ComfyOrg_1913645697319796738.json
hash: df1604ee174bf080
coverage: 0.846154
learned_at: 2026-10-10 20:58:39
nodes: [CLIPTextEncode, ModelSamplingSD3, VAEDecode, VAELoader, QuadrupleCLIPLoader, EmptySD3LatentImage, SaveImage, MarkdownNote, KSampler, CLIPTextEncode, Note, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 28095740842945, "steps": 28}
---

# 图片生成/文生图/HiDream dev_full Workflow ComfyOrg_1913645697319796738.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/HiDream dev_full Workflow ComfyOrg_1913645697319796738.json`

## 结构

**节点**（13 个）：
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `VAEDecode`
- `VAELoader`
- `QuadrupleCLIPLoader`
- `EmptySD3LatentImage`
- `SaveImage`
- `MarkdownNote`
- `KSampler`
- `CLIPTextEncode`
- `Note`
- `UNETLoader`
- `UNETLoader`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `seed` = `28095740842945`
- `steps` = `28`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`VAEDecode`、`VAELoader`、`QuadrupleCLIPLoader`、`EmptySD3LatentImage`、`SaveImage`、`MarkdownNote`、`KSampler`、`Note`
