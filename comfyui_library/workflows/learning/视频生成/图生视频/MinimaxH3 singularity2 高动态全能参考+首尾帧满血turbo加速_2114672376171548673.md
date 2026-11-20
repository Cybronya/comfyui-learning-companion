---
key: 视频生成/图生视频/MinimaxH3 singularity2 高动态全能参考+首尾帧满血turbo加速_2114672376171548673.json
name: MinimaxH3 singularity2 高动态全能参考+首尾帧满血turbo加速_2114672376171548673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3 singularity2 高动态全能参考+首尾帧满血turbo加速_2114672376171548673.json
hash: 8ad9d7d0cb5e62f8
coverage: 0.833333
learned_at: 2026-10-30 17:58:27
nodes: [VAEDecode, KSamplerSelect, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, CLIPLoader, VAELoader, ComfyMathExpression, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, PrimitiveFloat, VAEDecodeAudio, AnySwitch, ResolutionSelector, VAELoader, ComfySwitchNode, SaveVideo, BasicScheduler, PrimitiveBoolean, AnySwitch, UNETLoader, UNETLoader, Fast Bypasser (rgthree), PrimitiveStringMultiline, LoadImage, LoadImage, LoraLoaderModelOnly, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ComfySwitchNode, ComfySwitchNode, PrimitiveBoolean, FastGroupsBypassSwitch, Bool, Bool, ComfySwitchNode, Int, Int, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/MinimaxH3 singularity2 高动态全能参考+首尾帧满血turbo加速_2114672376171548673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3 singularity2 高动态全能参考+首尾帧满血turbo加速_2114672376171548673.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（42 个）：
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `VAEDecodeAudio` ★核心
- `AnySwitch`
- `ResolutionSelector`
- `VAELoader`
- `ComfySwitchNode`
- `SaveVideo`
- `BasicScheduler`
- `PrimitiveBoolean`
- `AnySwitch`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `FastGroupsBypassSwitch`
- `Bool`
- `Bool`
- `ComfySwitchNode`
- `Int`
- `Int`
- `VHS_LoadVideo`

## 知识

覆盖率 **83%**（35/42）

**有卡**：`VAEDecode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`MiniMaxH3ImageToVideo`、`MiniMaxH3ReferenceToVideo`、`VAEDecodeAudio`、`AnySwitch`、`ResolutionSelector`、`SaveVideo`、`BasicScheduler`、`PrimitiveBoolean`、`UNETLoader`、`Fast Bypasser (rgthree)`、`LoadImage`、`LoraLoaderModelOnly`、`FastGroupsBypassSwitch`、`Bool`、`Int`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
