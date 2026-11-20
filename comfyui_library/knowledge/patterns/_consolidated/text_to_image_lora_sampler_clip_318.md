---
name: text_to_image_lora_sampler_clip_318
type: Text To Image
frequency: 7
level: strong
coverage: 0.896571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/lightx2v-Turbo-1.0+Realism-People-Lora｜MiniMax文生视频_2088131080607064066.json, 视频生成/文生视频/加速版超强文生视频｜MiniMax-H3人物类特效数字人工作流_2087232767292694530.json, 视频生成/文生视频/图生视频5秒1080p｜MiniMax-H3八分钟全节点注释_2090913102907920385.json, 视频生成/文生视频/官方提示词模板加持｜MiniMax H3 多图参考提速40%_2096274541071917057.json, 视频生成/文生视频/开源版文生视频｜MiniMax-H3提示词一键出片_2089012717008023553.json, 视频生成/文生视频/开源版文生视频｜MiniMax-H3纯文本生成视频开源工作流_2088773720985923585.json, 视频生成/文生视频/文生视频直出｜MiniMax H3高清一键生成_2089797615142658050.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_318

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/lightx2v-Turbo-1.0+Realism-People-Lora｜MiniMax文生视频_2088131080607064066.json、视频生成/文生视频/加速版超强文生视频｜MiniMax-H3人物类特效数字人工作流_2087232767292694530.json、视频生成/文生视频/图生视频5秒1080p｜MiniMax-H3八分钟全节点注释_2090913102907920385.json、视频生成/文生视频/官方提示词模板加持｜MiniMax H3 多图参考提速40%_2096274541071917057.json、视频生成/文生视频/开源版文生视频｜MiniMax-H3提示词一键出片_2089012717008023553.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `CR Text` —— 3/7 个有
- `EasyCache` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `LoadImage` —— 2/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/7 个有
- `VHS_VideoCombine` —— 2/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `Int` —— 1/7 个有
- `MiniMaxH3ReferenceToVideo` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `Text Find and Replace` —— 1/7 个有
- `TextOverlay` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
