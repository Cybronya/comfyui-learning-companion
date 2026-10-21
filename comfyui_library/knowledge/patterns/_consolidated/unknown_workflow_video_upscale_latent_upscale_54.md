---
name: unknown_workflow_video_upscale_latent_upscale_54
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.693857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 Easy 工作台+双采样+提示词增强_2096870281045434370.json, 视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2098217190175629314.json, 视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2105565512574001153.json, 视频生成/图生视频/H3最强去油+双采样+提示词全自动优化_2096561381649772545.json, 视频生成/图生视频/MINIMAX-H3开源 最强去油全模式精简流+独立双采样_2095453807462412289.json, 视频生成/图生视频/MINIMAX-H3开源 最强去油全模式精简流+独立双采样_2095464911093714946.json, 视频生成/图生视频/电商带货版 + H3 多参2采 + Qwen3.8提示词优化版_2105732568514650113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_54

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3 Easy 工作台+双采样+提示词增强_2096870281045434370.json、视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2098217190175629314.json、视频生成/图生视频/H3 多参2采 + Qwen3.8提示词优化版_2105565512574001153.json、视频生成/图生视频/H3最强去油+双采样+提示词全自动优化_2096561381649772545.json、视频生成/图生视频/MINIMAX-H3开源 最强去油全模式精简流+独立双采样_2095453807462412289.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `CR Prompt Text` —— 5/7 个有
- `MiniMaxH3PromptEnhancerT8` —— 5/7 个有
- `PreviewAny` —— 5/7 个有
- `RH_Translator` —— 5/7 个有
- `easy saveText` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `H3SigmaRefiner` —— 4/7 个有
- `MiniMaxH3Easy` —— 4/7 个有
- `MiniMaxH3EasyModelAdapter` —— 4/7 个有
- `MiniMaxH3EasyOutput` —— 4/7 个有
- `MiniMaxH3EasySecondPassConditioning` —— 4/7 个有
- `ComfyMathExpression` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `Label (rgthree)` —— 3/7 个有
- `MiniMaxH3ReferenceToVideo` —— 3/7 个有
- `PrimitiveFloat` —— 3/7 个有
- `ResolutionSelector` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `easy float` —— 3/7 个有
- `忽略多组孤海` —— 3/7 个有
- `Int` —— 2/7 个有
- `easy indexTTSForceCleanup` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
