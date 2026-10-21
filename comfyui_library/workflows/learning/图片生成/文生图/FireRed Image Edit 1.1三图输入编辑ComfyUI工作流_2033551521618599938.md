---
key: 图片生成/文生图/FireRed Image Edit 1.1三图输入编辑ComfyUI工作流_2033551521618599938.json
name: FireRed Image Edit 1.1三图输入编辑ComfyUI工作流_2033551521618599938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FireRed Image Edit 1.1三图输入编辑ComfyUI工作流_2033551521618599938.json
hash: 84f72cf9220cb525
coverage: 0.769231
learned_at: 2026-10-19 22:45:29
nodes: [Reroute, LoraLoaderModelOnly, Reroute, Reroute, Note, FluxKontextMultiReferenceLatentMethod, KSampler, CFGNorm, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEditPlus, EmptySD3LatentImage, ModelSamplingAuraFlow, Seed (rgthree), CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, LoadImage, LoadImage, Note, LoraLoaderModelOnly, LoadImage, Note, Textbox, UNETLoader, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 602596886192896, "steps": 12}
---

# 图片生成/文生图/FireRed Image Edit 1.1三图输入编辑ComfyUI工作流_2033551521618599938.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FireRed Image Edit 1.1三图输入编辑ComfyUI工作流_2033551521618599938.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `Note`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler` ★核心
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEditPlus`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `Seed (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LoadImage`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Note`
- `Textbox`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `602596886192896`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`LoraLoaderModelOnly`、`FluxKontextMultiReferenceLatentMethod`、`KSampler`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`Seed (rgthree)`、`CLIPLoader`、`VAELoader`、`LoadImage`、`Textbox`、`UNETLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
