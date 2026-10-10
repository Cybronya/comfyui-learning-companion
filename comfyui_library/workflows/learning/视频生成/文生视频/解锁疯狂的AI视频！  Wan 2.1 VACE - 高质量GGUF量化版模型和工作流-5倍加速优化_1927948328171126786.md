---
key: 视频生成/文生视频/解锁疯狂的AI视频！  Wan 2.1 VACE - 高质量GGUF量化版模型和工作流-5倍加速优化_1927948328171126786.json
name: 解锁疯狂的AI视频！  Wan 2.1 VACE - 高质量GGUF量化版模型和工作流-5倍加速优化_1927948328171126786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/解锁疯狂的AI视频！  Wan 2.1 VACE - 高质量GGUF量化版模型和工作流-5倍加速优化_1927948328171126786.json
hash: f4427791da8535e0
coverage: 0.449275
learned_at: 2026-10-10 23:13:58
nodes: [Note, Any Switch (rgthree), MarkdownNote, ModelPatchTorchSettings, PathchSageAttentionKJ, UnetLoaderGGUF, CLIPLoader, ClipLoaderGGUF, RH_Translator, Note, Note, easy textSwitch, CLIPTextEncode, CLIPTextEncode, SetNode, PrimitiveInt, Note, Note, ImageUpscaleWithModel, UpscaleModelLoader, RIFE VFI, RIFE VFI, SetNode, LoraLoaderVanilla, SaveAnimatedWEBP, VHS_VideoCombine, ModelSamplingSD3, easy clearCacheAll, easy cleanGpuUsed, GetNode, GetNode, easy clearCacheAll, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, WanVaceToVideo, easy clearCacheAll, easy clearCacheAll, KSampler, SetNode, GetNode, CR Text, VHS_LoadVideo, DisplayText_Zho, DisplayText_Zho, Note, Fast Groups Bypasser (rgthree), Note, VAELoader, VAEDecode, Note, Primitive integer [Crystools], TrimVideoLatent, RH_Captioner, LoadImage, Note, ImageResize+, VHS_VideoCombine, VHS_VideoCombine, DWPreprocessor, ImpactSwitch, VHS_VideoCombine, VRAM_Debug, VRAM_Debug, Note, ImageResize+, Note, Canny, MarkdownNote]
patterns: []
missing: [CR Text, Primitive integer [Crystools], RIFE VFI, RIFE VFI, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy textSwitch, ImageResize+, ImageResize+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan21_CausVid_14B_T2V_lora_rank32-1.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 859911411659251, "steps": 6, "strength_clip": 1, "strength_model": 1}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/解锁疯狂的AI视频！  Wan 2.1 VACE - 高质量GGUF量化版模型和工作流-5倍加速优化_1927948328171126786.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/解锁疯狂的AI视频！  Wan 2.1 VACE - 高质量GGUF量化版模型和工作流-5倍加速优化_1927948328171126786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `Note`
- `Any Switch (rgthree)`
- `MarkdownNote`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `ClipLoaderGGUF`
- `RH_Translator`
- `Note`
- `Note`
- `easy textSwitch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `PrimitiveInt`
- `Note`
- `Note`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `RIFE VFI`
- `RIFE VFI`
- `SetNode`
- `LoraLoaderVanilla` ★核心
- `SaveAnimatedWEBP`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `WanVaceToVideo`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `KSampler` ★核心
- `SetNode`
- `GetNode`
- `CR Text`
- `VHS_LoadVideo`
- `DisplayText_Zho`
- `DisplayText_Zho`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `Primitive integer [Crystools]`
- `TrimVideoLatent`
- `RH_Captioner`
- `LoadImage`
- `Note`
- `ImageResize+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `VRAM_Debug`
- `Note`
- `ImageResize+`
- `Note`
- `Canny`
- `MarkdownNote`

## 关键参数

- `lora_name` = `Wan21_CausVid_14B_T2V_lora_rank32-1.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `859911411659251`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **45%**（31/69）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`CLIPLoader`、`ClipLoaderGGUF`、`RH_Translator`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`LoraLoaderVanilla`、`SaveAnimatedWEBP`、`VHS_VideoCombine`、`ModelSamplingSD3`、`WanVaceToVideo`、`KSampler`、`VHS_LoadVideo`、`DisplayText_Zho`、`VAELoader`、`VAEDecode`、`TrimVideoLatent`、`RH_Captioner`、`LoadImage`、`DWPreprocessor`、`VRAM_Debug`、`Canny`

**缺卡**（15）：`CR Text`、`Primitive integer [Crystools]`、`RIFE VFI`、`RIFE VFI`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy textSwitch`、`ImageResize+`、`ImageResize+`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、Canny、TrimVideoLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
