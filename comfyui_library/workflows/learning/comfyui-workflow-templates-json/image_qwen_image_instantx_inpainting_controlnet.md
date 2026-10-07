---
key: comfyui-workflow-templates-json/image_qwen_image_instantx_inpainting_controlnet.json
name: image_qwen_image_instantx_inpainting_controlnet
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_instantx_inpainting_controlnet.json
hash: 1a0b3773fbe12a09
official: true
coverage: 0.770833
learned_at: 2026-10-07 21:36:02
nodes: [CLIPLoader, UNETLoader, CLIPTextEncode, ControlNetLoader, VAELoader, ModelSamplingAuraFlow, ControlNetInpaintingAliMamaApply, MarkdownNote, Note, VAEEncode, SetLatentNoiseMask, MaskPreview, MarkdownNote, CLIPLoader, UNETLoader, ControlNetLoader, ModelSamplingAuraFlow, ImageScaleToMaxDimension, LoraLoaderModelOnly, VAEDecode, ImageCompositeMasked, MaskPreview, PreviewImage, KSampler, MarkdownNote, LoadImage, MarkdownNote, CLIPTextEncode, ImagePadForOutpaint, cade3e30-0eb2-4fd2-bf6e-8518f3a96e0c, f93c215e-c393-460e-9534-ed2c3d8a652e, VAEEncode, ControlNetInpaintingAliMamaApply, VAELoader, 2a4b2cc0-db37-4302-a067-da392f38f06b, SaveImage, LoadImage, SaveImage, CLIPTextEncode, CLIPTextEncode, Note, LoraLoaderModelOnly, KSampler, SaveImage, SaveImage, MarkdownNote, VAEDecode, ImageCompositeMasked]
patterns: [image_to_image]
missing: [2a4b2cc0-db37-4302-a067-da392f38f06b, cade3e30-0eb2-4fd2-bf6e-8518f3a96e0c, f93c215e-c393-460e-9534-ed2c3d8a652e]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 134554158057228, "steps": 20}
discoveries: [次要节点 `2a4b2cc0-db37-4302-a067-da392f38f06b` 知识库中没有该节点类型的任何知识, 次要节点 `cade3e30-0eb2-4fd2-bf6e-8518f3a96e0c` 知识库中没有该节点类型的任何知识, 次要节点 `f93c215e-c393-460e-9534-ed2c3d8a652e` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# comfyui-workflow-templates-json/image_qwen_image_instantx_inpainting_controlnet.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_instantx_inpainting_controlnet.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `ControlNetInpaintingAliMamaApply`
- `MarkdownNote`
- `Note`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `MaskPreview`
- `MarkdownNote`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ControlNetLoader`
- `ModelSamplingAuraFlow`
- `ImageScaleToMaxDimension`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ImageCompositeMasked`
- `MaskPreview`
- `PreviewImage`
- `KSampler` ★核心
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `ImagePadForOutpaint`
- `cade3e30-0eb2-4fd2-bf6e-8518f3a96e0c`
- `f93c215e-c393-460e-9534-ed2c3d8a652e`
- `VAEEncode` ★核心
- `ControlNetInpaintingAliMamaApply`
- `VAELoader`
- `2a4b2cc0-db37-4302-a067-da392f38f06b`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `MarkdownNote`
- `VAEDecode` ★核心
- `ImageCompositeMasked`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `134554158057228`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（37/48）

**有卡**：`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`ControlNetLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`ControlNetInpaintingAliMamaApply`、`VAEEncode`、`SetLatentNoiseMask`、`MaskPreview`、`ImageScaleToMaxDimension`、`LoraLoaderModelOnly`、`VAEDecode`、`ImageCompositeMasked`、`KSampler`、`LoadImage`、`ImagePadForOutpaint`、`SaveImage`

**缺卡**（3）：`2a4b2cc0-db37-4302-a067-da392f38f06b`、`cade3e30-0eb2-4fd2-bf6e-8518f3a96e0c`、`f93c215e-c393-460e-9534-ed2c3d8a652e`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `2a4b2cc0-db37-4302-a067-da392f38f06b` 知识库中没有该节点类型的任何知识
- 次要节点 `cade3e30-0eb2-4fd2-bf6e-8518f3a96e0c` 知识库中没有该节点类型的任何知识
- 次要节点 `f93c215e-c393-460e-9534-ed2c3d8a652e` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
