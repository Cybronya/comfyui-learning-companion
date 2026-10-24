---
name: text_to_image_sampler_clip_unet_136
type: Text To Image
frequency: 5
level: strong
coverage: 0.899
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, EmptyLatentImage, JWInteger, KSampler, RH_LLMAPI_NODE, SaveImage, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, Wan_video_prompt_generator]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/wan2.2低频超真实+批量文生图（自动提示词）V3_1950771546711351297.json, 图片生成/文生图/wan2.2超真实+批量文生图（自动提示词）V4_1955481041341485058.json, 图片生成/文生图/wan2.2超真实+批量文生图（自动提示词）V4_2033193785663954945.json, 图片生成/文生图/wan2.2高低频超真实+超级快文生图_2028351546110517249.json, 图片生成/文生图/wan2.2高低频超真实+超级快文生图（自动提示词）V2_1950700991370973185.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_136

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/wan2.2低频超真实+批量文生图（自动提示词）V3_1950771546711351297.json、图片生成/文生图/wan2.2超真实+批量文生图（自动提示词）V4_1955481041341485058.json、图片生成/文生图/wan2.2超真实+批量文生图（自动提示词）V4_2033193785663954945.json、图片生成/文生图/wan2.2高低频超真实+超级快文生图_2028351546110517249.json、图片生成/文生图/wan2.2高低频超真实+超级快文生图（自动提示词）V2_1950700991370973185.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `JWInteger`
- `KSampler`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `Wan_video_prompt_generator`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStarAndInit` —— 3/5 个有
- `LoraLoader` —— 3/5 个有
- `RHHiddenNodes` —— 3/5 个有
- `Bjornulf_TextToStringAndSeed` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `ModelSamplingSD3` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | 0.4 - 0.4 | 3 | 100% |
| LoRA 文本强度 | 0.4 | 0.4 - 0.4 | 3 | 100% |
| 采样步数 | 8 | 8 - 10 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_2s | - | 5 | 60% |
| 调度器 | bong_tangent | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 512 | 512 - 512 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，5 个样本，一致性 60%
- 调度器 最常用 bong_tangent，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
