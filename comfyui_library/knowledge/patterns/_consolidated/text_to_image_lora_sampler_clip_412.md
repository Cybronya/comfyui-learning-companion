---
name: text_to_image_lora_sampler_clip_412
type: Text To Image
frequency: 5
level: strong
coverage: 0.8688
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3图片换头 图生视频人物替换处理生成工具_2100269102773395458.json, 视频生成/图生视频/H3图片换头生视频 图生视频创作处理工具_2100267469515608066.json, 视频生成/图生视频/漫剧林辰角色动态演绎 图生视频一键生成流畅画面_2104279422512754690.json, 视频生成/图生视频/短剧漫剧参考图生视频工作流，图生视频短剧制作方案_2103604319982542850.json, 视频生成/文生视频/H3文生视频加速版 官方Turbo加速出片_2099594371384561665.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_412

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/H3图片换头 图生视频人物替换处理生成工具_2100269102773395458.json、视频生成/图生视频/H3图片换头生视频 图生视频创作处理工具_2100267469515608066.json、视频生成/图生视频/漫剧林辰角色动态演绎 图生视频一键生成流畅画面_2104279422512754690.json、视频生成/图生视频/短剧漫剧参考图生视频工作流，图生视频短剧制作方案_2103604319982542850.json、视频生成/文生视频/H3文生视频加速版 官方Turbo加速出片_2099594371384561665.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 4/5 个有
- `SaveVideo` —— 4/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `CR Color Panel` —— 2/5 个有
- `CR Text` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `ImageCompositeMasked` —— 2/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RH_LLMAPI_Pro_Node` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `MiniMaxH3ImageToVideo` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `easy saveVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
