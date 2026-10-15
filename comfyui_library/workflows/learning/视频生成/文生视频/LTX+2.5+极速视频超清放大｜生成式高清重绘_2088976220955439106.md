---
key: 视频生成/文生视频/LTX+2.5+极速视频超清放大｜生成式高清重绘_2088976220955439106.json
name: LTX+2.5+极速视频超清放大｜生成式高清重绘_2088976220955439106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX+2.5+极速视频超清放大｜生成式高清重绘_2088976220955439106.json
hash: 767443b2a9914ccd
coverage: 0.9
learned_at: 2026-10-15 22:44:36
nodes: [LTXVLoopingSampler, CFGGuider, LTXVConditioning, VAEEncodeTiled, CreateVideo, LTXVSpatioTemporalTiledVAEDecode, MarkdownNote, UNETLoader, MarkdownNote, RandomNoise, KSamplerSelect, VAELoader, CLIPLoader, GetVideoComponents, LoadVideo, SaveVideo, Yuan_RTXVideoUpscaleH3, CLIPTextEncode, LoraLoaderModelOnly, ManualSigmas]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX+2.5+极速视频超清放大｜生成式高清重绘_2088976220955439106.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX+2.5+极速视频超清放大｜生成式高清重绘_2088976220955439106.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `LTXVLoopingSampler` ★核心
- `CFGGuider`
- `LTXVConditioning`
- `VAEEncodeTiled` ★核心
- `CreateVideo`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `MarkdownNote`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAELoader`
- `CLIPLoader`
- `GetVideoComponents`
- `LoadVideo`
- `SaveVideo`
- `Yuan_RTXVideoUpscaleH3`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`LTXVLoopingSampler`、`CFGGuider`、`LTXVConditioning`、`VAEEncodeTiled`、`CreateVideo`、`LTXVSpatioTemporalTiledVAEDecode`、`UNETLoader`、`RandomNoise`、`KSamplerSelect`、`VAELoader`、`CLIPLoader`、`GetVideoComponents`、`LoadVideo`、`SaveVideo`、`Yuan_RTXVideoUpscaleH3`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ManualSigmas`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGGuider、KSamplerSelect、LTXVLoopingSampler
