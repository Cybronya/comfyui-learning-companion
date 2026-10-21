---
name: text_to_image_lora_sampler_clip_276
type: Text To Image
frequency: 4
level: strong
coverage: 0.82975
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/3合1集合工作流多模态视频生成首尾帧视频文生视频开源版MiniMax_2087435183631986689.json, 视频生成/文生视频/MiniMax H3海螺模型9种SKILL文生视频图生视频生成_2088191082780778497.json, 视频生成/文生视频/MiniMax H3海螺模型9种SKILL视频生成处理工作流_2101003222906400770.json, 视频生成/文生视频/文生视频首尾帧控制 MiniMax H3开源版多模态3合1集合工作流_2104829423152357378.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_276

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/3合1集合工作流多模态视频生成首尾帧视频文生视频开源版MiniMax_2087435183631986689.json、视频生成/文生视频/MiniMax H3海螺模型9种SKILL文生视频图生视频生成_2088191082780778497.json、视频生成/文生视频/MiniMax H3海螺模型9种SKILL视频生成处理工作流_2101003222906400770.json、视频生成/文生视频/文生视频首尾帧控制 MiniMax H3开源版多模态3合1集合工作流_2104829423152357378.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `ComfyMathExpression` —— 2/4 个有
- `CreateVideo` —— 2/4 个有
- `Fast Muter (rgthree)` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `MiniMaxChunkFeedForward` —— 2/4 个有
- `MiniMaxH3AVDecodeT8` —— 2/4 个有
- `MiniMaxLowVRAMAttention` —— 2/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `VAEDecodeAudio` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `PixaromaLabel` —— 1/4 个有
- `PixaromaResolution` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
