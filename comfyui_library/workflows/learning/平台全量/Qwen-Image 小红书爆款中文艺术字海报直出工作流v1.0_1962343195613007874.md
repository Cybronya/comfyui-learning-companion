---
key: 平台全量/Qwen-Image 小红书爆款中文艺术字海报直出工作流v1.0_1962343195613007874.json
name: Qwen-Image 小红书爆款中文艺术字海报直出工作流v1.0_1962343195613007874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image 小红书爆款中文艺术字海报直出工作流v1.0_1962343195613007874.json
hash: fcf47aec1cd7132d
coverage: 0.857143
learned_at: 2026-11-14 00:51:32
nodes: [KSampler, VAEDecode, ConditioningZeroOut, CLIPLoader, ModelSamplingAuraFlow, VAELoader, LoadImage, UNETLoader, SaveImage, CR SDXL Aspect Ratio, PreviewImage, LoraLoaderModelOnly, CLIPTextEncode, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 4.1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 159341827091316, "steps": 20}
---

# 平台全量/Qwen-Image 小红书爆款中文艺术字海报直出工作流v1.0_1962343195613007874.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image 小红书爆款中文艺术字海报直出工作流v1.0_1962343195613007874.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `LoadImage`
- `UNETLoader` ★核心
- `SaveImage`
- `CR SDXL Aspect Ratio`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `159341827091316`
- `steps` = `20`
- `cfg` = `4.1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`CLIPLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`LoadImage`、`UNETLoader`、`SaveImage`、`CR SDXL Aspect Ratio`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut
