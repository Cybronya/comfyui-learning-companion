---
key: 视频生成/图生视频/图生视频-rh-Wan2.2-Remix-I2V-提示词优化-模板_1986819504288296962.json
name: 图生视频-rh-Wan2.2-Remix-I2V-提示词优化-模板_1986819504288296962.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1986819504288296962.json
hash: 2c8ce1446707f5a9
coverage: 0.731707
learned_at: 2026-10-15 22:32:57
nodes: [KSamplerAdvanced, wanBlockSwap, ModelSamplingSD3, INTConstant, wanBlockSwap, ModelSamplingSD3, WanImageToVideo, KSamplerAdvanced, VAELoader, Seed (rgthree), ImageResize+, UNETLoader, UNETLoader, CLIPLoader, CR Text Concatenate, Text Multiline (Code Compatible), easy cleanGpuUsed, easy showAnything, Qwen3_VQA, Text Multiline (Code Compatible), SetNode, INTConstant, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, INTConstant, SetNode, INTConstant, SetNode, SetNode, VAEDecode, easy cleanGpuUsed, RIFE VFI, VHS_VideoCombine, ImageLoader, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频-rh-Wan2.2-Remix-I2V-提示词优化-模板_1986819504288296962.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986819504288296962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（41 个）：
- `KSamplerAdvanced` ★核心
- `wanBlockSwap`
- `ModelSamplingSD3`
- `INTConstant`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `Seed (rgthree)`
- `ImageResize+`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CR Text Concatenate`
- `Text Multiline (Code Compatible)`
- `easy cleanGpuUsed`
- `easy showAnything`
- `Qwen3_VQA`
- `Text Multiline (Code Compatible)`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `RIFE VFI`
- `VHS_VideoCombine`
- `ImageLoader`
- `INTConstant`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **73%**（30/41）

**有卡**：`KSamplerAdvanced`、`wanBlockSwap`、`ModelSamplingSD3`、`INTConstant`、`WanImageToVideo`、`VAELoader`、`Seed (rgthree)`、`ImageResize+`、`UNETLoader`、`CLIPLoader`、`CR Text Concatenate`、`Text Multiline (Code Compatible)`、`easy cleanGpuUsed`、`Qwen3_VQA`、`CLIPTextEncode`、`VAEDecode`、`RIFE VFI`、`VHS_VideoCombine`、`ImageLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、ImageResize+
