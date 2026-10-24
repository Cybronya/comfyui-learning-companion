---
key: 图片生成/图生图/wan2.2分块重绘细化_1955621338107953154.json
name: wan2.2分块重绘细化_1955621338107953154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2分块重绘细化_1955621338107953154.json
hash: 188b54643cc77566
coverage: 0.916667
learned_at: 2026-10-23 11:46:03
nodes: [CLIPTextEncode, CLIPLoader, CLIPTextEncode, RH_Captioner, UNETLoader, easy float, LoraLoaderModelOnly, VAELoader, KSampler, ImageUpscaleWithModel, UpscaleModelLoader, ImageTile+, ImpactImageBatchToImageList, VAEEncodeTiled, ShowText|pysssss, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, LoadImage, VAEDecodeTiled, ImageListToBatch+, Image Comparer (rgthree), ImageUntile+, SaveImage]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 0.16, "sampler_name": "res_multistep", "scheduler": "kl_optimal", "seed": 743151249539862, "steps": 10}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/图生图/wan2.2分块重绘细化_1955621338107953154.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2分块重绘细化_1955621338107953154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `UNETLoader` ★核心
- `easy float`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSampler` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageTile+`
- `ImpactImageBatchToImageList`
- `VAEEncodeTiled` ★核心
- `ShowText|pysssss`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VAEDecodeTiled` ★核心
- `ImageListToBatch+`
- `Image Comparer (rgthree)`
- `ImageUntile+`
- `SaveImage`

## 关键参数

- `seed` = `743151249539862`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `kl_optimal`
- `denoise` = `0.16`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`RH_Captioner`、`UNETLoader`、`easy float`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageTile+`、`ImpactImageBatchToImageList`、`VAEEncodeTiled`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoadImage`、`VAEDecodeTiled`、`ImageListToBatch+`、`ImageUntile+`、`SaveImage`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
