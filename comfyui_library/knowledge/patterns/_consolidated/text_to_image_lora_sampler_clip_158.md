---
name: text_to_image_lora_sampler_clip_158
type: Text To Image
frequency: 11
level: strong
coverage: 0.844273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/R2V参考生视频加速版｜5060Ti 16G本地极速跑_2103045635455938561.json, 视频生成/图生视频/REF2V图生视频生成｜地表最强开源Minimax H3运镜_2096664623201218561.json, 视频生成/图生视频/h3参考生视频方案，图生视频多参考精准还原_2110861891965902849.json, 视频生成/图生视频/minimax_h3多图参考生视频｜图生视频高质量生成工作流_2097783512152760321.json, 视频生成/图生视频/三图版全能参考｜MiniMax H3图生视频一键生成_2094737971634335745.json, 视频生成/图生视频/全能参考图生视频美少女｜miniMAXH3视频生成工作流_2088145573164707841.json, 视频生成/图生视频/全能多参生视频自用版｜Minimax H3 人物场景类特效_2089349057071378433.json, 视频生成/图生视频/参考生视频玩法升级｜MiniMax H3 视频生视频双通道_2096253067581812737.json, 视频生成/图生视频/双图版全能参考｜MiniMax H3图生视频高质量生成_2094740772443738114.json, 视频生成/图生视频/地表最强开源 Minimax H3 REF2V｜角色一致性图生视频运镜_2096852990467592194.json, 视频生成/图生视频/多图参考直出｜MiniMax H3图生视频一致性生成_2090271687425220609.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_158

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/R2V参考生视频加速版｜5060Ti 16G本地极速跑_2103045635455938561.json、视频生成/图生视频/REF2V图生视频生成｜地表最强开源Minimax H3运镜_2096664623201218561.json、视频生成/图生视频/h3参考生视频方案，图生视频多参考精准还原_2110861891965902849.json、视频生成/图生视频/minimax_h3多图参考生视频｜图生视频高质量生成工作流_2097783512152760321.json、视频生成/图生视频/三图版全能参考｜MiniMax H3图生视频一键生成_2094737971634335745.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `PrimitiveFloat` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `PrimitiveInt` —— 8/11 个有
- `ComfySwitchNode` —— 7/11 个有
- `PrimitiveBoolean` —— 7/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/11 个有
- `SaveImage` —— 4/11 个有
- `LoadAudio` —— 3/11 个有
- `PathchSageAttentionKJ` —— 3/11 个有
- `EasyCache` —— 2/11 个有
- `ImpactSwitch` —— 2/11 个有
- `Int` —— 2/11 个有
- `TextBox` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `Fast Bypasser (rgthree)` —— 1/11 个有
- `Load Lora` —— 1/11 个有
- `MiniMaxH3AddGuide` —— 1/11 个有
- `MiniMaxH3QwenReferencePrefixCacheT8Advanced` —— 1/11 个有
- `ModelAttentionBackend` —— 1/11 个有
- `VideoCombineV2` —— 1/11 个有
- `XB_ReferenceAny` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
