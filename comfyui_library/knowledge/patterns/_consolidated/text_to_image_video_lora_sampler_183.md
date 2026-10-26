---
name: text_to_image_video_lora_sampler_183
type: Text To Image
frequency: 3
level: strong
coverage: 0.560667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, StringConcatenate, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2109368887719587842.json, 视频生成/文生视频/MiniMax-H3 全栈式短剧 V1.0｜多图音频参考二采优化_2096882058416189442.json, 视频生成/文生视频/全能多参考｜H3 4步加速生视频 提示词自动优化 文生图生视频生_2089331197225820161.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_183

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2109368887719587842.json、视频生成/文生视频/MiniMax-H3 全栈式短剧 V1.0｜多图音频参考二采优化_2096882058416189442.json、视频生成/文生视频/全能多参考｜H3 4步加速生视频 提示词自动优化 文生图生视频生_2089331197225820161.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `GetImage` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `JoinStringMulti` —— 2/3 个有
- `LTXVConcatAVLatent` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `MinimaxH3LatentUpscaler3D` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `PurgeVRAM_UTK` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `SplitSigmas` —— 2/3 个有
- `TextGenerate` —— 2/3 个有
- `ToString` —— 2/3 个有
- `YUAN_TXTJsonExtractor` —— 2/3 个有
- `YUAN_TXTParagraphSplitter` —— 2/3 个有
- `YUAN_TXTShotReplace` —— 2/3 个有
- `YuanAudioList` —— 2/3 个有
- `YuanAudioSplit` —— 2/3 个有
- `YuanMultiImage` —— 2/3 个有
- `YuanTool` —— 2/3 个有
- `easy float` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `BatchImagesNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `SaveImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
