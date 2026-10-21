---
name: text_to_image_sampler_clip_checkpoint_8
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9727
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/文生图宠物_1778280371394240514.json, 图片生成/文生图/智能助手 - AI秘书在你身边_1880174533549387777.json, 图片生成/文生图/校园天台动漫女孩_2104024650153025537.json, 图片生成/文生图/橘红晚霞_2083896592209371137.json, 图片生成/文生图/治愈系吉卜力手绘质感_2071054394577211394.json, 图片生成/文生图/测试_2011714143212019713.json, 图片生成/文生图/深秋庭院闺阁小院_2084285079899168769.json, 图片生成/文生图/深蓝色水手服美少女战士_2080967268124684290.json, 图片生成/文生图/清晰_2013889963875639297.json, 图片生成/文生图/酒馆2D角色卡封面生成_2002452758932385793.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/文生图宠物_1778280371394240514.json、图片生成/文生图/智能助手 - AI秘书在你身边_1880174533549387777.json、图片生成/文生图/校园天台动漫女孩_2104024650153025537.json、图片生成/文生图/橘红晚霞_2083896592209371137.json、图片生成/文生图/治愈系吉卜力手绘质感_2071054394577211394.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPSetLastLayer` —— 2/10 个有
- `LatentUpscaleBy` —— 2/10 个有
- `HAIGC_SaveImagesToZip` —— 1/10 个有
- `LoraLoader` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `VAELoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 768 | 10 | 83% |
| 高度 | 968 | 512 - 1024 | 10 | 73% |
| 采样步数 | 37.5 | 20 - 60 | 10 | 55% |
| Prompt 约束强度(CFG) | 5 | 3.5 - 8 | 10 | 64% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | normal | - | 10 | 80% |
| 重绘幅度 | 1 | 0.5 - 1 | 10 | 80% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 768，10 个样本，取值集中（一致性 83%）
- 高度 中位数 968，观测区间 512 - 1024，10 个样本
- 采样步数 中位数 37.5，观测区间 20 - 60，10 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 3.5 - 8，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 normal，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，10 个样本，取值集中（一致性 80%）
