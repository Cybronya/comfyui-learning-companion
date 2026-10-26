---
name: text_to_image_video_lora_sampler_132
type: Text To Image
frequency: 6
level: strong
coverage: 0.777333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/快速文生视频｜Fastvideo H3角色表演ComfyUI工作流_2095559517340790785.json, 视频生成/文生视频/文生图生视频全能参考三合一｜minimax阿里8步加速_2095811801366745089.json, 视频生成/文生视频/文生视频 MiniMax H3 可设时长分辨率比例快速出片_2094174814998192130.json, 视频生成/文生视频/文生视频直出｜MiniMax H3官方工作流高清生成_2090155730023305218.json, 视频生成/文生视频/新ref V1.0 Lora阿里8步版｜MiniMax H3多参考加速生成_2096684025057468417.json, 视频生成/文生视频/氛围感短视频生成｜H3文生视频光影情绪渲染_2096675059892047874.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_132

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/快速文生视频｜Fastvideo H3角色表演ComfyUI工作流_2095559517340790785.json、视频生成/文生视频/文生图生视频全能参考三合一｜minimax阿里8步加速_2095811801366745089.json、视频生成/文生视频/文生视频 MiniMax H3 可设时长分辨率比例快速出片_2094174814998192130.json、视频生成/文生视频/文生视频直出｜MiniMax H3官方工作流高清生成_2090155730023305218.json、视频生成/文生视频/新ref V1.0 Lora阿里8步版｜MiniMax H3多参考加速生成_2096684025057468417.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `MiniMaxH3ImageToVideo` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `LoadImage` —— 3/6 个有
- `MiniMaxH3ReferenceToVideo` —— 3/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `Text` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `ManualSigmas` —— 1/6 个有
- `MiniMaxH3AVDecodeT8` —— 1/6 个有
- `ModelPreviewOverrideKJ` —— 1/6 个有
- `RunningHub Deepcleaner` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `VHS_LoadVideoFFmpeg` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
