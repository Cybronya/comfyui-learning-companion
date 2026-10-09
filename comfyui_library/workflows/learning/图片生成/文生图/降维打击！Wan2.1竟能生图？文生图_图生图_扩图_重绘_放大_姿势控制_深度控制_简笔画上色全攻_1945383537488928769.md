---
key: 图片生成/文生图/降维打击！Wan2.1竟能生图？文生图_图生图_扩图_重绘_放大_姿势控制_深度控制_简笔画上色全攻_1945383537488928769.json
name: 降维打击！Wan2.1竟能生图？文生图_图生图_扩图_重绘_放大_姿势控制_深度控制_简笔画上色全攻_1945383537488928769.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/降维打击！Wan2.1竟能生图？文生图_图生图_扩图_重绘_放大_姿势控制_深度控制_简笔画上色全攻_1945383537488928769.json
hash: 742497544022b207
coverage: 0.927536
learned_at: 2026-10-07 22:52:39
nodes: [VAEDecode, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, VAEDecode, ModelSamplingSD3, PreviewImage, SaveImage, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, PreviewImage, UNETLoader, TrimVideoLatent, VAEDecode, CLIPLoader, EmptyHunyuanLatentVideo, SaveImage, PreviewImage, VAELoader, VAEEncode, CLIPTextEncode, KSampler, VAELoader, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, KSampler, LoadImage, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, LoadImage, CLIPTextEncode, ImagePadForOutpaint, WanVaceToVideo, RepeatImageBatch, CLIPLoader, UNETLoader, VAELoader, KSampler, CLIPTextEncode, PreviewImage, TrimVideoLatent, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, WanVaceToVideo, RepeatImageBatch, LoadImage, CLIPTextEncode, LoadImage, CLIPLoader, UNETLoader, VAELoader, KSampler, CLIPTextEncode, PreviewImage, TrimVideoLatent, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, RepeatImageBatch, CLIPLoader, UNETLoader, VAELoader, KSampler, CLIPTextEncode, TrimVideoLatent, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, LoadImage, CLIPTextEncode, WanVaceToVideo, LoadImage, CLIPTextEncode, RepeatImageBatch, WanVaceToVideo, GetImageRangeFromBatch, CLIPLoader, UNETLoader, VAELoader, KSampler, CLIPTextEncode, TrimVideoLatent, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, GetImageRangeFromBatch, LoadImage, WanVaceToVideo, RepeatImageBatch, CLIPTextEncode, CLIPLoader, UNETLoader, VAELoader, KSampler, TrimVideoLatent, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, GetImageRangeFromBatch, WanVaceToVideo, RepeatImageBatch, LoadImage, CLIPTextEncode, CLIPTextEncode, AIO_Preprocessor, AIO_Preprocessor, SaveImage, PreviewImage, SaveImage, PreviewImage, LoadImage, AIO_Preprocessor, SaveImage, PreviewImage, Fast Groups Bypasser (rgthree), Label (rgthree)]
patterns: [image_to_image]
missing: [Label (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666, "steps": 6}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/降维打击！Wan2.1竟能生图？文生图_图生图_扩图_重绘_放大_姿势控制_深度控制_简笔画上色全攻_1945383537488928769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1945383537488928769.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（138 个）：
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `SaveImage`
- `PreviewImage`
- `VAELoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `KSampler` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImagePadForOutpaint`
- `WanVaceToVideo`
- `RepeatImageBatch`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SaveImage`
- `WanVaceToVideo`
- `RepeatImageBatch`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SaveImage`
- `RepeatImageBatch`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `RepeatImageBatch`
- `WanVaceToVideo`
- `GetImageRangeFromBatch`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SaveImage`
- `GetImageRangeFromBatch`
- `LoadImage`
- `WanVaceToVideo`
- `RepeatImageBatch`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SaveImage`
- `GetImageRangeFromBatch`
- `WanVaceToVideo`
- `RepeatImageBatch`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `AIO_Preprocessor`
- `SaveImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `666`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（128/138）

**有卡**：`VAEDecode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`SaveImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`KSampler`、`CLIPTextEncode`、`TrimVideoLatent`、`EmptyHunyuanLatentVideo`、`VAEEncode`、`ImageResizeKJv2`、`LoadImage`、`ImagePadForOutpaint`、`WanVaceToVideo`、`RepeatImageBatch`、`GetImageRangeFromBatch`、`AIO_Preprocessor`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 7 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
