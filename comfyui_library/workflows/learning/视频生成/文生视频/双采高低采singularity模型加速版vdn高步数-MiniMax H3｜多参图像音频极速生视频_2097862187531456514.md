---
key: 视频生成/文生视频/双采高低采singularity模型加速版vdn高步数-MiniMax H3｜多参图像音频极速生视频_2097862187531456514.json
name: 双采高低采singularity模型加速版vdn高步数-MiniMax H3｜多参图像音频极速生视频_2097862187531456514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/双采高低采singularity模型加速版vdn高步数-MiniMax H3｜多参图像音频极速生视频_2097862187531456514.json
hash: 54d875a7ba7e75e8
coverage: 0.835443
learned_at: 2026-10-11 21:41:57
nodes: [DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, MarkdownNote, ShowAnything|Mie, ShowAnything|Mie, GetVideoComponents, LoadVideo, LoadVideo, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio, LoadAudio, LoadImage, Note, PrimitiveFloat, Note, CLIPLoader, EasyCache, ModelAttentionBackend, SolAttnMiniMax, MiniMaxH3VDNRuntimeAuditT8Advanced, Lora Loader Stack (rgthree), BasicGuider, VAELoader, VAELoader, LTXVSeparateAVLatent, MinimaxH3LatentUpscaler3D, LTXVConcatAVLatent, RandomNoise, VAEDecode, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, VAEDecodeAudio, DF_Int_to_Float, ImpactSwitch, DF_Int_to_Float, ImpactSwitch, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CreateVideo, SaveVideo, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, SamplerCustomAdvanced, SplitSigmas, ComfyMathExpression, CR Prompt Text, SeedVR2LoadVAEModel, ModelPreviewOverrideKJ, UNETLoader, BasicScheduler, KSamplerSelect, PrimitiveFloat, MarkdownNote, LoadVideo, GetVideoComponents, Fast Groups Bypasser (rgthree), ResolutionSelector, CreateVideo, SaveVideo, CreateVideo, SaveVideo, GetVideoComponents]
patterns: []
missing: [ShowAnything|Mie, ShowAnything|Mie, CR Prompt Text, Lora Loader Stack (rgthree)]
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/双采高低采singularity模型加速版vdn高步数-MiniMax H3｜多参图像音频极速生视频_2097862187531456514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/双采高低采singularity模型加速版vdn高步数-MiniMax H3｜多参图像音频极速生视频_2097862187531456514.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `MarkdownNote`
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `GetVideoComponents`
- `LoadVideo`
- `LoadVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `Note`
- `PrimitiveFloat`
- `Note`
- `CLIPLoader`
- `EasyCache`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `MiniMaxH3VDNRuntimeAuditT8Advanced`
- `Lora Loader Stack (rgthree)`
- `BasicGuider`
- `VAELoader`
- `VAELoader`
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `VAEDecode` ★核心
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `VAEDecodeAudio` ★核心
- `DF_Int_to_Float`
- `ImpactSwitch`
- `DF_Int_to_Float`
- `ImpactSwitch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CreateVideo`
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `SamplerCustomAdvanced` ★核心
- `SplitSigmas`
- `ComfyMathExpression`
- `CR Prompt Text`
- `SeedVR2LoadVAEModel`
- `ModelPreviewOverrideKJ`
- `UNETLoader` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `PrimitiveFloat`
- `MarkdownNote`
- `LoadVideo`
- `GetVideoComponents`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `CreateVideo`
- `SaveVideo`
- `CreateVideo`
- `SaveVideo`
- `GetVideoComponents`

## 知识

覆盖率 **84%**（66/79）

**有卡**：`DF_Int_to_Float`、`GetVideoComponents`、`LoadVideo`、`LoadImage`、`LoadAudio`、`CLIPLoader`、`EasyCache`、`ModelAttentionBackend`、`SolAttnMiniMax`、`MiniMaxH3VDNRuntimeAuditT8Advanced`、`BasicGuider`、`VAELoader`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`RandomNoise`、`VAEDecode`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`VAEDecodeAudio`、`CreateVideo`、`SaveVideo`、`SamplerCustomAdvanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`SplitSigmas`、`ComfyMathExpression`、`SeedVR2LoadVAEModel`、`ModelPreviewOverrideKJ`、`UNETLoader`、`BasicScheduler`、`KSamplerSelect`、`ResolutionSelector`

**缺卡**（4）：`ShowAnything|Mie`、`ShowAnything|Mie`、`CR Prompt Text`、`Lora Loader Stack (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
