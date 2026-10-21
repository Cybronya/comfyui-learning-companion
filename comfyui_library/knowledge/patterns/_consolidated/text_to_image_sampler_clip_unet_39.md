---
name: text_to_image_sampler_clip_unet_39
type: Text To Image
frequency: 10
level: moderate
coverage: 0.8838
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree)]
members: [图片生成/文生图/1977407979249127426.json, 图片生成/文生图/1984067041122516994.json, 图片生成/文生图/47_anima文生图3lora工作流_2062720329054773250.json, 图片生成/文生图/48_anima文生图3lora工作流_2_2063974322926088193.json, 图片生成/文生图/87time 造相-Z-Image-Turbo_1992926870398238721.json, 图片生成/文生图/Anima Base 复古动漫文生图_2078659623917277185.json, 图片生成/文生图/Anima DMDX 四步极速版_2060754845304446978.json, 图片生成/文生图/Anima base v1 动漫生图_2059172782583410690.json, 图片生成/文生图/Anima base v1 动漫生图_2093989338236407810.json, 图片生成/文生图/Anima+2.9b+vs+Anima base+生图_2089681885474680834.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1977407979249127426.json、图片生成/文生图/1984067041122516994.json、图片生成/文生图/47_anima文生图3lora工作流_2062720329054773250.json、图片生成/文生图/48_anima文生图3lora工作流_2_2063974322926088193.json、图片生成/文生图/87time 造相-Z-Image-Turbo_1992926870398238721.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/10 个有
- `ModelSamplingAuraFlow` —— 4/10 个有
- `AddLabel` —— 3/10 个有
- `PrimitiveInt` —— 3/10 个有
- `PreviewAny` —— 2/10 个有
- `AILab_QwenVL` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LayerUtility: TextJoin` —— 1/10 个有
- `Text` —— 1/10 个有
- `TextEncodeQwenImageEditPlus` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 896 - 1920 | 10 | 74% |
| 高度 | 1260 | 768 - 1920 | 10 | 76% |
| 采样步数 | 25 | 4 - 30 | 10 | 45% |
| Prompt 约束强度(CFG) | 4 | 1 - 5 | 10 | 46% |
| 采样算法 | er_sde | - | 10 | 50% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 896 - 1920，10 个样本
- 高度 中位数 1260，观测区间 768 - 1920，10 个样本
- 采样步数 中位数 25，观测区间 4 - 30，10 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 5，10 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 er_sde，10 个样本，一致性 50%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)
