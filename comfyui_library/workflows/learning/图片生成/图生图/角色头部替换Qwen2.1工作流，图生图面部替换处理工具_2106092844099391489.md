---
key: 角色头部替换Qwen2.1工作流，图生图面部替换处理工具_2106092844099391489.json
name: 角色头部替换Qwen2.1工作流，图生图面部替换处理工具_2106092844099391489
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色头部替换Qwen2.1工作流，图生图面部替换处理工具_2106092844099391489.json
hash: 5caac1b616a3667f
coverage: 0.784314
learned_at: 2026-10-10 21:22:54
nodes: [EmptyLatentImage, UNETLoader, CLIPLoader, KSampler, VAELoader, ResolutionSelector, llama_cpp_instruct_adv, llama_cpp_parameters, easy clearCacheAll, easy clearCacheAll, llama_cpp_model_loader, PreviewAny, LoadImage, QwenImage21Cache, SaveImage, LoadImage, VAEDecode, PreviewImage, easy imageConcat, JjkText, TextEncodeQwenImage21, PIP_图像联结, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [PIP_图像联结, easy clearCacheAll, easy clearCacheAll, easy imageConcat]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `PIP_图像联结` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 角色头部替换Qwen2.1工作流，图生图面部替换处理工具_2106092844099391489.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色头部替换Qwen2.1工作流，图生图面部替换处理工具_2106092844099391489.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `ResolutionSelector`
- `llama_cpp_instruct_adv`
- `llama_cpp_parameters`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `llama_cpp_model_loader`
- `PreviewAny`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `easy imageConcat`
- `JjkText`
- `TextEncodeQwenImage21`
- `PIP_图像联结`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **78%**（40/51）

**有卡**：`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`KSampler`、`VAELoader`、`ResolutionSelector`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`LoadImage`、`QwenImage21Cache`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（4）：`PIP_图像联结`、`easy clearCacheAll`、`easy clearCacheAll`、`easy imageConcat`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `PIP_图像联结` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
