---
key: 视频生成/图生视频/shake the breast（wan smooth mix）_1991419275315531777.json
name: shake the breast（wan smooth mix）_1991419275315531777.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/shake the breast（wan smooth mix）_1991419275315531777.json
hash: ab29c54eac8a2edf
coverage: 0.875
learned_at: 2026-10-15 22:33:13
nodes: [UNETLoader, UNETLoader, CLIPLoader, CLIPVisionLoader, VAELoader, CLIPTextEncode, CLIPVisionEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, intToFloat _O, Int, Int, Int, WanImageToVideo, MathExpression|pysssss, CR Text, RHHiddenNodes, WanMoeKSampler, VAEDecode, LoadImage, Note, Note, Note, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/shake the breast（wan smooth mix）_1991419275315531777.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1991419275315531777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `intToFloat _O`
- `Int`
- `Int`
- `Int`
- `WanImageToVideo`
- `MathExpression|pysssss`
- `CR Text`
- `RHHiddenNodes`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`intToFloat _O`、`Int`、`WanImageToVideo`、`MathExpression|pysssss`、`CR Text`、`RHHiddenNodes`、`WanMoeKSampler`、`VAEDecode`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、CLIPVisionEncode
