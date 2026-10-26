---
name: text_to_image_sampler_clip_vae_6
type: Text To Image
frequency: 18
level: moderate
coverage: 0.9455
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1650 4G 文生图_Z-image量化 低显存_2061641168311640065.json, 图片生成/文生图/2029960172382195714.json, 图片生成/文生图/2030697459789336578.json, 图片生成/文生图/47_anima文生图3lora工作流_2062720329054773250.json, 图片生成/文生图/48_anima文生图3lora工作流_2_2063974322926088193.json, 图片生成/文生图/87time # 30  通义千问 QW 中文生成_1938456564812414977.json, 图片生成/文生图/A1、文生图千问2.5高保真 - 和风_1984067041122516994.json, 图片生成/文生图/KREA2-CC人像版_2095722389442224130.json, 图片生成/文生图/Z-Image-Engineer-V4--文生图_2028091411702222850.json, 图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2001971849082859521.json, 图片生成/文生图/Z-image D-OPSD文生图_2056614357865418754.json, 图片生成/文生图/Z-image D-OPSD文生图_2056619453462441985.json, 图片生成/文生图/Z-image D-OPSD文生图_2057839881359020034.json, 图片生成/文生图/Z-image Qwen3 4B Vs Qwen3 4b Z-image Engineer V4_2027773457253011458.json, 图片生成/文生图/Z-image-Turbo电影质感文生图_2056911427314737153.json, 图片生成/文生图/Z-image-turbo Vs flow-dpo对比_2026971124013207554.json, 图片生成/文生图/Z-image-turbo Vs flow-dpo对比工作流 林耀2.27_2027214097611231233.json, 图片生成/文生图/（贞贞Lora）Z-image同丹不同配方Lora对比测试_1996261458461736961.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_6

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/1650 4G 文生图_Z-image量化 低显存_2061641168311640065.json、图片生成/文生图/2029960172382195714.json、图片生成/文生图/2030697459789336578.json、图片生成/文生图/47_anima文生图3lora工作流_2062720329054773250.json、图片生成/文生图/48_anima文生图3lora工作流_2_2063974322926088193.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 17/18 个有
- `CLIPLoader` —— 15/18 个有
- `LoraLoaderModelOnly` —— 15/18 个有
- `CR Prompt Text` —— 10/18 个有
- `ConditioningZeroOut` —— 10/18 个有
- `easy seed` —— 8/18 个有
- `AddLabel` —— 4/18 个有
- `CLIPLoaderGGUF` —— 4/18 个有
- `ImageConcanate` —— 4/18 个有
- `PreviewImage` —— 3/18 个有
- `Label (rgthree)` —— 2/18 个有
- `Seed (rgthree)` —— 2/18 个有
- `Int` —— 1/18 个有
- `PDIMAGE_LongerSize` —— 1/18 个有
- `UnetLoaderGGUF` —— 1/18 个有
- `easy promptLine` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 304 - 1920 | 18 | 68% |
| 高度 | 1920 | 304 - 1984 | 18 | 67% |
| 采样步数 | 10 | 8 - 25 | 18 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 18 | 29% |
| 采样算法 | euler | - | 18 | 89% |
| 调度器 | simple | - | 18 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 304 - 1920，18 个样本
- 高度 中位数 1920，观测区间 304 - 1984，18 个样本
- 采样步数 中位数 10，观测区间 8 - 25，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，18 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，18 个样本，一致性 89%
- 调度器 最常用 simple，18 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
