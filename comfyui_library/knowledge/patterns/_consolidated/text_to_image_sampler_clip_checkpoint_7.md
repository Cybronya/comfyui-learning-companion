---
name: text_to_image_sampler_clip_checkpoint_7
type: Text To Image
frequency: 9
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/1979490298709577729.json, 图片生成/文生图/1989688004904185857.json, 图片生成/文生图/controlnet文生图SD_2096536231768317953.json, 图片生成/文生图/智能助手 - AI秘书在你身边_1880174533549387777.json, 图片生成/文生图/校园天台动漫女孩_2104024650153025537.json, 图片生成/文生图/视频跟练_2106961244719767554.json, 数字人/数字人/酒吧美男_2089335688880807938.json, 视频生成/图生视频/2053664172625408002.json, 视频生成/图生视频/2053673513051013121.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1979490298709577729.json、图片生成/文生图/1989688004904185857.json、图片生成/文生图/controlnet文生图SD_2096536231768317953.json、图片生成/文生图/智能助手 - AI秘书在你身边_1880174533549387777.json、图片生成/文生图/校园天台动漫女孩_2104024650153025537.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/9 个有
- `IPAdapterUnifiedLoader` —— 3/9 个有
- `IPAdapterAdvanced` —— 2/9 个有
- `IPAdapterStyleComposition` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 50 | 9 | 63% |
| Prompt 约束强度(CFG) | 7 | 3.5 - 8 | 9 | 79% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | normal | - | 9 | 56% |
| 重绘幅度 | 1 | 0.9 - 1 | 9 | 97% |
| 宽度 | 768 | 480 - 1280 | 9 | 65% |
| 高度 | 720 | 512 - 1536 | 9 | 62% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 50，9 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 3.5 - 8，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 normal，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，9 个样本，取值集中（一致性 97%）
- 宽度 中位数 768，观测区间 480 - 1280，9 个样本
- 高度 中位数 720，观测区间 512 - 1536，9 个样本
