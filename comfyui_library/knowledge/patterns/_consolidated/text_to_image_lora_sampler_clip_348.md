---
name: text_to_image_lora_sampler_clip_348
type: Text To Image
frequency: 6
level: weak
coverage: 0.927167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/PromptLine+Anima 艺术家批量风格测试_2029160162027638786.json, 图片生成/文生图/Z image_绝对美写实人像_2045520449718718466.json, 图片生成/文生图/Z image_绝对美写实人像_2063211868080140290.json, 图片生成/文生图/Z image绝对美写实人像｜美少女文生图质感在线_2101553419847815169.json, 图片生成/文生图/krea2免LORA文生图｜无需训练直接出图省心版_2111061448398041089.json, 图片生成/文生图/全能图片G image 2.0文生图官方稳定版｜文生图放心冲_2111830361557786625.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_348

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/PromptLine+Anima 艺术家批量风格测试_2029160162027638786.json、图片生成/文生图/Z image_绝对美写实人像_2045520449718718466.json、图片生成/文生图/Z image_绝对美写实人像_2063211868080140290.json、图片生成/文生图/Z image绝对美写实人像｜美少女文生图质感在线_2101553419847815169.json、图片生成/文生图/krea2免LORA文生图｜无需训练直接出图省心版_2111061448398041089.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy promptLine` —— 4/6 个有
- `Int` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `TextInput_` —— 3/6 个有
- `solarL_SaveImagesToZip` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `AdjustContrast` —— 1/6 个有
- `JWStringConcat` —— 1/6 个有
- `RH_RhartImageG2OfficialTextToImage` —— 1/6 个有
- `String Literal` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 552 | 80 - 1080 | 6 | 14% |
| 高度 | 552 | 80 - 1920 | 6 | 3% |
| 采样步数 | 6 | 4 - 20 | 6 | 29% |
| Prompt 约束强度(CFG) | 2.95 | 1 - 4.5 | 6 | 40% |
| 采样算法 | er_sde | - | 6 | 50% |
| 调度器 | beta | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 552，观测区间 80 - 1080，6 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，观测区间 80 - 1920，6 个样本，取值分散，一致性仅 3%
- 采样步数 中位数 6，观测区间 4 - 20，6 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 2.95，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 er_sde，6 个样本，一致性 50%
- 调度器 最常用 beta，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
