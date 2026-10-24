---
name: unknown_workflow_sampler_checkpoint_vae_6
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.99125
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/大凯辰光-动漫转真人+Qwen+2511-在线工作流_2009514500982054913.json, 图片生成/图生图/大凯辰光-双图编辑_图像混合+Qwen+2511All In One 在线工作流_2009542498447790082.json, 图片生成/图生图/相同背景一致性Qwen-Edit Aio V5版本_1979016110806831105.json, 图片生成/图生图/（SFW版）Qwen-Edit 2511 Aio V23单图编辑_2016579981308071938.json, 图片生成/图生图/（同景同人随机版）Qwen-Edit Aio V5模型单图编辑_1978395444101451777.json, 图片生成/图生图/（同景同人随机版）Qwen-Edit Aio V5模型单图编辑_1978736627881283586.json, 图片生成/图生图/（自用）Qwen-Edit 2511 Aio V19单图编辑_2012905523384950786.json, 图片生成/图生图/（自用）Qwen-Edit 2511 Aio V20单图编辑_2012906084079505409.json, 图片生成/图生图/（自用）Qwen-Edit 2511 Aio V21单图编辑_2016579591296524289.json, 图片生成/图生图/（自用）Qwen-Edit 2511 Aio V22单图编辑_2016579760331169793.json, 图片生成/图生图/（自用）Qwen-Edit 2511 Aio V23单图编辑_2016579888261632002.json, 图片生成/图生图/🦖Qwen-Edit 2511 Aio视图编辑（自用）_2008059225108389889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_6

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/大凯辰光-动漫转真人+Qwen+2511-在线工作流_2009514500982054913.json、图片生成/图生图/大凯辰光-双图编辑_图像混合+Qwen+2511All In One 在线工作流_2009542498447790082.json、图片生成/图生图/相同背景一致性Qwen-Edit Aio V5版本_1979016110806831105.json、图片生成/图生图/（SFW版）Qwen-Edit 2511 Aio V23单图编辑_2016579981308071938.json、图片生成/图生图/（同景同人随机版）Qwen-Edit Aio V5模型单图编辑_1978395444101451777.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 11/12 个有
- `ImageConcanate` —— 11/12 个有
- `Text Multiline` —— 10/12 个有
- `CR Prompt Text` —— 6/12 个有
- `DuckHideNode` —— 6/12 个有
- `LoraLoaderModelOnly` —— 2/12 个有
- `Text` —— 2/12 个有
- `INTConstant` —— 1/12 个有
- `Int` —— 1/12 个有
- `TwoWaySwitch` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 10 | 12 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 58% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 768 | 768 - 1280 | 12 | 78% |
| 高度 | 768 | 720 - 768 | 12 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 10，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 58%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1280，12 个样本
- 高度 中位数 768，观测区间 720 - 768，12 个样本，取值集中（一致性 98%）
- 高发问题（6/12 个样本）：Steps较低可能导致细节不足
