---
name: unknown_workflow_video_lora_sampler_130
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.896231
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/（自编排-Confucius4-R2T2）MiniMax H3数字人加速版V1_2104777855577186305.json, 视频生成/图生视频/（自编排数字人音频MV-Confucius4-R2T2）MiniMax H3数字人加速_2105353404636811266.json, 视频生成/图生视频/（音频驱动-10Eros-Max Beta3）MiniMax H3数字人加速版V1_2092497551713980417.json, 视频生成/图生视频/（音频驱动-Dasiwa V1）MiniMax H3数字人加速版V1_2092541511882854402.json, 视频生成/图生视频/（音频驱动-Remix V1）MiniMax H3数字人加速版V1_2092542937363214338.json, 视频生成/图生视频/（音频驱动-zs05）MiniMax H3数字人加速版V1_2092541557630136322.json, 视频生成/图生视频/（音频驱动-音乐MV-数字人）MiniMax H3加速_2105347148022894593.json, 视频生成/图生视频/（音频驱动-音乐MV）MiniMax H3数字人加速版V1_2099766391334330369.json, 视频生成/图生视频/（音频驱动-音乐MV）MiniMax H3数字人加速版V1_2099827196100694018.json, 视频生成/图生视频/（音频驱动-音乐MV）MiniMax H3数字人加速版V1_2099845520981323778.json, 视频生成/图生视频/（音频驱动-音乐MV）MiniMax H3数字人加速版V1_2104909753217536002.json, 视频生成/图生视频/（音频驱动-音乐MV）MiniMax H3数字人加速版_2099850720488017921.json, 视频生成/文生视频/(双时钟-8步高质量极速)Minimax文生视频V2（600步新加速LORA）_2087936438015975426.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_130

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/（自编排-Confucius4-R2T2）MiniMax H3数字人加速版V1_2104777855577186305.json、视频生成/图生视频/（自编排数字人音频MV-Confucius4-R2T2）MiniMax H3数字人加速_2105353404636811266.json、视频生成/图生视频/（音频驱动-10Eros-Max Beta3）MiniMax H3数字人加速版V1_2092497551713980417.json、视频生成/图生视频/（音频驱动-Dasiwa V1）MiniMax H3数字人加速版V1_2092541511882854402.json、视频生成/图生视频/（音频驱动-Remix V1）MiniMax H3数字人加速版V1_2092542937363214338.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 12/13 个有
- `LoadImage` —— 12/13 个有
- `SolAttnMiniMax` —— 12/13 个有
- `Float to Int` —— 2/13 个有
- `MiniMaxH3PromptEnhancerT8` —— 2/13 个有
- `R2T2GGUFLoader` —— 2/13 个有
- `R2T2Transcribe` —— 2/13 个有
- `StringConcatenate` —— 2/13 个有
- `T8PerformanceDirectorConfig` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `easy showAnything` —— 2/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
