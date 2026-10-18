---
key: 视频生成/图生视频/WAN2.2夜魔佬中间帧_1982294061598023681.json
name: WAN2.2夜魔佬中间帧_1982294061598023681.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2夜魔佬中间帧_1982294061598023681.json
hash: eed897178abbe2f4
coverage: 1
learned_at: 2026-10-15 22:32:40
nodes: [ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, INTConstant, KSamplerAdvanced, CLIPTextEncode, INTConstant, VAEDecode, VHS_VideoCombine, CLIPTextEncode, ImpactImageInfo, WanFirstMiddleLastFrameToVideo, LoadImage, LoadImage, LoadImage, CLIPLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2夜魔佬中间帧_1982294061598023681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982294061598023681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `ImpactImageInfo`
- `WanFirstMiddleLastFrameToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`ModelSamplingSD3`、`KSamplerAdvanced`、`INTConstant`、`CLIPTextEncode`、`VAEDecode`、`VHS_VideoCombine`、`ImpactImageInfo`、`WanFirstMiddleLastFrameToVideo`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
