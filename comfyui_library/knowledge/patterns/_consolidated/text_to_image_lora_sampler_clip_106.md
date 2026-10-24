---
name: text_to_image_lora_sampler_clip_106
type: Text To Image
frequency: 13
level: moderate
coverage: 0.923846
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/侧躺v1-qwen_2007031839227121665.json, 图片生成/图生图/侧躺v2-qwen_2007034788410040321.json, 图片生成/图生图/俯卧撑-qwen_2007253375464771585.json, 图片生成/图生图/唯美朦胧qwen_2004687491070394370.json, 图片生成/图生图/坐在椅子上qwen_2003080195269697538.json, 图片生成/图生图/清冷古水墨qwen_2004131003285291010.json, 图片生成/图生图/潜水自拍-qwen_2019930247847743489.json, 图片生成/图生图/瑜伽趴qwen_2004167335042818050.json, 图片生成/图生图/细腰肥腿qwen_2001563164082860034.json, 图片生成/图生图/背对镜头qwen_2004791573655289858.json, 图片生成/图生图/舞台剧qwen_1985312105345728513.json, 图片生成/图生图/钢琴女神-qwen_2007336836372369410.json, 图片生成/文生图/Qwen-鬼刀画风_2005241079274373122.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/侧躺v1-qwen_2007031839227121665.json、图片生成/图生图/侧躺v2-qwen_2007034788410040321.json、图片生成/图生图/俯卧撑-qwen_2007253375464771585.json、图片生成/图生图/唯美朦胧qwen_2004687491070394370.json、图片生成/图生图/坐在椅子上qwen_2003080195269697538.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/13 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 12/13 个有
- `GLM_Text_Chat` —— 4/13 个有
- `PreviewAny` —— 3/13 个有
- `ImageUpscaleWithModel` —— 2/13 个有
- `MultiTextConcatenate` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `RH_Captioner` —— 2/13 个有
- `UpscaleModelLoader` —— 2/13 个有
- `VAEEncode` —— 2/13 个有
- `FlashVSRNode` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/13 个有
- `RandomLineFromText` —— 1/13 个有
- `TextEncodeQwenImageEdit` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 13 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 13 | 35% |
| 采样算法 | euler | - | 13 | 77% |
| 调度器 | beta | - | 13 | 46% |
| 重绘幅度 | 1 | 0.1 - 1 | 13 | 74% |
| 宽度 | 1024 | 928 - 1664 | 13 | 72% |
| 高度 | 1536 | 720 - 1664 | 13 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，13 个样本，一致性 77%
- 调度器 最常用 beta，13 个样本，一致性 46%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，13 个样本
- 宽度 中位数 1024，观测区间 928 - 1664，13 个样本
- 高度 中位数 1536，观测区间 720 - 1664，13 个样本
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
