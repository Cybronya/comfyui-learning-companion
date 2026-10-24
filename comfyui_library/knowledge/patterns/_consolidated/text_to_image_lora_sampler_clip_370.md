---
name: text_to_image_lora_sampler_clip_370
type: Text To Image
frequency: 5
level: weak
coverage: 0.9106
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/PromptLine+Anima 艺术家批量风格测试_2029160162027638786.json, 图片生成/文生图/Z image_绝对美写实人像_2045520449718718466.json, 图片生成/文生图/Z image_绝对美写实人像_2063211868080140290.json, 图片生成/文生图/Z image绝对美写实人像｜美少女文生图质感在线_2101553419847815169.json, 图片生成/文生图/全能图片文生图，多风格题材一workflow通吃_2112307328287596546.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_370

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/PromptLine+Anima 艺术家批量风格测试_2029160162027638786.json、图片生成/文生图/Z image_绝对美写实人像_2045520449718718466.json、图片生成/文生图/Z image_绝对美写实人像_2063211868080140290.json、图片生成/文生图/Z image绝对美写实人像｜美少女文生图质感在线_2101553419847815169.json、图片生成/文生图/全能图片文生图，多风格题材一workflow通吃_2112307328287596546.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
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
- `TextInput_` —— 4/5 个有
- `easy promptLine` —— 4/5 个有
- `Int` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `solarL_SaveImagesToZip` —— 2/5 个有
- `孤海注释` —— 2/5 个有
- `AdjustContrast` —— 1/5 个有
- `JWStringConcat` —— 1/5 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/5 个有
- `String Literal` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1080 | 5 | 28% |
| 高度 | 1024 | 80 - 1920 | 5 | 18% |
| 采样步数 | 8 | 4 - 20 | 5 | 33% |
| Prompt 约束强度(CFG) | 1.4 | 1 - 4.5 | 5 | 33% |
| 采样算法 | res_2s | - | 5 | 40% |
| 调度器 | bong_tangent | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1080，5 个样本，取值分散，一致性仅 28%
- 高度 中位数 1024，观测区间 80 - 1920，5 个样本，取值分散，一致性仅 18%
- 采样步数 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1.4，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 res_2s，5 个样本，一致性 40%
- 调度器 最常用 bong_tangent，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
