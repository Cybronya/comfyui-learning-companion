---
key: 视频生成/图生视频/wan2.2-TI2V-5B-图生视频_1950069954751152129.json
name: wan2.2-TI2V-5B-图生视频_1950069954751152129.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950069954751152129.json
hash: 73001231fbcae24c
coverage: 0.842105
learned_at: 2026-10-15 22:30:52
nodes: [UNETLoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAELoader, VAEDecodeTiled, CreateVideo, MathExpression|pysssss, Fast Groups Bypasser (rgthree), CLIPLoader, SaveVideo, KSampler, Wan22ImageToVideoLatent, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, JjkText, DF_Integer, DF_Integer]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 563167498989147, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/wan2.2-TI2V-5B-图生视频_1950069954751152129.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950069954751152129.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `MathExpression|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `SaveVideo`
- `KSampler` ★核心
- `Wan22ImageToVideoLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `JjkText`
- `DF_Integer`
- `DF_Integer`

## 关键参数

- `seed` = `563167498989147`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`VAEDecodeTiled`、`CreateVideo`、`MathExpression|pysssss`、`CLIPLoader`、`SaveVideo`、`KSampler`、`Wan22ImageToVideoLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`DF_Integer`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled、Wan22ImageToVideoLatent

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
