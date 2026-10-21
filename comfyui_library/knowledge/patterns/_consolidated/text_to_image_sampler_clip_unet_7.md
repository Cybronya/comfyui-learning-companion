---
name: text_to_image_sampler_clip_unet_7
type: Text To Image
frequency: 21
level: moderate
coverage: 0.961476
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图_1993984303098953730.json, 图片生成/文生图/Z-image文生图_1994050196562706434.json, 图片生成/文生图/Z-image文生图_1994253056955138050.json, 图片生成/文生图/Z-image文生图_1994323420024422402.json, 图片生成/文生图/Z-image文生图_1994684914001977346.json, 图片生成/文生图/Z-image文生图_1996854775096516609.json, 图片生成/文生图/Z-image文生图_2002645259123322881.json, 图片生成/文生图/Z-image文生图_2002734393544306690.json, 图片生成/文生图/Z-image文生图_2003370209052401665.json, 图片生成/文生图/Z-image文生图——25年末的超级王炸_1994392372287053826.json, 图片生成/文生图/Z-image文生图人像摄影2K版_1994574159525126145.json, 图片生成/文生图/Z-image文生图（最新加速版）_1996623220235182081.json, 图片生成/文生图/Z-image文生图（非收敛-随机种子生效版）_1996582595745955841.json, 图片生成/文生图/boogu turbo文生图加速版V1_2067837356199202818.json, 图片生成/文生图/boogu turbo文生图加速版V1_2068270357320126466.json, 图片生成/文生图/boogu turbo文生图加速版工作流_2067860195535052801.json, 图片生成/文生图/boogu turbo文生图加速版工作流_2067879436858511361.json, 图片生成/文生图/boogu_base_文生图-支持复杂提示词_2069073383496708097.json, 图片生成/文生图/boogu_image_turbo 文生图_2074111380944408578.json, 图片生成/文生图/（小情绪版）Z-image文生图V1_1999752612872417281.json, 图片生成/文生图/（自用）成人摄影Z-image文生图2K版_1993954086909313026.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/Z-image文生图_1993984303098953730.json、图片生成/文生图/Z-image文生图_1994050196562706434.json、图片生成/文生图/Z-image文生图_1994253056955138050.json、图片生成/文生图/Z-image文生图_1994323420024422402.json、图片生成/文生图/Z-image文生图_1994684914001977346.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 20/21 个有
- `CR Prompt Text` —— 11/21 个有
- `PreviewImage` —— 5/21 个有
- `easy promptLine` —— 5/21 个有
- `LoraLoaderModelOnly` —— 4/21 个有
- `Anything Everywhere3` —— 1/21 个有
- `Float` —— 1/21 个有
- `JWInteger` —— 1/21 个有
- `TT_img_enc` —— 1/21 个有
- `TT_img_enc_v2` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 40 | 21 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 21 | 44% |
| 采样算法 | euler | - | 21 | 67% |
| 调度器 | simple | - | 21 | 52% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 1080 | 680 - 1920 | 21 | 66% |
| 高度 | 1080 | 720 - 1920 | 21 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 40，21 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，21 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，21 个样本，一致性 67%
- 调度器 最常用 simple，21 个样本，一致性 52%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 680 - 1920，21 个样本
- 高度 中位数 1080，观测区间 720 - 1920，21 个样本
