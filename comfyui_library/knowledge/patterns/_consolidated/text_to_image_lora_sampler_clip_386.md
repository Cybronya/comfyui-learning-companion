---
name: text_to_image_lora_sampler_clip_386
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8514
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewAny, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen+Next-Scene-V2-影视剧情分镜-自动提示词_1983383446804471809.json, 图片生成/图生图/qwen_image_edit_plus_nextscene_v2_1982130472799084545.json, 图片生成/图生图/影视短剧导演之连续画面AI导演工作流之-生图_1989691164641120258.json, 图片生成/图生图/微缩景观图片生成_1983795666323480578.json, 图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_386

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen+Next-Scene-V2-影视剧情分镜-自动提示词_1983383446804471809.json、图片生成/图生图/qwen_image_edit_plus_nextscene_v2_1982130472799084545.json、图片生成/图生图/影视短剧导演之连续画面AI导演工作流之-生图_1989691164641120258.json、图片生成/图生图/微缩景观图片生成_1983795666323480578.json、图片生成/文生图/qwen_image_edit_plus_Miniature_Worlds_1977407979249127426.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/5 个有
- `StringReplace` —— 3/5 个有
- `easy promptLine` —— 3/5 个有
- `GetImageSize` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0 - 1 | 5 | 50% |
| 宽度 | 1080 | 1080 - 1920 | 5 | 71% |
| 高度 | 1920 | 1080 - 1920 | 5 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0 - 1，5 个样本
- 宽度 中位数 1080，观测区间 1080 - 1920，5 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，5 个样本
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
