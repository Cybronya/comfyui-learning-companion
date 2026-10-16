---
key: 视频生成/图生视频/Wan2.2-子弹时间【创意玩法】_1984075275195613186.json
name: Wan2.2-子弹时间【创意玩法】_1984075275195613186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1984075275195613186.json
hash: 16f7f1259291c5d5
coverage: 0.9375
learned_at: 2026-10-15 22:32:47
nodes: [KSamplerAdvanced, INTConstant, INTConstant, Int, PreviewImage, CLIPTextEncode, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, CLIPTextEncode, VAELoader, LoadImage, WanImageToVideo, VAEDecode, VHS_VideoCombine, RHHiddenNodes]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-子弹时间【创意玩法】_1984075275195613186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1984075275195613186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `Int`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RHHiddenNodes`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`KSamplerAdvanced`、`INTConstant`、`Int`、`CLIPTextEncode`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`LoadImage`、`WanImageToVideo`、`VAEDecode`、`VHS_VideoCombine`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、Int、INTConstant
