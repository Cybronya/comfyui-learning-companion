---
key: 视频生成/图生视频/MiniMax H3 Super Acceleration二阶段超级加速（仅适合文戏）_2093866023492603906.json
name: MiniMax H3 Super Acceleration二阶段超级加速（仅适合文戏）_2093866023492603906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Super Acceleration二阶段超级加速（仅适合文戏）_2093866023492603906.json
hash: 03d847445bb7ca7e
coverage: 0.962963
learned_at: 2026-10-16 23:42:14
nodes: [CLIPLoader, VAELoader, BasicGuider, RandomNoise, MarkdownNote, ComfyMathExpression, MiniMaxH3DualClockSamplerT8, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoaderBypassModelOnly, ModelAttentionBackend, SolAttnMiniMax, ResolutionSelector, UNETLoader, LoraLoaderBypassModelOnly, SamplerCustomAdvanced, MiniMaxH3SolEngineDraftToLTXT8Advanced, VAEEncode, LatentUpscaleModelLoader, LTXVLatentUpsampler, UNETLoader, LoraLoaderModelOnly, RandomNoise, MiniMaxH3SolEngineTAEHVDecodeT8Advanced, MiniMaxH3OutputTrimT8, CreateVideo, SaveVideo, LTXVConditioning, MiniMaxH3AVDecodeT8, CreateVideo, GetVideoComponents, CLIPTextEncode, PrimitiveFloat, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Prompt Text, VAELoader, MiniMaxH3SolEngineTAEHVLoaderT8Advanced, CFGGuider, MiniMaxH3SolEngineLTXIdentityRefinerSetupT8Advanced, VHS_VideoCombine, ConcatTextOfUtils, SamplerCustomAdvanced]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 Super Acceleration二阶段超级加速（仅适合文戏）_2093866023492603906.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Super Acceleration二阶段超级加速（仅适合文戏）_2093866023492603906.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Output → Other

**节点**（54 个）：
- `CLIPLoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `MarkdownNote`
- `ComfyMathExpression`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderBypassModelOnly` ★核心
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3SolEngineDraftToLTXT8Advanced`
- `VAEEncode` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `MiniMaxH3SolEngineTAEHVDecodeT8Advanced`
- `MiniMaxH3OutputTrimT8`
- `CreateVideo`
- `SaveVideo`
- `LTXVConditioning`
- `MiniMaxH3AVDecodeT8`
- `CreateVideo`
- `GetVideoComponents`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `VAELoader`
- `MiniMaxH3SolEngineTAEHVLoaderT8Advanced`
- `CFGGuider`
- `MiniMaxH3SolEngineLTXIdentityRefinerSetupT8Advanced`
- `VHS_VideoCombine`
- `ConcatTextOfUtils`
- `SamplerCustomAdvanced` ★核心

## 知识

覆盖率 **96%**（52/54）

**有卡**：`CLIPLoader`、`VAELoader`、`BasicGuider`、`RandomNoise`、`ComfyMathExpression`、`MiniMaxH3DualClockSamplerT8`、`LoadImage`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AudioConditioningT8`、`LoraLoaderBypassModelOnly`、`ModelAttentionBackend`、`SolAttnMiniMax`、`ResolutionSelector`、`UNETLoader`、`SamplerCustomAdvanced`、`MiniMaxH3SolEngineDraftToLTXT8Advanced`、`VAEEncode`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`MiniMaxH3SolEngineTAEHVDecodeT8Advanced`、`MiniMaxH3OutputTrimT8`、`CreateVideo`、`SaveVideo`、`LTXVConditioning`、`MiniMaxH3AVDecodeT8`、`GetVideoComponents`、`CLIPTextEncode`、`CR Prompt Text`、`MiniMaxH3SolEngineTAEHVLoaderT8Advanced`、`CFGGuider`、`MiniMaxH3SolEngineLTXIdentityRefinerSetupT8Advanced`、`VHS_VideoCombine`、`ConcatTextOfUtils`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、CFGGuider
