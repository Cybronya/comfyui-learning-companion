---
key: 视频生成/图生视频/LTXV0.9.6-秒级视频生成-图生视频_1897512765190262785.json
name: LTXV0.9.6-秒级视频生成-图生视频_1897512765190262785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1897512765190262785.json
hash: 00f84b4cfd1db47d
coverage: 0.952381
learned_at: 2026-10-15 22:29:18
nodes: [LTXVScheduler, KSamplerSelect, LTXVConditioning, SamplerCustom, LTXVImgToVideo, CLIPLoader, LTXVPreprocess, CLIPTextEncode, CR Text Concatenate, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], VHS_VideoCombine, VAEDecode, CLIPTextEncode, CheckpointLoaderSimple, Primitive string [Crystools], LoadImage, Fast Groups Bypasser (rgthree), LTXVPromptEnhancerLoader, LTXVPromptEnhancer]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-2b-0.9.6-dev-04-25-v1.safetensors"}
---

# 视频生成/图生视频/LTXV0.9.6-秒级视频生成-图生视频_1897512765190262785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1897512765190262785.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `LTXVImgToVideo`
- `CLIPLoader`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `Primitive string [Crystools]`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LTXVPromptEnhancerLoader`
- `LTXVPromptEnhancer`

## 关键参数

- `checkpoint` = `ltxv-2b-0.9.6-dev-04-25-v1.safetensors`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`LTXVScheduler`、`KSamplerSelect`、`LTXVConditioning`、`SamplerCustom`、`LTXVImgToVideo`、`CLIPLoader`、`LTXVPreprocess`、`CLIPTextEncode`、`CR Text Concatenate`、`Primitive integer [Crystools]`、`VHS_VideoCombine`、`VAEDecode`、`CheckpointLoaderSimple`、`Primitive string [Crystools]`、`LoadImage`、`LTXVPromptEnhancerLoader`、`LTXVPromptEnhancer`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、LTXVConditioning
