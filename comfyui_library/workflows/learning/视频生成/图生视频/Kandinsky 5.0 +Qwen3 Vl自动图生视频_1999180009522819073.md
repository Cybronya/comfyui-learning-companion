---
key: 视频生成/图生视频/Kandinsky 5.0 +Qwen3 Vl自动图生视频_1999180009522819073.json
name: Kandinsky 5.0 +Qwen3 Vl自动图生视频_1999180009522819073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1999180009522819073.json
hash: e780b8dec67f4830
coverage: 0.909091
learned_at: 2026-10-15 22:33:36
nodes: [UNETLoader, VAELoader, CLIPTextEncode, ImageScale, ModelSamplingSD3, Kandinsky5ImageToVideo, KSampler, CLIPTextEncode, CreateVideo, MarkdownNote, DualCLIPLoader, AILab_QwenVL, CR Prompt Text, RH_LLMAPI_NODE, LoadImage, VAEDecode, NormalizeVideoLatentStart, ReplaceVideoLatentFrames, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, easy showAnything, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 518634496447047, "steps": 50}
---

# 视频生成/图生视频/Kandinsky 5.0 +Qwen3 Vl自动图生视频_1999180009522819073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999180009522819073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ImageScale`
- `ModelSamplingSD3`
- `Kandinsky5ImageToVideo`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `MarkdownNote`
- `DualCLIPLoader`
- `AILab_QwenVL`
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `LoadImage`
- `VAEDecode` ★核心
- `NormalizeVideoLatentStart`
- `ReplaceVideoLatentFrames`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `easy showAnything`
- `SaveVideo`

## 关键参数

- `seed` = `518634496447047`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`ImageScale`、`ModelSamplingSD3`、`Kandinsky5ImageToVideo`、`KSampler`、`CreateVideo`、`DualCLIPLoader`、`AILab_QwenVL`、`CR Prompt Text`、`RH_LLMAPI_NODE`、`LoadImage`、`VAEDecode`、`NormalizeVideoLatentStart`、`ReplaceVideoLatentFrames`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、ReplaceVideoLatentFrames、NormalizeVideoLatentStart
