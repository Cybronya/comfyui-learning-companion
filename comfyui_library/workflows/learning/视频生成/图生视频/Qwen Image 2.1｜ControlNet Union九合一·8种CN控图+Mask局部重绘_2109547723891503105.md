---
key: 视频生成/图生视频/Qwen Image 2.1｜ControlNet Union九合一·8种CN控图+Mask局部重绘_2109547723891503105.json
name: Qwen Image 2.1｜ControlNet Union九合一·8种CN控图+Mask局部重绘_2109547723891503105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1｜ControlNet Union九合一·8种CN控图+Mask局部重绘_2109547723891503105.json
hash: e97dfadf1c42a937
coverage: 0.867925
learned_at: 2026-10-18 00:23:45
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, QwenImage21UnionLoader, PreviewImage, AIO_Preprocessor, PreviewImage, VAEDecode, SaveImage, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, ImageScale, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, QwenImage21UnionLoader, JWString, PreviewImage, AIO_Preprocessor, PreviewImage, VAEDecode, RandomNoise, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, ImageScale, RHLLMChatNode, JWStringConcat, easy showAnything, TextEncodeQwenImage21, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, QwenImage21UnionLoader, JWString, PreviewImage, AIO_Preprocessor, PreviewImage, QwenImage21UnionApply, VAEDecode, SaveImage, RandomNoise, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, PreviewImage, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, ImageScale, RHLLMChatNode, JWStringConcat, easy showAnything, TextEncodeQwenImage21, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, QwenImage21UnionLoader, JWString, PreviewImage, AIO_Preprocessor, PreviewImage, QwenImage21UnionApply, VAEDecode, SaveImage, RandomNoise, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, PreviewImage, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, ImageScale, RHLLMChatNode, JWStringConcat, easy showAnything, TextEncodeQwenImage21, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, QwenImage21UnionLoader, JWString, PreviewImage, AIO_Preprocessor, PreviewImage, VAEDecode, SaveImage, RandomNoise, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, PreviewImage, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, ImageScale, RHLLMChatNode, JWStringConcat, easy showAnything, TextEncodeQwenImage21, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, QwenImage21UnionLoader, JWString, PreviewImage, AIO_Preprocessor, PreviewImage, VAEDecode, SaveImage, RandomNoise, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, PreviewImage, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, ImageScale, RHLLMChatNode, JWStringConcat, easy showAnything, TextEncodeQwenImage21, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, QwenImage21UnionLoader, JWString, PreviewImage, AIO_Preprocessor, PreviewImage, QwenImage21UnionApply, VAEDecode, SaveImage, RandomNoise, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, PreviewImage, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, ImageScale, RHLLMChatNode, JWStringConcat, easy showAnything, TextEncodeQwenImage21, QwenImage21UnionApply, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageScaleBy, ImageScale, ImageScaleBy, ImageScale, ImageScaleBy, ImageScale, ImageScaleBy, ImageScale, ImageScaleBy, ImageScale, ImageScaleBy, ImageScale, ImageScaleBy, ImageScale, SaveImage, easy showAnything, TextEncodeQwenImage21, RHLLMChatNode, JWString, JWStringConcat, EmptyLatentImage, EmptyLatentImage, EmptyLatentImage, EmptyLatentImage, EmptyLatentImage, EmptyLatentImage, EmptyLatentImage, CFGGuider, PreviewImage, QwenImage21UnionApply, PreviewImage, LoadImage, LoadImage, QwenImage21UnionApply, QwenImage21UnionApply, PreviewImage, PreviewImage, QwenImage21UnionApply, VAEDecode, SaveImage, CFGGuider, SamplerCustomAdvanced, PreviewImage, LoadImage, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, ImageScale, RHLLMChatNode, JWStringConcat, easy showAnything, TextEncodeQwenImage21, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, QwenImage21UnionLoader, JWString, RandomNoise, KSamplerSelect, ManualSigmas, EmptyLatentImage, ImageDesaturate+, PreviewImage, PreviewImage, VAEDecode, CFGGuider, SamplerCustomAdvanced, PreviewImage, GetImageSize, MathExpression|pysssss, MathExpression|pysssss, ImageScale, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, RandomNoise, KSamplerSelect, ManualSigmas, QwenImage21UnionLoader, MaskToImage, ImageScale, ImageToMask, EmptyLatentImage, ImageCompositeMasked, LoadImage, SaveImage, TextEncodeQwenImage21, QwenImage21UnionApply]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 2048, "width": 2048}
---

# 视频生成/图生视频/Qwen Image 2.1｜ControlNet Union九合一·8种CN控图+Mask局部重绘_2109547723891503105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1｜ControlNet Union九合一·8种CN控图+Mask局部重绘_2109547723891503105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（265 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21UnionLoader`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21UnionLoader`
- `JWString`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `VAEDecode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `RHLLMChatNode`
- `JWStringConcat`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21UnionLoader`
- `JWString`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `QwenImage21UnionApply`
- `VAEDecode` ★核心
- `SaveImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `RHLLMChatNode`
- `JWStringConcat`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21UnionLoader`
- `JWString`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `QwenImage21UnionApply`
- `VAEDecode` ★核心
- `SaveImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `RHLLMChatNode`
- `JWStringConcat`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21UnionLoader`
- `JWString`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `RHLLMChatNode`
- `JWStringConcat`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21UnionLoader`
- `JWString`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `RHLLMChatNode`
- `JWStringConcat`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21UnionLoader`
- `JWString`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `QwenImage21UnionApply`
- `VAEDecode` ★核心
- `SaveImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `RHLLMChatNode`
- `JWStringConcat`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `QwenImage21UnionApply`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageScaleBy`
- `ImageScale`
- `ImageScaleBy`
- `ImageScale`
- `ImageScaleBy`
- `ImageScale`
- `ImageScaleBy`
- `ImageScale`
- `ImageScaleBy`
- `ImageScale`
- `ImageScaleBy`
- `ImageScale`
- `ImageScaleBy`
- `ImageScale`
- `SaveImage`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `RHLLMChatNode`
- `JWString`
- `JWStringConcat`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `CFGGuider`
- `PreviewImage`
- `QwenImage21UnionApply`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21UnionApply`
- `QwenImage21UnionApply`
- `PreviewImage`
- `PreviewImage`
- `QwenImage21UnionApply`
- `VAEDecode` ★核心
- `SaveImage`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `LoadImage`
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `RHLLMChatNode`
- `JWStringConcat`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21UnionLoader`
- `JWString`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `EmptyLatentImage` ★核心
- `ImageDesaturate+`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `GetImageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageScale`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `QwenImage21UnionLoader`
- `MaskToImage`
- `ImageScale`
- `ImageToMask`
- `EmptyLatentImage` ★核心
- `ImageCompositeMasked`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `QwenImage21UnionApply`

## 关键参数

- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（230/265）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`QwenImage21UnionLoader`、`AIO_Preprocessor`、`VAEDecode`、`SaveImage`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`GetImageSize`、`MathExpression|pysssss`、`ImageScale`、`JWString`、`CFGGuider`、`RHLLMChatNode`、`JWStringConcat`、`TextEncodeQwenImage21`、`QwenImage21UnionApply`、`LoadImage`、`ImageScaleBy`、`EmptyLatentImage`、`ImageDesaturate+`、`MaskToImage`、`ImageToMask`、`ImageCompositeMasked`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
