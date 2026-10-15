---
key: 视频生成/文生视频/MiniMax H3｜Ref2VA 多参考+关键帧剧情控制｜Motion Lab 动作_2094644471542673409.json
name: MiniMax H3｜Ref2VA 多参考+关键帧剧情控制｜Motion Lab 动作_2094644471542673409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3｜Ref2VA 多参考+关键帧剧情控制｜Motion Lab 动作_2094644471542673409.json
hash: 5be1d49fe54a0b05
coverage: 0.827586
learned_at: 2026-10-15 22:46:11
nodes: [MarkdownNote, RandomNoise, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, MarkdownNote, UNETLoader, ModelAttentionBackend, SolAttnMiniMax, BasicGuider, SamplerCustomAdvanced, MarkdownNote, MiniMaxH3AVDecodeT8, LTXVSeparateAVLatent, H3JerkOracle, H3TimeSmear, VAEEncode, H3V2VInit, H3InjectSchedule, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, MarkdownNote, VAEEncode, MinimaxH3LatentUpscaler3D, LTXVConcatAVLatent, MiniMaxH3AudioConditioningT8, MiniMaxH3PDD8StepSetupT8Advanced, SplitSigmasDenoise, BasicGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecode, CreateVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, MarkdownNote, LoadVideo, Video Slice, GetVideoComponents, LoadAudio, TrimAudioDuration, ComfyMathExpression, MiniMaxH3AddGuide, ComfyMathExpression, MiniMaxH3AddGuide, H3ModeSwitch, H3ModeSwitch, H3ModeSwitch, H3ModeSwitch, PrimitiveInt, CreateVideo, H3ExactRecover, PrimitiveInt, PrimitiveInt, PrimitiveFloat, H3ModeSwitch, PrimitiveInt, SaveVideo, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, SaveVideo, PrimitiveInt, MiniMaxH3SigmaShift, MiniMaxH3PDD8StepSetupT8Advanced, CLIPLoader, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AudioConditioningT8, MiniMaxH3AddGuide]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3｜Ref2VA 多参考+关键帧剧情控制｜Motion Lab 动作_2094644471542673409.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3｜Ref2VA 多参考+关键帧剧情控制｜Motion Lab 动作_2094644471542673409.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `MarkdownNote`
- `RandomNoise`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `MiniMaxH3AVDecodeT8`
- `LTXVSeparateAVLatent`
- `H3JerkOracle`
- `H3TimeSmear`
- `VAEEncode` ★核心
- `H3V2VInit`
- `H3InjectSchedule`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `MarkdownNote`
- `VAEEncode` ★核心
- `MinimaxH3LatentUpscaler3D`
- `LTXVConcatAVLatent`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3PDD8StepSetupT8Advanced`
- `SplitSigmasDenoise`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `LoadVideo`
- `Video Slice`
- `GetVideoComponents`
- `LoadAudio`
- `TrimAudioDuration`
- `ComfyMathExpression`
- `MiniMaxH3AddGuide`
- `ComfyMathExpression`
- `MiniMaxH3AddGuide`
- `H3ModeSwitch`
- `H3ModeSwitch`
- `H3ModeSwitch`
- `H3ModeSwitch`
- `PrimitiveInt`
- `CreateVideo`
- `H3ExactRecover`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `H3ModeSwitch`
- `PrimitiveInt`
- `SaveVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `PrimitiveInt`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3PDD8StepSetupT8Advanced`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AddGuide`

## 知识

覆盖率 **83%**（72/87）

**有卡**：`RandomNoise`、`ComfyMathExpression`、`UNETLoader`、`ModelAttentionBackend`、`SolAttnMiniMax`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`LTXVSeparateAVLatent`、`H3JerkOracle`、`H3TimeSmear`、`VAEEncode`、`H3V2VInit`、`H3InjectSchedule`、`KSamplerSelect`、`VAEDecode`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3PDD8StepSetupT8Advanced`、`SplitSigmasDenoise`、`CreateVideo`、`LoadVideo`、`Video Slice`、`GetVideoComponents`、`LoadAudio`、`TrimAudioDuration`、`MiniMaxH3AddGuide`、`H3ModeSwitch`、`H3ExactRecover`、`SaveVideo`、`LoadImage`、`MiniMaxH3SigmaShift`、`CLIPLoader`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、SplitSigmasDenoise
