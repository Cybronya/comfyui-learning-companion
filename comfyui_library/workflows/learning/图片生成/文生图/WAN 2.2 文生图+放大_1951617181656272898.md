---
key: 图片生成/文生图/WAN 2.2 文生图+放大_1951617181656272898.json
name: WAN 2.2 文生图+放大_1951617181656272898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN 2.2 文生图+放大_1951617181656272898.json
hash: 24e3a82eacb093d5
coverage: 0.916667
learned_at: 2026-10-15 22:27:34
nodes: [LoraLoaderModelOnly, UnetLoaderGGUF, CLIPLoader, VAELoader, CLIPTextEncode, SharkOptions_Beta, ClownOptions_SwapSampler_Beta, EmptyLatentImage, ClownOptions_DetailBoost_Beta, VAEDecode, PathchSageAttentionKJ, ClownsharKSampler_Beta, LatentUpscaleBy, PreviewImage, Image Sharpen FS, Image Comparer (rgthree), VAEDecodeTiled, SaveImage, ClownsharKSampler_Beta, LoraLoaderModelOnly, iToolsPromptRecord, easy promptConcat, CLIPTextEncode, iToolsPromptRecord]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": 1.0000000000000002, "height": 1024, "sampler_name": -1, "scheduler": 0.6000000000000001, "seed": 0.5, "steps": "bong_tangent", "width": 1024}
---

# 图片生成/文生图/WAN 2.2 文生图+放大_1951617181656272898.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN 2.2 文生图+放大_1951617181656272898.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SharkOptions_Beta`
- `ClownOptions_SwapSampler_Beta` ★核心
- `EmptyLatentImage` ★核心
- `ClownOptions_DetailBoost_Beta`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `ClownsharKSampler_Beta` ★核心
- `LatentUpscaleBy`
- `PreviewImage`
- `Image Sharpen FS`
- `Image Comparer (rgthree)`
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `ClownsharKSampler_Beta` ★核心
- `LoraLoaderModelOnly` ★核心
- `iToolsPromptRecord`
- `easy promptConcat`
- `CLIPTextEncode` ★核心
- `iToolsPromptRecord`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `10`
- `sampler_name` = `-1`
- `scheduler` = `0.6000000000000001`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`SharkOptions_Beta`、`ClownOptions_SwapSampler_Beta`、`EmptyLatentImage`、`ClownOptions_DetailBoost_Beta`、`VAEDecode`、`PathchSageAttentionKJ`、`ClownsharKSampler_Beta`、`LatentUpscaleBy`、`Image Sharpen FS`、`VAEDecodeTiled`、`SaveImage`、`iToolsPromptRecord`、`easy promptConcat`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ClownsharKSampler_Beta、ClownOptions_SwapSampler_Beta
