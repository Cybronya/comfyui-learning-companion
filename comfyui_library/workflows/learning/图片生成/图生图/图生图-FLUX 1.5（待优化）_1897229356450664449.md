---
key: 图片生成/图生图/图生图-FLUX 1.5（待优化）_1897229356450664449.json
name: 图生图-FLUX 1.5（待优化）_1897229356450664449
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生图-FLUX 1.5（待优化）_1897229356450664449.json
hash: 81f4bae8eab0fb86
coverage: 0.865385
learned_at: 2026-10-23 12:42:53
nodes: [VAELoader, RandomNoise, VAEEncode, FluxGuidance, Florence2Run, Florence2ModelLoader, KSamplerSelect, BasicGuider, KSamplerSelect, UNETLoader, DualCLIPLoader, ttN concat, VAELoader, SamplerCustomAdvanced, FluxGuidance, CLIPTextEncode, TextInputBasic, ttN concat, ShowText|pysssss, VAEEncode, TextInputBasic, Image Comparer (rgthree), KSampler, TextInputBasic, LoadImage, TextInputBasic, WD14Tagger|pysssss, ttN concat, ttN concat, ShowText|pysssss, CLIPTextEncode, CLIPTextEncode, VAEDecode, VAEEncode, CheckpointLoaderSimple, RandomNoise, BasicGuider, VAEDecode, LoadImage, Note, BasicScheduler, BasicScheduler, Fast Groups Muter (rgthree), CLIPTextEncode, DualCLIPLoader, Image Comparer (rgthree), SamplerCustomAdvanced, Image Comparer (rgthree), LoadImage, UNETLoader, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 7, "checkpoint": "Flux Fill dev - fp8_黑森林官方重绘模型_fp8_e4m3fn", "denoise": 0.35000000000000003, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 374688777498207, "steps": 60}
---

# 图片生成/图生图/图生图-FLUX 1.5（待优化）_1897229356450664449.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生图-FLUX 1.5（待优化）_1897229356450664449.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（52 个）：
- `VAELoader`
- `RandomNoise`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Florence2Run`
- `Florence2ModelLoader`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ttN concat`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `TextInputBasic`
- `ttN concat`
- `ShowText|pysssss`
- `VAEEncode` ★核心
- `TextInputBasic`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `TextInputBasic`
- `LoadImage`
- `TextInputBasic`
- `WD14Tagger|pysssss`
- `ttN concat`
- `ttN concat`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `RandomNoise`
- `BasicGuider`
- `VAEDecode` ★核心
- `LoadImage`
- `Note`
- `BasicScheduler`
- `BasicScheduler`
- `Fast Groups Muter (rgthree)`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `374688777498207`
- `steps` = `60`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.35000000000000003`
- `checkpoint` = `Flux Fill dev - fp8_黑森林官方重绘模型_fp8_e4m3fn`

## 知识

覆盖率 **87%**（45/52）

**有卡**：`VAELoader`、`RandomNoise`、`VAEEncode`、`FluxGuidance`、`Florence2Run`、`Florence2ModelLoader`、`KSamplerSelect`、`BasicGuider`、`UNETLoader`、`DualCLIPLoader`、`ttN concat`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`TextInputBasic`、`KSampler`、`LoadImage`、`WD14Tagger|pysssss`、`VAEDecode`、`CheckpointLoaderSimple`、`BasicScheduler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
