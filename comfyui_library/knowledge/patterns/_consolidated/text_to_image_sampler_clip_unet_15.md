---
name: text_to_image_sampler_clip_unet_15
type: Text To Image
frequency: 22
level: weak
coverage: 0.9895
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image批量写提示词出图_2109157072960057346.json, 图片生成/文生图/Z-image批量写提示词出图_2116706059661438978.json, 图片生成/文生图/Z-image批量写提示词出图_2116720173221769218.json, 图片生成/文生图/Z-image文生图   自然风格首选_1993896427099193345.json, 图片生成/文生图/Z-image文生图_1993860952581931009.json, 图片生成/文生图/Z-image文生图人像摄影2K版_1994574159525126145.json, 图片生成/文生图/Z-image文生图（最新加速版）_1996623220235182081.json, 图片生成/文生图/Z-image文生图（非收敛-随机种子生效版）_1996582595745955841.json, 图片生成/文生图/boogu turbo文生图加速版V1_2067837356199202818.json, 图片生成/文生图/boogu turbo文生图加速版V1_2068270357320126466.json, 图片生成/文生图/boogu turbo文生图加速版工作流_2067860195535052801.json, 图片生成/文生图/boogu turbo文生图加速版工作流_2067879436858511361.json, 图片生成/文生图/boogu文生图满血版工作流_2067862555661520898.json, 图片生成/文生图/boogu文生图满血版工作流_2067880773423816705.json, 图片生成/文生图/boogu满血版文生图V1_2067838674468958210.json, 图片生成/文生图/boogu满血版文生图V1_2068275477441236993.json, 图片生成/文生图/krea2-Afterlight（光影美学文生图）_2083839367738642434.json, 图片生成/文生图/krea2_ID13_v2_融合prompt_单分支_2086591602310602754.json, 图片生成/文生图/krea2_对比流_官方vsAnima配方_random_2086586562653024257.json, 图片生成/文生图/（fg-Lora）Z-image Engineer V4-文生图V2（3000步）_2028626642955935746.json, 图片生成/文生图/（小情绪版）Z-image文生图V1_1999752612872417281.json, 图片生成/文生图/（自用-zhenzhen）Z-image-turbo文生图2K版_2019482059055566849.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_15

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/Z-image批量写提示词出图_2109157072960057346.json、图片生成/文生图/Z-image批量写提示词出图_2116706059661438978.json、图片生成/文生图/Z-image批量写提示词出图_2116720173221769218.json、图片生成/文生图/Z-image文生图   自然风格首选_1993896427099193345.json、图片生成/文生图/Z-image文生图_1993860952581931009.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 21/22 个有
- `ConditioningZeroOut` —— 19/22 个有
- `CR Prompt Text` —— 15/22 个有
- `easy promptLine` —— 11/22 个有
- `LoraLoaderModelOnly` —— 10/22 个有
- `RH_LLMAPI_Pro_Node` —— 3/22 个有
- `ShowText|pysssss` —— 3/22 个有
- `ConditioningKrea2Rebalance` —— 2/22 个有
- `ClipLoaderGGUF` —— 1/22 个有
- `DuckHideNode` —— 1/22 个有
- `MultiLinePrompt` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 50 | 22 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 22 | 25% |
| 采样算法 | euler | - | 22 | 59% |
| 调度器 | simple | - | 22 | 45% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 1052 | 896 - 1920 | 22 | 69% |
| 高度 | 1212 | 1024 - 1920 | 22 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 50，22 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，22 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，22 个样本，一致性 59%
- 调度器 最常用 simple，22 个样本，一致性 45%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 896 - 1920，22 个样本
- 高度 中位数 1212，观测区间 1024 - 1920，22 个样本
