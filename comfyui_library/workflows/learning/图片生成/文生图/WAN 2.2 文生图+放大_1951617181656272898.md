---
key: 图片生成/文生图/WAN 2.2 文生图+放大_1951617181656272898.json
name: WAN 2.2 文生图+放大_1951617181656272898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN 2.2 文生图+放大_1951617181656272898.json
hash: 24e3a82eacb093d5
coverage: 0.833333
learned_at: 2026-10-10 20:59:13
nodes: [LoraLoaderModelOnly, UnetLoaderGGUF, CLIPLoader, VAELoader, CLIPTextEncode, SharkOptions_Beta, ClownOptions_SwapSampler_Beta, EmptyLatentImage, ClownOptions_DetailBoost_Beta, VAEDecode, PathchSageAttentionKJ, ClownsharKSampler_Beta, LatentUpscaleBy, PreviewImage, Image Sharpen FS, Image Comparer (rgthree), VAEDecodeTiled, SaveImage, ClownsharKSampler_Beta, LoraLoaderModelOnly, iToolsPromptRecord, easy promptConcat, CLIPTextEncode, iToolsPromptRecord]
patterns: []
missing: [Image Sharpen FS, easy promptConcat]
parameters: {"batch_size": 1, "cfg": 10, "denoise": 1.0000000000000002, "height": 1024, "sampler_name": -1, "scheduler": 0.6000000000000001, "seed": 0.5, "steps": "bong_tangent", "width": 1024}
discoveries: [次要节点 `Image Sharpen FS` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/WAN 2.2 文生图+放大_1951617181656272898.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN 2.2 文生图+放大_1951617181656272898.json`

## 结构

**节点**（24 个）：
- `LoraLoaderModelOnly`
- `UnetLoaderGGUF`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `SharkOptions_Beta`
- `ClownOptions_SwapSampler_Beta`
- `EmptyLatentImage`
- `ClownOptions_DetailBoost_Beta`
- `VAEDecode`
- `PathchSageAttentionKJ`
- `ClownsharKSampler_Beta`
- `LatentUpscaleBy`
- `PreviewImage`
- `Image Sharpen FS`
- `Image Comparer (rgthree)`
- `VAEDecodeTiled`
- `SaveImage`
- `ClownsharKSampler_Beta`
- `LoraLoaderModelOnly`
- `iToolsPromptRecord`
- `easy promptConcat`
- `CLIPTextEncode`
- `iToolsPromptRecord`

## 关键参数

- `batch_size` = `1`
- `cfg` = `10`
- `denoise` = `1.0000000000000002`
- `height` = `1024`
- `sampler_name` = `-1`
- `scheduler` = `0.6000000000000001`
- `seed` = `0.5`
- `steps` = `bong_tangent`
- `width` = `1024`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`SharkOptions_Beta`、`ClownOptions_SwapSampler_Beta`、`EmptyLatentImage`、`ClownOptions_DetailBoost_Beta`、`VAEDecode`、`PathchSageAttentionKJ`、`ClownsharKSampler_Beta`、`LatentUpscaleBy`、`PreviewImage`、`Image Sharpen FS`、`Image Comparer (rgthree)`、`VAEDecodeTiled`、`SaveImage`

**缺卡**（2）：`Image Sharpen FS`、`easy promptConcat`

## 学习发现

- 次要节点 `Image Sharpen FS` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
