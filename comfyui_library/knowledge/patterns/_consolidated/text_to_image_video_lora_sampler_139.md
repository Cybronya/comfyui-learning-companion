---
name: text_to_image_video_lora_sampler_139
type: Text To Image
frequency: 5
level: strong
coverage: 0.7074
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, JjkText, JoinStringMulti, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, PurgeVRAM_UTK, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, StringConcatenate, ToString, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3全能多参提示词优化｜4步加速文生视频图生视频_2089386017529880578.json, 视频生成/文生视频/MiniMax H3 全能参考_自动提示词_2085967794637729794.json, 视频生成/文生视频/MiniMaxH3加速版尾帧做参考｜4步加速 文生视频视频生视频快出片_2104097352675057665.json, 视频生成/文生视频/全能多参考｜H3 4步加速生视频 提示词自动优化 文生图生视频生_2089331197225820161.json, 视频生成/文生视频/尾帧参考4步加速 MiniMaxH3极速生视频省时方案_2104330470908579842.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_139

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/H3全能多参提示词优化｜4步加速文生视频图生视频_2089386017529880578.json、视频生成/文生视频/MiniMax H3 全能参考_自动提示词_2085967794637729794.json、视频生成/文生视频/MiniMaxH3加速版尾帧做参考｜4步加速 文生视频视频生视频快出片_2104097352675057665.json、视频生成/文生视频/全能多参考｜H3 4步加速生视频 提示词自动优化 文生图生视频生_2089331197225820161.json、视频生成/文生视频/尾帧参考4步加速 MiniMaxH3极速生视频省时方案_2104330470908579842.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `JjkText`
- `JoinStringMulti`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `StringConcatenate`
- `ToString`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有
- `BatchImagesNode` —— 3/5 个有
- `LoadVideo` —— 3/5 个有
- `GetLastFrameNode` —— 2/5 个有
- `ModelPreviewOverrideKJ` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `workflow>2` —— 2/5 个有
- `Label (rgthree)` —— 1/5 个有
- `SaveImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
