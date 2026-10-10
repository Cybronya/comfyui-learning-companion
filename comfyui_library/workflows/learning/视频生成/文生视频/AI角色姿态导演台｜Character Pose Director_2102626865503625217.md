---
key: 视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json
name: AI角色姿态导演台｜Character Pose Director_2102626865503625217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json
hash: ae0fed2e8bdb6f26
coverage: 0.928571
learned_at: 2026-10-10 22:58:37
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, QwenImage21Cache, TextEncodeQwenImage21, Image Comparer (rgthree), GetImageSize, SaveImage, LoraLoaderModelOnly, LoadImage, VNCCS_PoseStudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 488345170733023, "steps": 25, "width": 1024}
---

# 视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `GetImageSize`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VNCCS_PoseStudio`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `488345170733023`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`GetImageSize`、`SaveImage`、`LoraLoaderModelOnly`、`LoadImage`、`VNCCS_PoseStudio`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
