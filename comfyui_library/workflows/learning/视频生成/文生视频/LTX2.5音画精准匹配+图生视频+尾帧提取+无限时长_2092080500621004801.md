---
key: 视频生成/文生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2092080500621004801.json
name: LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2092080500621004801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2092080500621004801.json
hash: 22b383bb105b4245
coverage: 0.819549
learned_at: 2026-10-15 22:45:18
nodes: [VAELoader, VAELoader, KSamplerSelect, RandomNoise, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, EmptyLTXVLatentVideo, LTXVLatentUpsampler, RandomNoise, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, LTXVImgToVideoInplace, LTXVConcatAVLatent, UNETLoader, CLIPLoader, LatentUpscaleModelLoader, ManualSigmas, LTXVAudioVAEDecode, LTXVConcatAVLatent, VAEDecodeTiled, MarkdownNote, MarkdownNote, CreateVideo, GetVideoComponents, ImageFromBatch+, MarkdownNote, MarkdownNote, CLIPVisionLoader, llama_cpp_model_loader, llama_cpp_parameters, ResizeImageMaskNode, SaveVideo, CLIPLoader, PreviewAny, ComfySwitchNode, CLIPTextEncode, RandomNoise, SamplerCustomAdvanced, LTXVEmptyLatentAudio, LTXVLatentUpsampler, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, ResolutionSelector, PrimitiveStringMultiline, LTXVPreprocess, TextGenerateLTX2Prompt, PreviewAny, UNETLoader, CLIPTextEncode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageSizeAndBatchSize, ComfyMathExpression, VAELoader, LatentUpscaleModelLoader, KSamplerSelect, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, ManualSigmas, PrimitiveBoolean, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVDualCFGGuider, CLIPLoader, VAELoader, PrimitiveInt, ResizeImageMaskNode, LTXVConditioning, PrimitiveInt, LTXVDualCFGGuider, LTXVConditioning, CLIPTextEncode, SaveVideo, CLIPLoader, CLIPLoader, PrimitiveInt, ComfySwitchNode, CLIPVisionEncode, CLIPVisionLoader, LTXVPreprocess, llama_cpp_parameters, llama_cpp_model_loader, ResolutionSelector, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVSeparateAVLatent, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, CLIPLoader, PreviewAny, CLIPTextEncode, TextGenerateLTX2Prompt, PreviewAny, PrimitiveBoolean, ComfyMathExpression, VHS_VideoCombine, MarkdownNote, CLIPLoader, PrimitiveBoolean, RIFE VFI, VHS_VideoCombine, 孤海注释, 孤海注释, LoadImage, CLIPVisionEncode, llama_cpp_instruct_adv, llama_cpp_instruct_adv, Fast Groups Muter (rgthree), LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2092080500621004801.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2092080500621004801.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（133 个）：
- `VAELoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `CreateVideo`
- `GetVideoComponents`
- `ImageFromBatch+`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPVisionLoader`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ResizeImageMaskNode`
- `SaveVideo`
- `CLIPLoader`
- `PreviewAny`
- `ComfySwitchNode`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageSizeAndBatchSize`
- `ComfyMathExpression`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `ManualSigmas`
- `PrimitiveBoolean`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `LTXVConditioning`
- `PrimitiveInt`
- `LTXVDualCFGGuider`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveInt`
- `ComfySwitchNode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LTXVPreprocess`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `ResolutionSelector`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CLIPLoader`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `MarkdownNote`
- `CLIPLoader`
- `PrimitiveBoolean`
- `RIFE VFI`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
- `LoadImage`
- `CLIPVisionEncode`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `Fast Groups Muter (rgthree)`
- `LoadVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（109/133）

**有卡**：`VAELoader`、`KSamplerSelect`、`RandomNoise`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`ManualSigmas`、`PrimitiveBoolean`、`LTXVConcatAVLatent`、`UNETLoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CreateVideo`、`GetVideoComponents`、`ImageFromBatch+`、`CLIPVisionLoader`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ResizeImageMaskNode`、`SaveVideo`、`CLIPTextEncode`、`ResolutionSelector`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`ComfyMathExpression`、`ImageSizeAndBatchSize`、`RIFE VFI`、`VHS_VideoCombine`、`LTXVConditioning`、`CLIPVisionEncode`、`LoadImage`、`llama_cpp_instruct_adv`、`LoadVideo`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
