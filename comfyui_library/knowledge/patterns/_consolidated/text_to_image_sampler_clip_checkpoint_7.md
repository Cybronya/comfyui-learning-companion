---
name: text_to_image_sampler_clip_checkpoint_7
type: Text To Image
frequency: 12
level: moderate
coverage: 0.882167
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图第4课：SDXL Refiner 精修，comfyui从入门到躺平系列教程_1979416721058598913.json, 图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json, 图片生成/文生图/新手工作流_2042208507885260802.json, 图片生成/文生图/森林岛大冒险1.0_1993881356163809282.json, 图片生成/文生图/艺术品高清图-青花龙_1778063653963108354.json, 平台全量/3D艺术花卉_1809053701435797506.json, 平台全量/Gameican游戏图标_1813100947754639362.json, 平台全量/三维半透明图标生成器_1792819874846789634.json, 平台全量/书画卷轴_1810574567969632257.json, 平台全量/可爱甜品餐车_1790585252880699394.json, 平台全量/大型载具_1788763953355091969.json, 平台全量/游戏角色_1807710611936620545.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/文生图第4课：SDXL Refiner 精修，comfyui从入门到躺平系列教程_1979416721058598913.json、图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json、图片生成/文生图/新手工作流_2042208507885260802.json、图片生成/文生图/森林岛大冒险1.0_1993881356163809282.json、图片生成/文生图/艺术品高清图-青花龙_1778063653963108354.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 10/12 个有
- `LoraLoader` —— 9/12 个有
- `ImageUpscaleWithModel` —— 8/12 个有
- `UpscaleModelLoader` —— 8/12 个有
- `VAEEncode` —— 8/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `Text Concatenate` —— 2/12 个有
- `ttN text` —— 2/12 个有
- `LoadImage` —— 1/12 个有
- `RMBG` —— 1/12 个有
- `Text Multiline` —— 1/12 个有
- `WD14Tagger|pysssss` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1280 | 12 | 86% |
| 高度 | 1024 | 512 - 1280 | 12 | 79% |
| 采样步数 | 20 | 5 - 230 | 12 | 0% |
| Prompt 约束强度(CFG) | 8 | 2 - 8 | 12 | 67% |
| 采样算法 | euler_ancestral | - | 12 | 42% |
| 调度器 | normal | - | 12 | 50% |
| 重绘幅度 | 0.475 | 0.25 - 1 | 12 | 50% |
| LoRA 模型强度 | 0.65 | 0.35 - 1 | 9 | 70% |
| LoRA 文本强度 | 1 | 0.3 - 1 | 9 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1280，12 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 512 - 1280，12 个样本
- 采样步数 中位数 20，观测区间 5 - 230，12 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 8，观测区间 2 - 8，12 个样本
- 采样算法 最常用 euler_ancestral，12 个样本，一致性 42%
- 调度器 最常用 normal，12 个样本，一致性 50%
- 重绘幅度 中位数 0.475，观测区间 0.25 - 1，12 个样本
- LoRA 模型强度 中位数 0.65，观测区间 0.35 - 1，9 个样本
- LoRA 文本强度 中位数 1，观测区间 0.3 - 1，9 个样本
- 风险：采样步数 观测到 230，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
