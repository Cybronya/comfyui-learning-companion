---
name: text_to_image_lora_sampler_clip_330
type: Text To Image
frequency: 6
level: strong
coverage: 0.883667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/lightx2v-Turbo-1.0+Realism-People-Lora｜MiniMax文生视频_2088131080607064066.json, 视频生成/文生视频/加速版超强文生视频｜MiniMax-H3人物类特效数字人工作流_2087232767292694530.json, 视频生成/文生视频/双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866.json, 视频生成/文生视频/官方提示词模板加持｜MiniMax H3 多图参考提速40%_2096274541071917057.json, 视频生成/文生视频/文生视频基础流｜Minimax_h3一键生成_2093223576789938178.json, 视频生成/文生视频/文生视频直出｜Minimax H3基础模型高质量生成_2093066954859966466.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_330

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/lightx2v-Turbo-1.0+Realism-People-Lora｜MiniMax文生视频_2088131080607064066.json、视频生成/文生视频/加速版超强文生视频｜MiniMax-H3人物类特效数字人工作流_2087232767292694530.json、视频生成/文生视频/双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866.json、视频生成/文生视频/官方提示词模板加持｜MiniMax H3 多图参考提速40%_2096274541071917057.json、视频生成/文生视频/文生视频基础流｜Minimax_h3一键生成_2093223576789938178.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

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
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 5/6 个有
- `CreateVideo` —— 4/6 个有
- `EasyCache` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `MiniMaxChunkFeedForward` —— 2/6 个有
- `MiniMaxLowVRAMAttention` —— 2/6 个有
- `PainterVRAM` —— 2/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `LoraLoaderBypassModelOnly` —— 1/6 个有
- `MiniMaxH3ReferenceToVideo` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `Text Find and Replace` —— 1/6 个有
- `TextOverlay` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

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
