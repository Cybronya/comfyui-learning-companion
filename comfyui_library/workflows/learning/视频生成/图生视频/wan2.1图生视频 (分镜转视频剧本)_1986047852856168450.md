---
key: 视频生成/图生视频/wan2.1图生视频 (分镜转视频剧本)_1986047852856168450.json
name: wan2.1图生视频 (分镜转视频剧本)_1986047852856168450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1986047852856168450.json
hash: 197b9114a77f5293
coverage: 0.894737
learned_at: 2026-10-15 22:32:53
nodes: [CLIPLoader, VAELoader, CLIPVisionLoader, KSampler, VAEDecode, ConstrainImage|pysssss, CLIPVisionEncode, CLIPTextEncode, ModelSamplingSD3, PrimitiveNode, PrimitiveNode, RIFE VFI, VHS_VideoCombine, LoadImage, CLIPTextEncode, easy imageSize, WanImageToVideo, UNETLoader, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 197632319968678, "steps": 10}
---

# 视频生成/图生视频/wan2.1图生视频 (分镜转视频剧本)_1986047852856168450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986047852856168450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConstrainImage|pysssss`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PrimitiveNode`
- `PrimitiveNode`
- `RIFE VFI`
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `197632319968678`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`KSampler`、`VAEDecode`、`ConstrainImage|pysssss`、`CLIPVisionEncode`、`CLIPTextEncode`、`ModelSamplingSD3`、`RIFE VFI`、`VHS_VideoCombine`、`LoadImage`、`easy imageSize`、`WanImageToVideo`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
