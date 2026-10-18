---
key: 视频生成/图生视频/MinimaxH3人物替换character swap_2109965862622031874.json
name: MinimaxH3人物替换character swap_2109965862622031874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3人物替换character swap_2109965862622031874.json
hash: 5d11527b3f7e359b
coverage: 0.735294
learned_at: 2026-10-18 00:23:41
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, ComfyMathExpression, MiniMaxH3ReferenceToVideo, PrimitiveInt, PrimitiveBoolean, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveFloat, ResolutionSelector, LoadVideo, GetVideoComponents, PreviewImage, QwenH3PromptLocal, AnySwitch, PreviewAny, PrimitiveStringMultiline, CreateVideo, LoadImage, SaveVideo, Fast Bypasser (rgthree), MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/MinimaxH3人物替换character swap_2109965862622031874.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3人物替换character swap_2109965862622031874.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（34 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoadVideo`
- `GetVideoComponents`
- `PreviewImage`
- `QwenH3PromptLocal`
- `AnySwitch`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `CreateVideo`
- `LoadImage`
- `SaveVideo`
- `Fast Bypasser (rgthree)`
- `MarkdownNote`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`ResolutionSelector`、`LoadVideo`、`GetVideoComponents`、`QwenH3PromptLocal`、`AnySwitch`、`CreateVideo`、`LoadImage`、`SaveVideo`、`Fast Bypasser (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
