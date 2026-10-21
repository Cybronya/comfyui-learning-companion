---
name: text_to_image_lora_sampler_clip_248
type: Text To Image
frequency: 5
level: strong
coverage: 0.9052
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3 OpenVDN DMD8深度引导生视频｜动作运镜结构全迁移_2103660126132596738.json, 视频生成/文生视频/MiniMax H3 OpenVDN DMD8深度视频引导生成，动作运镜结构迁移方案_2103894634056478721.json, 视频生成/文生视频/MiniMax H3 PDD 8步参考生视频 文生视频多模态处理_2098697368001671170.json, 视频生成/文生视频/MiniMax H3动作自然度增强 本地DiT推理运动流畅不僵硬_2098644023186649089.json, 视频生成/视频生视频/MiniMax H3视频编辑视频翻拍二创与指定角色替换_视频生视频工具_2105712272248233985.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_248

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 OpenVDN DMD8深度引导生视频｜动作运镜结构全迁移_2103660126132596738.json、视频生成/文生视频/MiniMax H3 OpenVDN DMD8深度视频引导生成，动作运镜结构迁移方案_2103894634056478721.json、视频生成/文生视频/MiniMax H3 PDD 8步参考生视频 文生视频多模态处理_2098697368001671170.json、视频生成/文生视频/MiniMax H3动作自然度增强 本地DiT推理运动流畅不僵硬_2098644023186649089.json、视频生成/视频生视频/MiniMax H3视频编辑视频翻拍二创与指定角色替换_视频生视频工具_2105712272248233985.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `GetVideoComponents` —— 3/5 个有
- `LoadVideo` —— 3/5 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 3/5 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `Video Slice` —— 3/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/5 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 1/5 个有
- `MiniMaxH3LoRACompatibilityLoaderT8Advanced` —— 1/5 个有
- `MiniMaxH3PDD8StepSetupT8Advanced` —— 1/5 个有

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
