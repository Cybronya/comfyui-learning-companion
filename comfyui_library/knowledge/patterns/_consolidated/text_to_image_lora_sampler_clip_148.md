---
name: text_to_image_lora_sampler_clip_148
type: Text To Image
frequency: 7
level: strong
coverage: 0.876286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/文生视频直出｜MiniMax H3官方工作流高清生成_2090155730023305218.json, 视频生成/文生视频/文生视频直出｜MiniMax H3高清一键生成_2089797615142658050.json, 视频生成/文生视频/文生视频直出｜Minimax H3基础模型高质量生成_2093066954859966466.json, 视频生成/文生视频/文生视频｜MiniMax H3 SageAttention+LoRA 双重加速_2089249506813636609.json, 视频生成/文生视频/文生视频｜MiniMax H3 SageAttention+LoRA 双重加速刘神_2094117560072626177.json, 视频生成/文生视频/超级加速文生视频｜Minimax_h3角色一致性表演生成_2093781650823012354.json, 视频生成/文生视频/超级加速文生视频｜Minimax_h3角色表演一致性_2093447912754860034.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_148

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/文生视频直出｜MiniMax H3官方工作流高清生成_2090155730023305218.json、视频生成/文生视频/文生视频直出｜MiniMax H3高清一键生成_2089797615142658050.json、视频生成/文生视频/文生视频直出｜Minimax H3基础模型高质量生成_2093066954859966466.json、视频生成/文生视频/文生视频｜MiniMax H3 SageAttention+LoRA 双重加速_2089249506813636609.json、视频生成/文生视频/文生视频｜MiniMax H3 SageAttention+LoRA 双重加速刘神_2094117560072626177.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
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
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 6/7 个有
- `CR Text` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `PainterVRAM` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `LoraLoaderBypassModelOnly` —— 2/7 个有
- `EasyCache` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `MiniMaxChunkFeedForward` —— 1/7 个有
- `MiniMaxH3AVDecodeT8` —— 1/7 个有
- `MiniMaxLowVRAMAttention` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `RunningHub Deepcleaner` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
