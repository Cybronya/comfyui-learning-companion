---
key: 图片生成/文生图/Krea VS Dev vs Wan2.2_1950983043634896897.json
name: Krea VS Dev vs Wan2.2_1950983043634896897
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea VS Dev vs Wan2.2_1950983043634896897.json
hash: cdd4dd7bd82da1d5
coverage: 0.982456
learned_at: 2026-10-10 20:58:43
nodes: [ConditioningZeroOut, easy seed, EmptySD3LatentImage, TeaCache, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, JWInteger, JWInteger, LoraLoaderModelOnly, KSampler, Bjornulf_TextToStringAndSeed, KSampler, CLIPTextEncode, KSampler, VAEDecode, VAEDecode, VAEDecode, DF_Get_image_size, DualCLIPLoader, VAELoader, CLIPTextEncode, FluxGuidance, UNETLoader, RH_Captioner, KSampler, ConditioningZeroOut, CLIPTextEncode, FluxGuidance, UNETLoader, AddLabel, AddLabel, AddLabel, ImageConcatMulti, LoadImage, SaveImage, PDIMAGE_LongerSize, SaveImage, AddLabel, AddLabel, VAEDecode, KSampler, TeaCache, UNETLoader, SaveImage, EmptyLatentImage, SaveImage, SaveImage, PDIMAGE_LongerSize, ConditioningZeroOut, easy seed, EmptySD3LatentImage, TeaCache, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, JWInteger, JWInteger, LoraLoaderModelOnly, Bjornulf_TextToStringAndSeed, KSampler, CLIPTextEncode, KSampler, VAEDecode, VAEDecode, VAEDecode, DF_Get_image_size, DualCLIPLoader, VAELoader, CLIPTextEncode, FluxGuidance, UNETLoader, RH_Captioner, KSampler, ConditioningZeroOut, CLIPTextEncode, FluxGuidance, UNETLoader, AddLabel, AddLabel, AddLabel, PDIMAGE_LongerSize, SaveImage, AddLabel, AddLabel, VAEDecode, KSampler, TeaCache, UNETLoader, EmptyLatentImage, SaveImage, KSampler, LoadImage, SaveImage, SaveImage, SaveImage, PDIMAGE_LongerSize, ImageConcatMulti, ConditioningZeroOut, easy seed, EmptySD3LatentImage, TeaCache, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, JWInteger, JWInteger, LoraLoaderModelOnly, Bjornulf_TextToStringAndSeed, KSampler, CLIPTextEncode, KSampler, VAEDecode, VAEDecode, DF_Get_image_size, DualCLIPLoader, VAELoader, CLIPTextEncode, FluxGuidance, UNETLoader, RH_Captioner, KSampler, ConditioningZeroOut, FluxGuidance, UNETLoader, AddLabel, AddLabel, AddLabel, PDIMAGE_LongerSize, SaveImage, AddLabel, AddLabel, TeaCache, UNETLoader, EmptyLatentImage, KSampler, SaveImage, SaveImage, ImageConcatMulti, PDIMAGE_LongerSize, KSampler, VAEDecode, CLIPTextEncode, LoadImage, VAEDecode, SaveImage, SaveImage]
patterns: [text_to_image]
missing: [easy seed, easy seed, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 994236951360843, "steps": 30, "width": 512}
discoveries: [次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Krea VS Dev vs Wan2.2_1950983043634896897.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea VS Dev vs Wan2.2_1950983043634896897.json`

## 结构

**节点**（171 个）：
- `ConditioningZeroOut`
- `easy seed`
- `EmptySD3LatentImage`
- `TeaCache`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `VAELoader`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly`
- `KSampler`
- `Bjornulf_TextToStringAndSeed`
- `KSampler`
- `CLIPTextEncode`
- `KSampler`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `DF_Get_image_size`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `FluxGuidance`
- `UNETLoader`
- `RH_Captioner`
- `KSampler`
- `ConditioningZeroOut`
- `CLIPTextEncode`
- `FluxGuidance`
- `UNETLoader`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `LoadImage`
- `SaveImage`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `AddLabel`
- `AddLabel`
- `VAEDecode`
- `KSampler`
- `TeaCache`
- `UNETLoader`
- `SaveImage`
- `EmptyLatentImage`
- `SaveImage`
- `SaveImage`
- `PDIMAGE_LongerSize`
- `ConditioningZeroOut`
- `easy seed`
- `EmptySD3LatentImage`
- `TeaCache`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `VAELoader`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly`
- `Bjornulf_TextToStringAndSeed`
- `KSampler`
- `CLIPTextEncode`
- `KSampler`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `DF_Get_image_size`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `FluxGuidance`
- `UNETLoader`
- `RH_Captioner`
- `KSampler`
- `ConditioningZeroOut`
- `CLIPTextEncode`
- `FluxGuidance`
- `UNETLoader`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `AddLabel`
- `AddLabel`
- `VAEDecode`
- `KSampler`
- `TeaCache`
- `UNETLoader`
- `EmptyLatentImage`
- `SaveImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PDIMAGE_LongerSize`
- `ImageConcatMulti`
- `ConditioningZeroOut`
- `easy seed`
- `EmptySD3LatentImage`
- `TeaCache`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `VAELoader`
- `CLIPLoader`
- `JWInteger`
- `JWInteger`
- `LoraLoaderModelOnly`
- `Bjornulf_TextToStringAndSeed`
- `KSampler`
- `CLIPTextEncode`
- `KSampler`
- `VAEDecode`
- `VAEDecode`
- `DF_Get_image_size`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `FluxGuidance`
- `UNETLoader`
- `RH_Captioner`
- `KSampler`
- `ConditioningZeroOut`
- `FluxGuidance`
- `UNETLoader`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `AddLabel`
- `AddLabel`
- `TeaCache`
- `UNETLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SaveImage`
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `KSampler`
- `VAEDecode`
- `CLIPTextEncode`
- `LoadImage`
- `VAEDecode`
- `SaveImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `512`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `994236951360843`
- `steps` = `30`
- `width` = `512`

## 知识

覆盖率 **98%**（168/171）

**有卡**：`ConditioningZeroOut`、`easy seed`、`EmptySD3LatentImage`、`TeaCache`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`JWInteger`、`KSampler`、`Bjornulf_TextToStringAndSeed`、`VAEDecode`、`DF_Get_image_size`、`DualCLIPLoader`、`FluxGuidance`、`RH_Captioner`、`AddLabel`、`ImageConcatMulti`、`LoadImage`、`SaveImage`、`PDIMAGE_LongerSize`、`EmptyLatentImage`

**缺卡**（3）：`easy seed`、`easy seed`、`easy seed`

## 学习发现

- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
