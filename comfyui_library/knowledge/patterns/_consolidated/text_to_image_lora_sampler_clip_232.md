---
name: text_to_image_lora_sampler_clip_232
type: Text To Image
frequency: 9
level: strong
coverage: 0.882222
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMaxH3图生视频场景特效直出_2093415902871121922.json, 视频生成/文生视频/Minimax H3提速全节点注释｜8步增速图生视频视频生视频_2089374494271041537.json, 视频生成/文生视频/Minimax H3文生视频工作流｜高质量视频生成_2095259805958098946.json, 视频生成/文生视频/MinimaxH3文生视频4步LORA加速-文生视频工作流_2087387239872557058.json, 视频生成/文生视频/Minimax_h3超级加速文生视频｜角色一致表演流畅省币首选_2103681865688375297.json, 视频生成/文生视频/SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314.json, 视频生成/文生视频/SageAttention+LoRA双重加速｜MiniMax H3文生视频_2089404463130963970.json, 视频生成/文生视频/T2V文生视频直出｜MiniMax H3高清视频一键生成_2089822887556509698.json, 视频生成/文生视频/像素幻想Lab出品｜MiniMaxH3图生视频场景特效_2093741804817567745.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_232

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/MiniMaxH3图生视频场景特效直出_2093415902871121922.json、视频生成/文生视频/Minimax H3提速全节点注释｜8步增速图生视频视频生视频_2089374494271041537.json、视频生成/文生视频/Minimax H3文生视频工作流｜高质量视频生成_2095259805958098946.json、视频生成/文生视频/MinimaxH3文生视频4步LORA加速-文生视频工作流_2087387239872557058.json、视频生成/文生视频/Minimax_h3超级加速文生视频｜角色一致表演流畅省币首选_2103681865688375297.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 8/9 个有
- `KSamplerSelect` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `CreateVideo` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `VHS_VideoCombine` —— 4/9 个有
- `LoadImage` —— 3/9 个有
- `LoraLoaderBypassModelOnly` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `llama_cpp_instruct_adv` —— 2/9 个有
- `llama_cpp_model_loader` —— 2/9 个有
- `llama_cpp_parameters` —— 2/9 个有
- `DiffusionModelLoaderKJ` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `PainterVRAM` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `easy int` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
