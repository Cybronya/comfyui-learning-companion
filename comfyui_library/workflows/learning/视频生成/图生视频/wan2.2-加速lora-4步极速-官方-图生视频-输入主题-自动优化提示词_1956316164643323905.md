---
key: 视频生成/图生视频/wan2.2-加速lora-4步极速-官方-图生视频-输入主题-自动优化提示词_1956316164643323905.json
name: wan2.2-加速lora-4步极速-官方-图生视频-输入主题-自动优化提示词_1956316164643323905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-加速lora-4步极速-官方-图生视频-输入主题-自动优化提示词_1956316164643323905.json
hash: e505e8450d5160d1
coverage: 0.848485
learned_at: 2026-10-15 22:31:13
nodes: [CLIPLoader, VAELoader, UNETLoader, ModelSamplingSD3, UNETLoader, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CreateVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, WanImageToVideo, TextBox, easy showAnything, LayerUtility: PurgeVRAM, easy showAnything, CR Text Replace, MarkdownNote, easy ifElse, TextBox, RH_Captioner, LoadImage, TextBox, Int, Int, Int, PrimitiveBoolean, SimpleMath+, SaveVideo, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2-加速lora-4步极速-官方-图生视频-输入主题-自动优化提示词_1956316164643323905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956316164643323905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `TextBox`
- `easy showAnything`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `CR Text Replace`
- `MarkdownNote`
- `easy ifElse`
- `TextBox`
- `RH_Captioner`
- `LoadImage`
- `TextBox`
- `Int`
- `Int`
- `Int`
- `PrimitiveBoolean`
- `SimpleMath+`
- `SaveVideo`
- `MarkdownNote`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`LoraLoaderModelOnly`、`WanImageToVideo`、`TextBox`、`LayerUtility: PurgeVRAM`、`CR Text Replace`、`RH_Captioner`、`LoadImage`、`Int`、`PrimitiveBoolean`、`SimpleMath+`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
