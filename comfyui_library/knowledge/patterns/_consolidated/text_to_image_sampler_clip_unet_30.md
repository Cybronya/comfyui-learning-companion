---
name: text_to_image_sampler_clip_unet_30
type: Text To Image
frequency: 15
level: moderate
coverage: 0.889533
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Zimage提示词海报逃离城市-拥抱自然_2057800201645154306.json, 图片生成/图生图/电商海报生成_2036017494078525441.json, 图片生成/图生图/百度ERNIE-image-turbo-自动提示词工作流_2044578766483103746.json, 图片生成/文生图/Z-image-Kook+Qwn3.5 反推提示词海报设计_2037007954775379969.json, 图片生成/文生图/Z-image头像生成器V2.0_2054103430381228033.json, 图片生成/文生图/Z-image头像生成器_1993848457626664961.json, 图片生成/文生图/Z-image头像生成器文生图_2052591390210707458.json, 图片生成/文生图/Zimage头像生成器_2057990922343899138.json, 图片生成/文生图/Zimage头像生成器_2061075705567473666.json, 图片生成/文生图/Zimage头像生成器_2072198363075923969.json, 图片生成/文生图/Zimage提示词海报设计制作_2054214009636835329.json, 图片生成/文生图/z image海报设计，主图设计_2038970982379032577.json, 图片生成/文生图/提示词+海报一键生成_2046250266453876738.json, 平台全量/电商海报生成_2035574532760674305.json, 平台全量/老许Gary：电商海报一键生成_2079314127780143105.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Zimage提示词海报逃离城市-拥抱自然_2057800201645154306.json、图片生成/图生图/电商海报生成_2036017494078525441.json、图片生成/图生图/百度ERNIE-image-turbo-自动提示词工作流_2044578766483103746.json、图片生成/文生图/Z-image-Kook+Qwn3.5 反推提示词海报设计_2037007954775379969.json、图片生成/文生图/Z-image头像生成器V2.0_2054103430381228033.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/15 个有
- `PreviewImage` —— 14/15 个有
- `CR Text` —— 9/15 个有
- `ShowText|pysssss` —— 8/15 个有
- `ConditioningZeroOut` —— 7/15 个有
- `FastFilmGrain` —— 7/15 个有
- `LayerColor: BrightnessContrastV2` —— 7/15 个有
- `Latent Noise Injection` —— 6/15 个有
- `LoadImage` —— 1/15 个有
- `Text Concatenate (JPS)` —— 1/15 个有
- `easy positive` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 15 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 53% |
| 调度器 | bong_tangent | - | 15 | 47% |
| 重绘幅度 | 1 | 0.3 - 1 | 15 | 52% |
| 宽度 | 1080 | 720 - 1440 | 15 | 87% |
| 高度 | 1536 | 1280 - 1920 | 15 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，15 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 53%
- 调度器 最常用 bong_tangent，15 个样本，一致性 47%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，15 个样本
- 宽度 中位数 1080，观测区间 720 - 1440，15 个样本，取值集中（一致性 87%）
- 高度 中位数 1536，观测区间 1280 - 1920，15 个样本，取值集中（一致性 87%）
- 高发问题（9/15 个样本）：Steps较低可能导致细节不足
