---
key: 视频生成/图生视频/LTXV 0.9.5图生视频工作流_1903736923179880450.json
name: LTXV 0.9.5图生视频工作流_1903736923179880450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1903736923179880450.json
hash: fb33a138875fa245
coverage: 0.941176
learned_at: 2026-10-15 22:29:25
nodes: [LTXVPromptEnhancerLoader, CLIPTextEncode, CLIPTextEncode, KSamplerSelect, LTXVScheduler, LTXVConditioning, SamplerCustom, VAEDecode, LTXVPromptEnhancer, ShowText|pysssss, LTXVImgToVideo, VHS_VideoCombine, ImageScale, LoadImage, CLIPLoader, CheckpointLoaderSimple, LTXVPreprocess]
patterns: []
missing: []
parameters: {"checkpoint": "LTXV-2b-v0.9.5.safetensors"}
---

# 视频生成/图生视频/LTXV 0.9.5图生视频工作流_1903736923179880450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1903736923179880450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `LTXVPromptEnhancerLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `LTXVPromptEnhancer`
- `ShowText|pysssss`
- `LTXVImgToVideo`
- `VHS_VideoCombine`
- `ImageScale`
- `LoadImage`
- `CLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVPreprocess`

## 关键参数

- `checkpoint` = `LTXV-2b-v0.9.5.safetensors`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`LTXVPromptEnhancerLoader`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVScheduler`、`LTXVConditioning`、`SamplerCustom`、`VAEDecode`、`LTXVPromptEnhancer`、`LTXVImgToVideo`、`VHS_VideoCombine`、`ImageScale`、`LoadImage`、`CLIPLoader`、`CheckpointLoaderSimple`、`LTXVPreprocess`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、LTXVConditioning
