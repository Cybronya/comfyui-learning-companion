---
key: 视频生成/文生视频/WAN2.2_TI2V_5B_加速生成_1950129189842280449.json
name: WAN2.2_TI2V_5B_加速生成_1950129189842280449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2_TI2V_5B_加速生成_1950129189842280449.json
hash: d297e02ff8448a59
coverage: 0.52
learned_at: 2026-10-15 22:47:04
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, Bookmark (rgthree), SetNode, GetNode, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), StringConcatenate, StringConcatenate, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), PrimitiveString, PrimitiveString, PrimitiveString, SetNode, GetNode, Reroute, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, Wan22ImageToVideoLatent, GetNode, GetNode, GetNode, GetNode, Note, Label (rgthree), VHS_VideoCombine, MarkdownNote, easy int, easy int, UNETLoader, easy int, KSampler, VAEDecode, CLIPLoader, VAELoader, PrimitiveStringMultiline, LoadImage, easy seed]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 84473059529407, "steps": 30}
---

# 视频生成/文生视频/WAN2.2_TI2V_5B_加速生成_1950129189842280449.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2_TI2V_5B_加速生成_1950129189842280449.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（50 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Bookmark (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `StringConcatenate`
- `StringConcatenate`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `PrimitiveString`
- `PrimitiveString`
- `PrimitiveString`
- `SetNode`
- `GetNode`
- `Reroute`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Wan22ImageToVideoLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `MarkdownNote`
- `easy int`
- `easy int`
- `UNETLoader` ★核心
- `easy int`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `LoadImage`
- `easy seed`

## 关键参数

- `seed` = `84473059529407`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（26/50）

**有卡**：`Bookmark (rgthree)`、`Label (rgthree)`、`StringConcatenate`、`ModelSamplingSD3`、`CLIPTextEncode`、`Wan22ImageToVideoLatent`、`VHS_VideoCombine`、`easy int`、`UNETLoader`、`KSampler`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`LoadImage`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、easy seed
