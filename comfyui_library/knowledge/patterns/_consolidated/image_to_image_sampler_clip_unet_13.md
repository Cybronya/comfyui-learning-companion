---
name: image_to_image_sampler_clip_unet_13
type: Image To Image
frequency: 15
level: weak
coverage: 0.995867
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图-百度-ERNIE-Image_2044557979541835777.json, 图片生成/图生图/图生图工作流77_2114259153182089217.json, 图片生成/图生图/场景洗图_2065796507659497474.json, 图片生成/图生图/旗袍美女qwen2512_2033779880537624578.json, 图片生成/图生图/日常穿搭Qwen2512真实人像质感御姐美女_2040711683684962306.json, 图片生成/图生图/昏暗灯光Qwen2512真实人像质感御姐美女_2040742192599277569.json, 图片生成/图生图/晚礼服Qwen2512真实人像质感御姐美女_2040739616071880706.json, 图片生成/图生图/欧式美女Qwen2512真实人像质感御姐美女_2040716624658960385.json, 图片生成/图生图/现代客厅美女Qwen2512真实人像质感御姐美女_2040726673531871234.json, 图片生成/图生图/睡衣系列Qwen2512真实人像质感御姐美女_2040663406696472578.json, 图片生成/图生图/短裤Qwen2512真实人像质感御姐美女_2040678187201470465.json, 图片生成/图生图/立体立绘Qwen2512真实人像质感御姐美女_2040764555873226753.json, 图片生成/图生图/粉色长发Qwen2512真实人像质感御姐美女_2040766504697860098.json, 图片生成/图生图/美女写真图Qwen2512真实人像质感御姐美女_2040708454158962689.json, 图片生成/图生图/蕾丝内衣Qwen2512真实人像质感御姐美女_2040698349422125057.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/图生图-百度-ERNIE-Image_2044557979541835777.json、图片生成/图生图/图生图工作流77_2114259153182089217.json、图片生成/图生图/场景洗图_2065796507659497474.json、图片生成/图生图/旗袍美女qwen2512_2033779880537624578.json、图片生成/图生图/日常穿搭Qwen2512真实人像质感御姐美女_2040711683684962306.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/15 个有
- `scale` —— 13/15 个有
- `ModelSamplingAuraFlow` —— 12/15 个有
- `Note _O` —— 12/15 个有
- `BiRefNet_Loader_LG` —— 1/15 个有
- `DF_Get_image_size` —— 1/15 个有
- `Image Comparer (rgthree)` —— 1/15 个有
- `ImageResizeKJv2` —— 1/15 个有
- `RepeatLatentBatch` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 15 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 15 | 66% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | beta | - | 15 | 87% |
| 重绘幅度 | 0.5 | 0.1 - 1 | 15 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，15 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 87%
- 重绘幅度 中位数 0.5，观测区间 0.1 - 1，15 个样本
- 高发问题（13/15 个样本）：Steps较低可能导致细节不足
