---
name: text_to_image_video_lora_sampler_159
type: Text To Image
frequency: 4
level: strong
coverage: 0.84125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/电影感画面增强｜MiniMax H3文生图生视频处理_2093220651229335554.json, 视频生成/文生视频/电影感画面增强｜MiniMax H3文生视频视频重绘_2093065468214071297.json, 视频生成/文生视频/简单易用全能生成｜文生视频图生视频一站式工作流_2096713688211345409.json, 视频生成/文生视频/高质量文生图生视频｜MiNiMax H3视频生视频全能工作流_2093088546247757825.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/电影感画面增强｜MiniMax H3文生图生视频处理_2093220651229335554.json、视频生成/文生视频/电影感画面增强｜MiniMax H3文生视频视频重绘_2093065468214071297.json、视频生成/文生视频/简单易用全能生成｜文生视频图生视频一站式工作流_2096713688211345409.json、视频生成/文生视频/高质量文生图生视频｜MiNiMax H3视频生视频全能工作流_2093088546247757825.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `MiniMaxH3Unified` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `MiniMaxH3ReferenceToVideo` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `SolAttnMiniMax` —— 1/4 个有
- `VideoCombineV2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
