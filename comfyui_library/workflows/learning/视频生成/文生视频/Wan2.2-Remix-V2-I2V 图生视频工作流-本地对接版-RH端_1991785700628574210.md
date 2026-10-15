---
key: 视频生成/文生视频/Wan2.2-Remix-V2-I2V 图生视频工作流-本地对接版-RH端_1991785700628574210.json
name: Wan2.2-Remix-V2-I2V 图生视频工作流-本地对接版-RH端_1991785700628574210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-Remix-V2-I2V 图生视频工作流-本地对接版-RH端_1991785700628574210.json
hash: 4e74e782defbadd6
coverage: 0.882353
learned_at: 2026-10-15 22:47:12
nodes: [wanBlockSwap, CLIPTextEncode, Note, Note, MarkdownNote, CLIPLoader, WanImageToVideo, INTConstant, CLIPTextEncode, VHS_VideoCombine, RIFEInterpolation, INTConstant, INTConstant, Note, INTConstant, INTConstant, wanBlockSwap, UNETLoader, UNETLoader, INTConstant, KSamplerAdvanced, KSamplerAdvanced, ImageResize+, ImageResize+, ModelSamplingSD3, ModelSamplingSD3, SaveLatent, TT_img_enc_v2, VAEDecode, Seed (rgthree), VAELoader, ImageLoader, Text Multiline, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2-Remix-V2-I2V 图生视频工作流-本地对接版-RH端_1991785700628574210.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-Remix-V2-I2V 图生视频工作流-本地对接版-RH端_1991785700628574210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `wanBlockSwap`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `MarkdownNote`
- `CLIPLoader`
- `WanImageToVideo`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `RIFEInterpolation`
- `INTConstant`
- `INTConstant`
- `Note`
- `INTConstant`
- `INTConstant`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResize+`
- `ImageResize+`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SaveLatent`
- `TT_img_enc_v2`
- `VAEDecode` ★核心
- `Seed (rgthree)`
- `VAELoader`
- `ImageLoader`
- `Text Multiline`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`wanBlockSwap`、`CLIPTextEncode`、`CLIPLoader`、`WanImageToVideo`、`INTConstant`、`VHS_VideoCombine`、`RIFEInterpolation`、`UNETLoader`、`KSamplerAdvanced`、`ImageResize+`、`ModelSamplingSD3`、`SaveLatent`、`TT_img_enc_v2`、`VAEDecode`、`Seed (rgthree)`、`VAELoader`、`ImageLoader`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、SaveLatent
