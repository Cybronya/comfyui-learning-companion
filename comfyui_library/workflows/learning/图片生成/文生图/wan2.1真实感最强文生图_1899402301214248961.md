---
key: 图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json
name: wan2.1真实感最强文生图_1899402301214248961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json
hash: 3c429384431ec5c6
coverage: 0.681818
learned_at: 2026-10-10 20:59:27
nodes: [CLIPLoader, WanVideoNAG, easy clearCacheAll, easy cleanGpuUsed, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, VAELoader, KSampler, VAEDecode, SaveImage, FastFilmGrain, SaveImage, Note, Note, Note, EmptyHunyuanLatentVideo, Note, Note]
patterns: []
missing: [easy cleanGpuUsed, easy clearCacheAll]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 456153843732613, "steps": 10}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json`

## 结构

**节点**（22 个）：
- `CLIPLoader`
- `WanVideoNAG`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `VAELoader`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `FastFilmGrain`
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `EmptyHunyuanLatentVideo`
- `Note`
- `Note`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `456153843732613`
- `steps` = `10`

## 知识

覆盖率 **68%**（15/22）

**有卡**：`CLIPLoader`、`WanVideoNAG`、`easy clearCacheAll`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAELoader`、`KSampler`、`VAEDecode`、`SaveImage`、`FastFilmGrain`

**缺卡**（2）：`easy cleanGpuUsed`、`easy clearCacheAll`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
