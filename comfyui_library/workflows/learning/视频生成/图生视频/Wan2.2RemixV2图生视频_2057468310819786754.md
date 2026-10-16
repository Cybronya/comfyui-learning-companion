---
key: 视频生成/图生视频/Wan2.2RemixV2图生视频_2057468310819786754.json
name: Wan2.2RemixV2图生视频_2057468310819786754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2057468310819786754.json
hash: 7ab54c21b5df97e2
coverage: 0.966667
learned_at: 2026-10-15 22:38:13
nodes: [wanBlockSwap, ModelSamplingSD3, INTConstant, wanBlockSwap, ModelSamplingSD3, CLIPTextEncode, WanImageToVideo, INTConstant, INTConstant, Seed (rgthree), KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, ImageLoader, INTConstant, RIFEInterpolation, UNETLoader, UNETLoader, CLIPLoader, VAELoader, Note, INTConstant, ImageResize+, Int, Int, Int, INTConstant, VAEDecode, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2RemixV2图生视频_2057468310819786754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2057468310819786754.json`

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
- `INTConstant`
- `INTConstant`
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `ImageLoader`
- `INTConstant`
- `RIFEInterpolation`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `INTConstant`
- `ImageResize+`
- `Int`
- `Int`
- `Int`
- `INTConstant`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`wanBlockSwap`、`ModelSamplingSD3`、`INTConstant`、`CLIPTextEncode`、`WanImageToVideo`、`Seed (rgthree)`、`KSamplerAdvanced`、`VHS_VideoCombine`、`ImageLoader`、`RIFEInterpolation`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageResize+`、`Int`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、ImageResize+
