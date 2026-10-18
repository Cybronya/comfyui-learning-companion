---
key: 视频生成/图生视频/参考视频人物替换｜Qwen3.8反推提示词H3视频生成_2096280706988204034.json
name: 参考视频人物替换｜Qwen3.8反推提示词H3视频生成_2096280706988204034
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/参考视频人物替换｜Qwen3.8反推提示词H3视频生成_2096280706988204034.json
hash: 5e7089219e25876a
coverage: 0.866667
learned_at: 2026-10-17 01:10:24
nodes: [SaveImage, LoadImage, LoadImage, VAELoader, VAEDecode, VAEDecodeAudio, SplitSigmas, CLIPLoader, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, UNETLoader, ShellAgentPluginOutputText, BasicScheduler, BasicGuider, KSamplerSelect, VAELoader, easy showAnything, MiniMaxH3PromptEnhancerT8, BasicGuider, VAEDecode, VAEDecodeAudio, LoadVideo, PrimitiveFloat, MarkdownNote, MuyeTextEditOutput, ModelPreviewOverrideKJ, SamplerCustomAdvanced, MinimaxH3LatentUpscaler3D, LTXVConcatAVLatent, SamplerCustomAdvanced, VHS_VideoCombine, Label (rgthree), ComfyMathExpression, PreviewAny, MiniMaxH3ReferenceToVideo, ResolutionSelector, ImageResizeKJv2, PrimitiveStringMultiline, MarkdownNote, VHS_LoadVideo, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Float to Int, MiniMaxH3SigmaShift, ModelAttentionBackend, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/参考视频人物替换｜Qwen3.8反推提示词H3视频生成_2096280706988204034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/参考视频人物替换｜Qwen3.8反推提示词H3视频生成_2096280706988204034.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SplitSigmas`
- `CLIPLoader`
- `ManualSigmas`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `ShellAgentPluginOutputText`
- `BasicScheduler`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAELoader`
- `easy showAnything`
- `MiniMaxH3PromptEnhancerT8`
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LoadVideo`
- `PrimitiveFloat`
- `MarkdownNote`
- `MuyeTextEditOutput`
- `ModelPreviewOverrideKJ`
- `SamplerCustomAdvanced` ★核心
- `MinimaxH3LatentUpscaler3D`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Label (rgthree)`
- `ComfyMathExpression`
- `PreviewAny`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `VHS_LoadVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Float to Int`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **87%**（65/75）

**有卡**：`SaveImage`、`LoadImage`、`VAELoader`、`VAEDecode`、`VAEDecodeAudio`、`SplitSigmas`、`CLIPLoader`、`ManualSigmas`、`RandomNoise`、`LTXVSeparateAVLatent`、`UNETLoader`、`ShellAgentPluginOutputText`、`BasicScheduler`、`BasicGuider`、`KSamplerSelect`、`MiniMaxH3PromptEnhancerT8`、`LoadVideo`、`MuyeTextEditOutput`、`ModelPreviewOverrideKJ`、`SamplerCustomAdvanced`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`Label (rgthree)`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`、`ImageResizeKJv2`、`VHS_LoadVideo`、`Float to Int`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
