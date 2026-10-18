---
key: 视频生成/图生视频/Wan2.2-Remix-V2-I2V 图生视频工作流_1988479150342193154.json
name: Wan2.2-Remix-V2-I2V 图生视频工作流_1988479150342193154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Remix-V2-I2V 图生视频工作流_1988479150342193154.json
hash: 203b2766d1b58e43
coverage: 0.866667
learned_at: 2026-10-15 22:33:02
nodes: [wanBlockSwap, ModelSamplingSD3, INTConstant, wanBlockSwap, ModelSamplingSD3, CLIPTextEncode, WanImageToVideo, ImageResize+, INTConstant, INTConstant, Seed (rgthree), INTConstant, INTConstant, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, VHS_VideoCombine, ImageLoader, INTConstant, RIFEInterpolation, CLIPTextEncode, Note, Note, Note, MarkdownNote, UNETLoader, UNETLoader, CLIPLoader, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-Remix-V2-I2V 图生视频工作流_1988479150342193154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988479150342193154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（30 个）：
- `wanBlockSwap`
- `ModelSamplingSD3`
- `INTConstant`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `ImageResize+`
- `INTConstant`
- `INTConstant`
- `Seed (rgthree)`
- `INTConstant`
- `INTConstant`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageLoader`
- `INTConstant`
- `RIFEInterpolation`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `MarkdownNote`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`wanBlockSwap`、`ModelSamplingSD3`、`INTConstant`、`CLIPTextEncode`、`WanImageToVideo`、`ImageResize+`、`Seed (rgthree)`、`VAEDecode`、`KSamplerAdvanced`、`VHS_VideoCombine`、`ImageLoader`、`RIFEInterpolation`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、ImageResize+
