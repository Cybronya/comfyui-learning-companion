---
key: Lisa生成器1.0【含8step+基础】_1985898941021659137.json
name: Lisa生成器1.0【含8step+基础】_1985898941021659137
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Lisa生成器1.0【含8step+基础】_1985898941021659137.json
hash: 557a44d679be9a47
coverage: 0.9375
learned_at: 2026-10-10 20:58:46
nodes: [CLIPLoader, VAELoader, ModelSamplingAuraFlow, EmptyLatentImage, VAEDecode, CFGNorm, KSampler, Power Lora Loader (rgthree), CLIPLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, VAEDecode, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, KSampler, Power Lora Loader (rgthree), CFGNorm, SaveImage, SaveImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, EmptyLatentImage, VAEDecode, UNETLoader, CFGNorm, SaveImage, EmptyLatentImage, Power Lora Loader (rgthree), CLIPLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, EmptyLatentImage, VAEDecode, UNETLoader, CFGNorm, SaveImage, KSampler, CLIPLoader, CLIPTextEncode, ModelSamplingAuraFlow, LoraLoaderModelOnly, VAEDecode, UNETLoader, Power Lora Loader (rgthree), CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, KSampler, VAELoader, CLIPTextEncode, EmptySD3LatentImage, SaveImage, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, KSampler, CLIPTextEncode, LoadImage]
patterns: [text_to_image]
missing: [Power Lora Loader (rgthree), Power Lora Loader (rgthree), Power Lora Loader (rgthree), Power Lora Loader (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 817349474416955, "steps": 14, "width": 768}
discoveries: [次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# Lisa生成器1.0【含8step+基础】_1985898941021659137.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Lisa生成器1.0【含8step+基础】_1985898941021659137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CFGNorm`
- `KSampler` ★核心
- `Power Lora Loader (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Power Lora Loader (rgthree)`
- `CFGNorm`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CFGNorm`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `Power Lora Loader (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CFGNorm`
- `SaveImage`
- `KSampler` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `Power Lora Loader (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `817349474416955`
- `steps` = `14`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **94%**（60/64）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`EmptyLatentImage`、`VAEDecode`、`CFGNorm`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`SaveImage`、`EmptySD3LatentImage`、`LoadImage`

**缺卡**（4）：`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 学习发现

- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
