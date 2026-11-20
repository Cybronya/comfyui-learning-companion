---
name: unknown_workflow_upscale_sampler_clip_16
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.985111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KOOK_ImageCompression, KOOK_SaveJPGImage, KSampler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/最新zimage_base高清4k美女生成器-墨幽版_2066851974158569474.json, 图片生成/文生图/墨幽-4kccd-纯文生_2067530864917049346.json, 图片生成/文生图/墨幽2kccd横屏4张_2065337333741867010.json, 图片生成/文生图/墨幽2kccd横屏4张_2065355065250115585.json, 图片生成/文生图/墨幽人造人ZIB-8步-2K4k_2068286081765822465.json, 图片生成/文生图/墨幽人造人ZIB-8步-4k_2065310807159828481.json, 图片生成/文生图/最新zimage base高清4k美女生成器-墨幽版_2066512473188036610.json, 图片生成/文生图/高清写实人物+墨幽-4kccd-文生图_2067807084611194881.json, 平台全量/Z-IMAGE-超逼真高清人像生成_2067871426543177729.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/最新zimage_base高清4k美女生成器-墨幽版_2066851974158569474.json、图片生成/文生图/墨幽-4kccd-纯文生_2067530864917049346.json、图片生成/文生图/墨幽2kccd横屏4张_2065337333741867010.json、图片生成/文生图/墨幽2kccd横屏4张_2065355065250115585.json、图片生成/文生图/墨幽人造人ZIB-8步-2K4k_2068286081765822465.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `KSampler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/9 个有
- `JjkText` —— 2/9 个有
- `RHHiddenNodes` —— 2/9 个有
- `RepeatLatentBatch` —— 2/9 个有
- `Text` —— 2/9 个有
- `easy saveText` —— 2/9 个有
- `忽略多组孤海` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 9 | 9 | 96% |
| Prompt 约束强度(CFG) | 2 | 1 - 2 | 9 | 83% |
| 采样算法 | res_2s | - | 9 | 89% |
| 调度器 | bong_tangent | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，9 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 2，9 个样本，取值集中（一致性 83%）
- 采样算法 最常用 res_2s，9 个样本，一致性 89%
- 调度器 最常用 bong_tangent，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
