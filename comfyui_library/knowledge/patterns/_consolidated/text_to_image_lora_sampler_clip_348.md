---
name: text_to_image_lora_sampler_clip_348
type: Text To Image
frequency: 5
level: strong
coverage: 0.842
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1图片编辑二号版｜图生图精细修改随心改_2112816409389649921.json, 图片生成/图生图/Qwen image 2.1角色四视图极速版｜4或8步加速秒出设定图_2103680364186259458.json, 图片生成/图生图/千问2.1多图像编辑工作流｜提示词自动优化省心出图_2103724810600804354.json, 图片生成/文生图/千问2.1图片编辑图生图工作流，文生图图生图双核引擎创作方案_2106474151585337346.json, 图片生成/文生图/千问Qwen2.1图片编辑神器｜文生图图生图双模式v260927新版本_2106191621074276353.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_348

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1图片编辑二号版｜图生图精细修改随心改_2112816409389649921.json、图片生成/图生图/Qwen image 2.1角色四视图极速版｜4或8步加速秒出设定图_2103680364186259458.json、图片生成/图生图/千问2.1多图像编辑工作流｜提示词自动优化省心出图_2103724810600804354.json、图片生成/文生图/千问2.1图片编辑图生图工作流，文生图图生图双核引擎创作方案_2106474151585337346.json、图片生成/文生图/千问Qwen2.1图片编辑神器｜文生图图生图双模式v260927新版本_2106191621074276353.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenPERewriteT8` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `FastGroupsBypassSwitch` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `EnhancedLoadDiffusionModel` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `KSamplerCacheable` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `ShowAnything|Mie` —— 2/5 个有
- `VAELoader_Any` —— 2/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `easy int` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

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
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
