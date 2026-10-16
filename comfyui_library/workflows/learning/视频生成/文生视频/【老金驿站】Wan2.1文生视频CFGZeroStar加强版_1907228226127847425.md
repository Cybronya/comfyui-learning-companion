---
key: 视频生成/文生视频/【老金驿站】Wan2.1文生视频CFGZeroStar加强版_1907228226127847425.json
name: 【老金驿站】Wan2.1文生视频CFGZeroStar加强版_1907228226127847425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1907228226127847425.json
hash: 0b36a27cf58c7b15
coverage: 1
learned_at: 2026-10-15 22:43:21
nodes: [VAEDecode, CLIPTextEncode, CLIPLoaderGGUF, EmptyHunyuanLatentVideo, CLIPLoader, UNETLoader, CLIPTextEncode, VAELoader, VHS_VideoCombine, KSampler, CFGZeroStarAndInit]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 750544171648989, "steps": 30}
---

# 视频生成/文生视频/【老金驿站】Wan2.1文生视频CFGZeroStar加强版_1907228226127847425.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1907228226127847425.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoaderGGUF`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `CFGZeroStarAndInit`

## 关键参数

- `seed` = `750544171648989`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`CLIPLoaderGGUF`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`VHS_VideoCombine`、`KSampler`、`CFGZeroStarAndInit`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStarAndInit、EmptyHunyuanLatentVideo
