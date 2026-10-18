---
key: 视频生成/图生视频/wan2.2图生视频_2102213428411715585.json
name: wan2.2图生视频_2102213428411715585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频_2102213428411715585.json
hash: f3816d7fa15d370f
coverage: 1
learned_at: 2026-10-17 02:29:37
nodes: [wanBlockSwap, ModelSamplingSD3, INTConstant, wanBlockSwap, ModelSamplingSD3, CLIPTextEncode, WanImageToVideo, INTConstant, INTConstant, Seed (rgthree), KSamplerAdvanced, KSamplerAdvanced, INTConstant, RIFEInterpolation, UNETLoader, UNETLoader, CLIPLoader, VAELoader, INTConstant, ImageResize+, Int, Int, Int, INTConstant, VAEDecode, VHS_VideoCombine, CLIPTextEncode, VHS_VideoCombine, ImageLoader]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2图生视频_2102213428411715585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频_2102213428411715585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
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
- `INTConstant`
- `RIFEInterpolation`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `INTConstant`
- `ImageResize+`
- `Int`
- `Int`
- `Int`
- `INTConstant`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `ImageLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`wanBlockSwap`、`ModelSamplingSD3`、`INTConstant`、`CLIPTextEncode`、`WanImageToVideo`、`Seed (rgthree)`、`KSamplerAdvanced`、`RIFEInterpolation`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageResize+`、`Int`、`VAEDecode`、`VHS_VideoCombine`、`ImageLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、ImageResize+
